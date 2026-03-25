from .models import SiteAppearance
from .permissions import can_edit_theme
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.shortcuts import get_current_site


def theme_context(request):
    theme = SiteAppearance.get_solo()
    theme_tokens = theme.get_theme_tokens()
    current_site = get_current_site(request)
    google_oauth_ready = SocialApp.objects.filter(
        provider="google",
        sites=current_site,
    ).exists()
    return {
        "site_theme": theme,
        "theme_tokens": theme_tokens,
        "theme_font_stack": theme.font_family,
        "google_oauth_ready": google_oauth_ready,
        "can_edit_site": can_edit_theme(request.user),
    }
