from django.db import models

# Create your models here.

class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    tahun_terbit = models.IntegerField()
    kategori = models.CharField(max_length=50)
    jumlah_tersedia = models.IntegerField(default=0)
    deskripsi = models.TextField(blank=True, null=True)
    tanggal_ditambahkan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
