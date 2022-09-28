from django import forms


class SectorForm(forms.ModelForm):
    class Meta:
        fields = [
            'name'
        ]