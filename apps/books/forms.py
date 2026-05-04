from django import forms
from .models import Buku

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ['judul', 'penulis', 'isbn', 'tahun_terbit', 'kategori', 'jumlah_tersedia', 'deskripsi']