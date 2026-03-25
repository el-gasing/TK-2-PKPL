from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        email = (data.get("email") or user.email or "").strip().lower()

        if email and not user.email:
            user.email = email

        if not getattr(user, "username", ""):
            user.username = self._build_unique_username(email)

        return user

    def _build_unique_username(self, email: str) -> str:
        UserModel = get_user_model()
        username_field = UserModel._meta.get_field("username")
        max_length = username_field.max_length or 150

        base = "user"
        if email:
            local_part = email.split("@", 1)[0]
            cleaned = "".join(ch for ch in local_part.lower() if ch.isalnum() or ch == "_")
            if cleaned:
                base = cleaned

        base = base[:max_length]
        candidate = base
        suffix = 1

        while UserModel.objects.filter(username=candidate).exists():
            suffix_text = str(suffix)
            candidate = f"{base[: max_length - len(suffix_text)]}{suffix_text}"
            suffix += 1

        return candidate
