import os

from allauth.socialaccount.models import SocialApp
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Setup/update Google OAuth SocialApp dari environment variables"

    def handle(self, *args, **options):
        client_id = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
        secret = os.getenv("GOOGLE_OAUTH_SECRET")
        site_domain = os.getenv("GOOGLE_OAUTH_SITE_DOMAIN", "127.0.0.1:8000")
        site_name = os.getenv("GOOGLE_OAUTH_SITE_NAME", "Tim Bjorka")

        if not client_id or not secret:
            raise CommandError("GOOGLE_OAUTH_CLIENT_ID dan GOOGLE_OAUTH_SECRET wajib diisi di environment/.env")

        site, _ = Site.objects.update_or_create(
            id=settings.SITE_ID,
            defaults={"domain": site_domain, "name": site_name},
        )

        social_app = SocialApp.objects.filter(provider="google").first()
        if social_app is None:
            social_app = SocialApp.objects.create(
                provider="google",
                name="Google OAuth",
                client_id=client_id,
                secret=secret,
                key="",
            )
        else:
            social_app.name = "Google OAuth"
            social_app.client_id = client_id
            social_app.secret = secret
            social_app.key = ""
            social_app.save()

        social_app.sites.set([site])

        self.stdout.write(self.style.SUCCESS("Google OAuth berhasil dikonfigurasi."))
        self.stdout.write(f"Site: {site.domain}")
        self.stdout.write(f"SocialApp ID: {social_app.id}")
