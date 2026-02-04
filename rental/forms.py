from django import forms

class CarForm(forms.Form):
    brand = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}))
    model = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Model'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year'}))

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}))

class RentForm(forms.Form):
    def __init__(self, customers, available_cars, *args, **kwargs):
        super(RentForm, self).__init__(*args, **kwargs)
        self.fields['customer'] = forms.ChoiceField(
            choices=[(c.name, c.name) for c in customers],
            widget=forms.Select(attrs={'class': 'form-select'})
        )
        self.fields['car'] = forms.ChoiceField(
            choices=[(c.car_id, f"{c.brand} {c.model} ({c.year})") for c in available_cars],
            widget=forms.Select(attrs={'class': 'form-select'})
        )
