from django.db import models


class GroupProfile(models.Model):
    group_name = models.CharField(max_length=150)
    class_name = models.CharField(max_length=150)
    course_name = models.CharField(max_length=150)
    members = models.TextField(help_text="Satu anggota per baris")
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.group_name


class SiteAppearance(models.Model):
    THEME_PRESETS = {
        "midnight": {
            "primary": "#38bdf8",
            "secondary": "#1e293b",
            "bg": "#0b1120",
            "paper": "#111827",
            "paper_2": "#1f2937",
            "ink": "#e2e8f0",
            "ink_soft": "#cbd5e1",
            "muted": "#94a3b8",
            "line": "#334155",
            "hero_a": "#172554",
            "hero_b": "#1e293b",
        },
        "sunrise": {
            "primary": "#f97316",
            "secondary": "#fff7ed",
            "bg": "#fffaf3",
            "paper": "#ffffff",
            "paper_2": "#ffedd5",
            "ink": "#2c1b12",
            "ink_soft": "#5b3b2a",
            "muted": "#7c5a43",
            "line": "#f5cba7",
            "hero_a": "#fed7aa",
            "hero_b": "#ffedd5",
        },
        "forest": {
            "primary": "#22c55e",
            "secondary": "#ecfdf5",
            "bg": "#f2fbf6",
            "paper": "#ffffff",
            "paper_2": "#dcfce7",
            "ink": "#10281a",
            "ink_soft": "#1d3b28",
            "muted": "#3d6a52",
            "line": "#b7ebc8",
            "hero_a": "#bbf7d0",
            "hero_b": "#dcfce7",
        },
        "royal": {
            "primary": "#8b5cf6",
            "secondary": "#eef2ff",
            "bg": "#f4f4ff",
            "paper": "#ffffff",
            "paper_2": "#e9e7ff",
            "ink": "#1f1b3a",
            "ink_soft": "#352f59",
            "muted": "#5b5584",
            "line": "#c7c2ff",
            "hero_a": "#ddd6fe",
            "hero_b": "#ede9fe",
        },
        "mono": {
            "primary": "#334155",
            "secondary": "#f8fafc",
            "bg": "#f8fafc",
            "paper": "#ffffff",
            "paper_2": "#f1f5f9",
            "ink": "#0f172a",
            "ink_soft": "#334155",
            "muted": "#64748b",
            "line": "#d5dde8",
            "hero_a": "#e2e8f0",
            "hero_b": "#f1f5f9",
        },
    }

    THEME_CHOICES = [
        ("midnight", "Midnight Tech"),
        ("sunrise", "Sunrise Clay"),
        ("forest", "Forest Mist"),
        ("royal", "Royal Violet"),
        ("mono", "Monochrome Clean"),
    ]

    FONT_CHOICES = [
        ("Manrope, sans-serif", "Manrope"),
        ("Poppins, sans-serif", "Poppins"),
        ("'Nunito Sans', sans-serif", "Nunito Sans"),
        ("'Space Grotesk', sans-serif", "Space Grotesk"),
        ("Merriweather, serif", "Merriweather"),
        ("Arial, sans-serif", "Arial"),
        ("'Courier New', monospace", "Courier New"),
        ("Georgia, serif", "Georgia"),
        ("'Trebuchet MS', sans-serif", "Trebuchet MS"),
        ("Verdana, sans-serif", "Verdana"),
    ]

    name = models.CharField(max_length=50, default="default", unique=True)
    theme_preset = models.CharField(max_length=30, choices=THEME_CHOICES, default="midnight")
    primary_color = models.CharField(max_length=7, default="#0f766e")
    secondary_color = models.CharField(max_length=7, default="#f1f5f9")
    font_family = models.CharField(max_length=50, choices=FONT_CHOICES, default="Manrope, sans-serif")
    updated_by = models.CharField(max_length=150, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Tema {self.name}"

    def get_theme_tokens(self) -> dict[str, str]:
        return dict(self.THEME_PRESETS.get(self.theme_preset, self.THEME_PRESETS["midnight"]))

    def save(self, *args, **kwargs):
        active_theme = self.get_theme_tokens()
        self.primary_color = active_theme["primary"]
        self.secondary_color = active_theme["secondary"]
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls) -> "SiteAppearance":
        obj, _ = cls.objects.get_or_create(name="default")
        return obj
