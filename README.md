# Ariza topshirish va ko‘rib chiqish tizimi

Ushbu loyiha orqali foydalanuvchilar web-sayt orqali ariza yuborishi, adminlar esa arizalarni ko‘rishi, PDF yuklab olishi va boshqarishi mumkin.

## Asosiy imkoniyatlar
- Foydalanuvchi ariza yuboradi (ism, familiya, otasining ismi, manzil, telefon, yo‘nalish, passport va selfi rasm)
- Arizalar bazaga saqlanadi
- Admin panel orqali barcha arizalar ko‘rinadi
- Har bir arizani PDF ko‘rinishida yuklab olish mumkin
- Arizani holatini (qabul qilingan, bekor qilingan, ko‘rib chiqilmoqda) boshqarish
- Adminlar ro‘yxati va yangi admin qo‘shish
- Avto-logout va chiroyli 404 sahifa

## Texnologiyalar
- Backend: Django (Python)
- Frontend: Django Template Engine (HTML, CSS, Bootstrap)
- Database: Django ORM (SQLite by default)
- Fayl yuklash: Django FileField va ImageField
- PDF generatsiya: xhtml2pdf

## O‘rnatish va ishga tushirish

1. **Klonlash va virtual environment yaratish:**
   ```bash
   git clone <repo-url>
   cd <repo-nomi>
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Kerakli kutubxonalarni o‘rnatish:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Migratsiyalarni bajarish:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Superuser (admin) yaratish:**
   ```bash
   python manage.py createsuperuser
   ```
5. **Serverni ishga tushirish:**
   ```bash
   python manage.py runserver
   ```
6. **Admin panel:**
   - `/admin-login/` orqali kirish
   - Dashboard: `/dashboard/`

## Muhim fayllar
- `ariza/models.py` — asosiy ma’lumotlar modeli
- `ariza/forms.py` — formalar va validatsiya
- `ariza/views.py` — barcha viewlar va logika
- `ariza/templates/` — barcha HTML shablonlar

## Litsenziya
MIT 