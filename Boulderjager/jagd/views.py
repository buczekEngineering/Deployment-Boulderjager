from .forms import AddBoulderFormBJM, AddBoulderFormBJW, AddBoulderFormUE50M, AddBoulderFormU18M, \
    AddBoulderFormU18W, AddBoulderFormUE50W
from .boulders_controller import get_sorted_boulder_data_based_on, get_existing_boulder_data, \
    retrieve_boulders_based_on_, retrieve_tops_amount, retrieve_zones_amount, category2boulder_model__mapping
from django.contrib.auth.decorators import login_required
import logging
from .models import UserProfile, U18W, U18M, UE50W, UE50M, BJM, BJW
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

import csv
logger = logging.getLogger(__name__)


def home(request):
    return render(request, "home.html")


def export_combined_data_to_csv(request):
    users_profiles = UserProfile.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="combined_data.csv"'

    fieldnames = ['user', 'category','points']
    boulder_fieldnames = [f'boulder_{i}' for i in range(1, 31)]  # List of boulder field names

    # Combine all field names
    all_fieldnames = fieldnames + boulder_fieldnames

    writer = csv.DictWriter(response, fieldnames=all_fieldnames)
    writer.writeheader()  # Write all_fieldnames as headers in the CSV

    for profile in users_profiles:
        category = f"{profile.mode}_{profile.gender}"
        model_name = category2boulder_model__mapping(category)

        if model_name:
            user_data = model_name.objects.filter(user=profile.user).first()

            if user_data:

                user = user_data.user
                user_values = {
                    'user': user.first_name + ' ' + user.last_name,
                    'category': category.replace('_', ' ').title(),
                    'points': user_data.points,

                }

                for i in range(1, 31):
                    boulder_field = f'boulder_{i}'
                    boulder_value = getattr(user_data, boulder_field)
                    user_values[boulder_field] = boulder_value

                writer.writerow(user_values)

    return response

def export_rankings_to_csv(request):
    modes = ["u18", "bj", "ue50"]
    genders = ["man", "woman"]

    rankings_data = []
    for mode in modes:
        for gender in genders:
            category = f"{mode}_{gender}"
            data = get_sorted_boulder_data_based_on(category)
            for idx, entry_data in enumerate(data, start=1):
                user = entry_data.user
                rankings_data.append({
                    'category': category.replace('_', ' ').title(),
                    'idx': idx,
                    'user_name': f"{user.first_name} {user.last_name}",
                    'points': entry_data.points
                })

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rankings.csv"'

    fieldnames = ['category', 'idx', 'user_name', 'points']
    writer = csv.DictWriter(response, fieldnames=fieldnames)
    writer.writeheader()

    for row in rankings_data:
        writer.writerow(row)

    return response


def ranking_view(request):
    modes = ["u18", "bj", "ue50"]
    genders = ["man", "woman"]

    rankings = {}

    for mode in modes:
        for gender in genders:
            category = f"{mode}_{gender}"
            data = get_sorted_boulder_data_based_on(category)
            rankings[category] = data

    context = {
        'rankings': rankings,
    }

    return render(request, "ranking.html", context)


@login_required
def view_boulder(request):

    cur_user_profile = UserProfile.objects.get(user=request.user)
    user_gender = cur_user_profile.gender
    user_mode = cur_user_profile.mode
    user_category = f"{user_mode}_{user_gender}"
    user_boulders = retrieve_boulders_based_on_(request.user, user_category)
    tops = retrieve_tops_amount(request.user, user_category)
    zones = retrieve_zones_amount(request.user, user_category)
    return render(request, 'view_boulder.html', {'boulders': user_boulders, 'username': request.user.username, "tops": tops, "zones": zones})


@login_required
def add_boulders_view(request):
    cur_user_profile = UserProfile.objects.get(user=request.user)
    user_gender = cur_user_profile.gender
    user_mode = cur_user_profile.mode
    user_category = f"{user_mode}_{user_gender}"

    existing_boulder = get_existing_boulder_data(request.user, user_category)
    if request.method == 'POST':
        form_name = retrieve_form_based_on_category(user_category)
        form = form_name(request.POST, instance=existing_boulder)
        if form.is_valid():
            boulder_entry = form.save(commit=False)
            boulder_entry.user = request.user
            boulder_entry.save()
            logger.info("Boulders added successfully")
            return redirect('jagd:view_boulder')
        else:
            form_name = retrieve_form_based_on_category(user_category)
            form = form_name(request.POST, instance=existing_boulder)

            logger.error("Boulders addition failed. Unsuccessful form submission")
        return render(request, "add_boulders.html", {'form': form, 'username': request.user.username})

    else:
        form_name= retrieve_form_based_on_category(user_category)
        form = form_name(instance=existing_boulder)
        return render(request, "add_boulders.html", {'form': form, "username": request.user.username})


def create_boulder_entry(user, category):
    if category == 'u18_man':
        U18M.objects.create(user=user)
    elif category == 'u18_woman':
        U18W.objects.create(user=user)
    elif category == 'ue50_man':
        UE50M.objects.create(user=user)
    elif category == 'ue50_woman':
        UE50W.objects.create(user=user)
    elif category == 'bj_man':
        BJM.objects.create(user=user)
    elif category == 'bj_woman':
        BJW.objects.create(user=user)


def retrieve_form_based_on_category(category):
    logger.info(f"Retrieving form based on category: {category}")
    category2form_mapping = {"u18_man": AddBoulderFormU18M,
                             "bj_man": AddBoulderFormBJM,
                             "ue50_woman": AddBoulderFormUE50W,
                             "bj_woman": AddBoulderFormBJW,
                             "ue50_man": AddBoulderFormUE50M,
                             "u18_woman": AddBoulderFormU18W}
    logger.info(f"Form retrieved: {category2form_mapping[category]}")
    return category2form_mapping[category]


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        #email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Der Benutzername existiert bereits! Bitte versuchen Sie es mit einem anderen Benutzernamen.")
            return render(request, "authentication/signup.html")


        if len(username) > 20:
            messages.error(request, "Der Benutzername muss weniger als 20 Zeichen lang sein!!")
            return render(request, "authentication/signup.html")

        #if User.objects.filter(email=email).exists():
        #    messages.error(request, "E-Mail Bereits registriert!!")
        #    return render(request, "authentication/signup.html")

        if pass1 != pass2:
            messages.error(request, "Passwörter stimmen nicht überein!!")
            return render(request, "authentication/signup.html")

        if not username.isalnum():
            messages.error(request, "Der Benutzername muss alphanumerisch sein!!")
            return render(request, "authentication/signup.html")

        myuser = User.objects.create_user(username, "", pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()
        gender = request.POST.get('gender')
        mode = request.POST.get('mode')
        UserProfile.objects.create(user=myuser, gender=gender, mode=mode)
        category = f"{mode}_{gender}"
        logger.info(f"Creating boulder entry for user: {myuser} and category: {category}")
        create_boulder_entry(myuser, category)

        messages.success(request,
                         "Dein Account wurde erfolgreich erstellt!!")

        return redirect('jagd:signin')

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            username = user.username
            return render(request, 'home.html', {"username": username})
        else:
            messages.error(request, "Benutzername oder Passwort ist falsch!!")
            return redirect('jagd:signin')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    return redirect('jagd:home')
