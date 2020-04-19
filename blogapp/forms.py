from django import forms

# iterable
CHOICES = (
        (11, 'Credit Card'),
        (12, 'Student Loans'),
        (13, 'Taxes'),
        (21, 'Books'),
        (22, 'Games'),
        (31, 'Groceries'),
        (32, 'Restaurants'),
    )


# creating a form
class GeeksForm(forms.Form):
    geeks_field = forms.ChoiceField(choices=CHOICES)