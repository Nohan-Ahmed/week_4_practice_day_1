from django import forms
import datetime

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
SIZE = [
    ('Small', 'S'),
    ('Meadum', 'M'),
    ('Large', 'L'),
]
FAVORITE_FRUITS_CHOICES = [
    ('Mango', 'Mango'),
    ('Watermelon', 'Watermelon'),
    ('Orange', 'Orange'),
    ('Apple', 'Apple'),
    ('Goava', 'Goava'),
]
EDUCATION = [
    ('PSC', 'PSC'),
    ('JSC', 'JSC'),
    ('SSC', 'SSC'),
    ('HSC', 'HSC'),
]

class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=10,
        label="Your full name",
    )
    email = forms.EmailField()
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}),
                           required=False,
                           initial=datetime.date.today)
    birth_year = forms.DateField(widget=forms.SelectDateWidget())
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_fruits = forms.MultipleChoiceField(choices=FAVORITE_FRUITS_CHOICES)
    size = forms.ChoiceField(choices=SIZE, widget=forms.RadioSelect)
    education = forms.ChoiceField(choices=EDUCATION, widget=forms.CheckboxSelectMultiple)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}),
                              initial='Thanks for contact us')
    agree = forms.BooleanField(initial=False, required=True)
