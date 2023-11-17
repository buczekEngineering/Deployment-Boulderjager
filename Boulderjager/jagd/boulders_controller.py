from jagd.forms import AddBoulderFormBJW, AddBoulderFormBJM
from jagd.models import U18W, U18M, UE50W, UE50M, BJW, BJM, UserProfile


def get_sorted_boulder_data_based_on(category):
    model_name = category2boulder_model__mapping(category)
    sorted_data = model_name.objects.all().order_by('-points')
    return sorted_data


def get_existing_boulder_data(user, category):
    model_name = category2boulder_model__mapping(category)
    try:
        # Attempt to get the user's existing boulder, if it exists
        existing_boulder = model_name.objects.get(user=user)
    except model_name.DoesNotExist:
        existing_boulder = None
    return existing_boulder


def retrieve_boulders_based_on_(user, category):
    model_name = category2boulder_model__mapping(category)
    boulder_entry = model_name.objects.filter(user=user)

    return boulder_entry

def retrieve_tops_amount(user, category):
    model_name = category2boulder_model__mapping(category)
    tops_amount = model_name.objects.get(user=user).tops_amount
    return tops_amount

def retrieve_zones_amount(user, category):
    model_name = category2boulder_model__mapping(category)
    zones_amount = model_name.objects.get(user=user).bonus_amount
    return zones_amount


def category2boulder_model_name__mapping(category: str):
    if category == "u18_woman":
        return "U18W"
    elif category == "u18_man":
        return "U18M"
    elif category == "ue50_woman":
        return "UE50W"
    elif category == "ue50_man":
        return "UE50M"
    elif category == "bj_woman":
        return "BJW"
    elif category == "bj_man":
        return "BJM"
    else:
        raise ValueError(f"Unknown category: {category}")

def category2boulder_model__mapping(category: str):
    if category == "u18_woman":
        return U18W
    elif category == "u18_man":
        return U18M
    elif category == "ue50_woman":
        return UE50W
    elif category == "ue50_man":
        return UE50M
    elif category == "bj_woman":
        return BJW
    elif category == "bj_man":
        return BJM
    else:
        raise ValueError(f"Unknown category: {category}")