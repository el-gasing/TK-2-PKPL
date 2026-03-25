# Website Biodata Kelompok Tim Bjorka (Django)

Website ini memenuhi kebutuhan tugas:
- Biodata kelompok bisa dilihat tanpa login.
- Login menggunakan OAuth Google.
- Hanya akun anggota kelompok yang login via Google yang bisa mengubah tema (warna/font).

## 1. Jalankan Proyek

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 2. Konfigurasi OAuth Google

1. Buka [Google Cloud Console](https://console.cloud.google.com/)
2. Buat OAuth Client ID (Web application).
3. Tambahkan redirect URI:
   - `http://127.0.0.1:8000/accounts/google/login/callback/`
4. Isi `.env`:
   - `GOOGLE_OAUTH_CLIENT_ID`
   - `GOOGLE_OAUTH_SECRET`
5. Jalankan:

```bash
python manage.py setup_google_oauth
```

## 3. Authorization Anggota

Daftar email anggota diatur lewat env:

```env
GROUP_MEMBER_EMAILS=anggota1@gmail.com,anggota2@gmail.com,anggota3@gmail.com
```

Akun harus memenuhi dua syarat untuk mengubah tema:
- Sudah login
- Login melalui provider Google dan email ada di daftar anggota

## 4. Struktur Fitur

- `/` halaman biodata publik
- `/accounts/login/` login Google
- `/tema/` form pilih preset tema + font global (hanya anggota yang berhak)
