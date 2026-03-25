from functools import wraps

from allauth.socialaccount.models import SocialAccount
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect


def can_edit_theme(user) -> bool:
    if not user.is_authenticated:
        return False

    email = (user.email or "").lower()
    is_group_member = email in settings.GROUP_MEMBER_EMAILS
    has_google_login = SocialAccount.objects.filter(user=user, provider="google").exists()
    return is_group_member and has_google_login


def group_member_required(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if can_edit_theme(request.user):
            return view_func(request, *args, **kwargs)
        messages.error(request, "Hanya anggota kelompok yang login via Google yang bisa mengubah tampilan.")
        return redirect("home")

    return _wrapped
