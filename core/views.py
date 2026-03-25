import re

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ThemeForm
from .models import GroupProfile, SiteAppearance
from .permissions import can_edit_theme, group_member_required


DEFAULT_MEMBERS = [
    "Mohammad Aly Haidarulloh (2406425804)",
    "M Naufal Zhafran Rabiul Batara (2406361694)",
    "Alvino Revaldi (2406438933)",
    "Haikal Muzaki (2406407360)",
    "Dion Wisdom Pasaribu (2406414536)",
]


def _member_cards(raw_members: str):
    cards = []
    for line in raw_members.splitlines():
        row = line.strip()
        if not row:
            continue
        match = re.match(r"^(.*?)\s*\((\d+)\)\s*$", row)
        if match:
            cards.append({"name": match.group(1).strip(), "npm": match.group(2).strip()})
        else:
            cards.append({"name": row, "npm": ""})
    return cards


def _google_oauth_ready(request):
    current_site = get_current_site(request)
    return SocialApp.objects.filter(provider="google", sites=current_site).exists()


def home(request):
    profile = GroupProfile.objects.first()
    if not profile:
        profile = GroupProfile.objects.create(
            group_name="Tim Bjorka",
            class_name="TK-2",
            course_name="PKPL",
            members="\n".join(DEFAULT_MEMBERS),
            description="Website biodata kelompok dengan autentikasi OAuth Google.",
        )
    elif "Nama Anggota 1" in profile.members:
        profile.members = "\n".join(DEFAULT_MEMBERS)
        profile.save(update_fields=["members", "updated_at"])

    context = {
        "profile": profile,
        "member_cards": _member_cards(profile.members),
        "can_edit": can_edit_theme(request.user),
    }
    return render(request, "core/home.html", context)


def quick_login(request):
    if _google_oauth_ready(request):
        return redirect("/accounts/google/login/?process=login")
    return render(request, "account/login.html")


@login_required
@group_member_required
def edit_theme(request):
    theme = SiteAppearance.get_solo()

    if request.method == "POST":
        form = ThemeForm(request.POST, instance=theme)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.updated_by = request.user.email
            obj.save()
            messages.success(request, "Tema website berhasil diperbarui.")
            return redirect("home")
    else:
        form = ThemeForm(instance=theme)

    return render(request, "core/edit_theme.html", {"form": form})
