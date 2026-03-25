from django import forms

from .models import SiteAppearance


class ThemeForm(forms.ModelForm):
    class Meta:
        model = SiteAppearance
        fields = ["theme_preset", "font_family"]
