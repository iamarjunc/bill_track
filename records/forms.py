from django import forms
from .models import BillRecord

INPUT_CLASSES = "block w-full px-4 py-3 rounded-lg border-slate-200 border focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all text-slate-700"

class BillRecordForm(forms.ModelForm):

    ADDED_BY_CHOICES = [
        ('Chandrakumar', 'Chandrakumar'),
        ('Sreelekha', 'Sreelekha'),
        ('Akku', 'Akku'),
        ('Appu', 'Appu'),
    ]

    added_by = forms.ChoiceField(
        choices=ADDED_BY_CHOICES,
        widget=forms.Select(attrs={'class': INPUT_CLASSES})
    )

    class Meta:
        model = BillRecord
        fields = [
            'customer_name',
            'bill_type',
            'start_no',
            'end_no',
            'pages',
            'books',
            'added_by'
        ]

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'bill_type': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'start_no': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'end_no': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'pages': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'books': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_no")
        end = cleaned_data.get("end_no")

        if start is not None and end is not None:
            if start >= end:
                raise forms.ValidationError("Start must be less than end.")

        return cleaned_data