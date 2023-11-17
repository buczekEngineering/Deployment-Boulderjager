from django import forms

from jagd.models import BJM, BJW, U18M, U18W, UE50M, UE50W


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class AddBoulderFormU18M(forms.ModelForm):
    class Meta:
        model = U18M
        fields = [f'boulder_{i}' for i in range(1, 26)]

    def __init__(self, *args, **kwargs):
        CHOICES = [
            ('None', 'None'),
            ('Bonus', 'Bonus'),
            ('Top', 'Top'),
        ]

        super(AddBoulderFormU18M, self).__init__(*args, **kwargs)


        for i in range(1, 26):
            field_name = f'boulder_{i}'
            self.fields[field_name] = forms.ChoiceField(
                choices=CHOICES,
                initial='None',
                widget=forms.Select(attrs={'class': 'form-control'})
            )

class AddBoulderFormU18W(forms.ModelForm):
    class Meta:
        model = U18W
        fields = [f'boulder_{i}' for i in range(1, 26)]

    def __init__(self, *args, **kwargs):
        CHOICES = [
            ('None', 'None'),
            ('Bonus', 'Bonus'),
            ('Top', 'Top'),
        ]

        super(AddBoulderFormU18W, self).__init__(*args, **kwargs)


        for i in range(1, 26):
            field_name = f'boulder_{i}'
            self.fields[field_name] = forms.ChoiceField(
                choices=CHOICES,
                initial='None',
                widget=forms.Select(attrs={'class': 'form-control'})
            )



class AddBoulderFormUE50M(forms.ModelForm):
    class Meta:
        model = UE50M
        fields = [f'boulder_{i}' for i in range(1, 26)]

    def __init__(self, *args, **kwargs):
        CHOICES = [
            ('None', 'None'),
            ('Bonus', 'Bonus'),
            ('Top', 'Top'),
        ]

        super(AddBoulderFormUE50M, self).__init__(*args, **kwargs)


        for i in range(1, 26):
            field_name = f'boulder_{i}'
            self.fields[field_name] = forms.ChoiceField(
                choices=CHOICES,
                initial='None',
                widget=forms.Select(attrs={'class': 'form-control'})
            )

class AddBoulderFormUE50W(forms.ModelForm):
    class Meta:
        model = UE50W
        fields = [f'boulder_{i}' for i in range(1, 26)]

    def __init__(self, *args, **kwargs):
        CHOICES = [
            ('None', 'None'),
            ('Bonus', 'Bonus'),
            ('Top', 'Top'),
        ]

        super(AddBoulderFormUE50W, self).__init__(*args, **kwargs)


        for i in range(1, 26):
            field_name = f'boulder_{i}'
            self.fields[field_name] = forms.ChoiceField(
                choices=CHOICES,
                initial='None',
                widget=forms.Select(attrs={'class': 'form-control'})
            )
class AddBoulderFormBJM(forms.ModelForm):
    class Meta:
        model = BJM
        fields = [f'boulder_{i}' for i in range(5, 31)]

    def __init__(self, *args, **kwargs):

        CHOICES = [
            ('None', 'None'),
            ('Bonus', 'Bonus'),
            ('Top', 'Top'),
        ]

        super(AddBoulderFormBJM, self).__init__(*args, **kwargs)

        for i in range(5, 31):
            field_name = f'boulder_{i}'
            self.fields[field_name] = forms.ChoiceField(
                choices=CHOICES,
                initial='None',
                widget=forms.Select(attrs={'class': 'form-control'})
            )

class AddBoulderFormBJW(forms.ModelForm):
    class Meta:
        model = BJW
        fields = [f'boulder_{i}' for i in range(3, 29)]

    def __init__(self, *args, **kwargs):

        CHOICES = [
            ('None', 'None'),
            ('Bonus', 'Bonus'),
            ('Top', 'Top'),
        ]

        super(AddBoulderFormBJW, self).__init__(*args, **kwargs)

        for i in range(3, 29):
            field_name = f'boulder_{i}'
            self.fields[field_name] = forms.ChoiceField(
                choices=CHOICES,
                initial='None',
                widget=forms.Select(attrs={'class': 'form-control'})
            )