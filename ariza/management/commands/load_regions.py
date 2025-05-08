from django.core.management.base import BaseCommand
from ariza.models import Viloyat, Tuman

class Command(BaseCommand):
    help = 'O\'zbekiston viloyatlari, shaharlari va tumanlarini yuklash'

    def handle(self, *args, **kwargs):
        # Viloyatlar, shaharlar va tumanlar ma'lumotlari
        regions = {
            'Andijon viloyati': {
                'shaharlar': ['Andijon shahri', 'Xonabod shahri', 'Asaka shahri'],
                'tumanlar': [
                    'Andijon tumani', 'Asaka tumani', 'Baliqchi tumani', 'Bo\'z tumani',
                    'Buloqboshi tumani', 'Izboskan tumani', 'Jalaquduq tumani', 'Marhamat tumani',
                    'Oltinko\'l tumani', 'Paxtaobod tumani', 'Qo\'rg\'ontepa tumani', 'Shahrixon tumani',
                    'Ulug\'nor tumani', 'Xo\'jaobod tumani'
                ]
            },
            'Buxoro viloyati': {
                'shaharlar': ['Buxoro shahri', 'Kogon shahri'],
                'tumanlar': [
                    'Buxoro tumani', 'G\'ijduvon tumani', 'Jondor tumani', 'Kogon tumani',
                    'Olot tumani', 'Peshku tumani', 'Qorovulbozor tumani', 'Qo\'g\'ay tumani',
                    'Romitan tumani', 'Shofirkon tumani'
                ]
            },
            'Farg\'ona viloyati': {
                'shaharlar': ['Farg\'ona shahri', 'Marg\'ilon shahri', 'Qo\'qon shahri'],
                'tumanlar': [
                    'Oltiariq tumani', 'Beshariq tumani', 'Bog\'dod tumani', 'Buvayda tumani',
                    'Dang\'ara tumani', 'Farg\'ona tumani', 'Furqat tumani', 'Qo\'shtepa tumani',
                    'Quva tumani', 'Rishton tumani', 'So\'x tumani', 'Toshloq tumani',
                    'Uchko\'prik tumani', 'Yozyovon tumani'
                ]
            },
            'Jizzax viloyati': {
                'shaharlar': ['Jizzax shahri'],
                'tumanlar': [
                    'Arnasoy tumani', 'Baxmal tumani', 'Do\'stlik tumani', 'Forish tumani',
                    'G\'allaorol tumani', 'Jizzax tumani', 'Mirzacho\'l tumani', 'Paxtakor tumani',
                    'Yangiobod tumani', 'Zomin tumani', 'Zafarobod tumani'
                ]
            },
            'Namangan viloyati': {
                'shaharlar': ['Namangan shahri', 'Kosonsoy shahri'],
                'tumanlar': [
                    'Chortoq tumani', 'Kosonsoy tumani', 'Mingbuloq tumani', 'Namangan tumani',
                    'Norin tumani', 'Pop tumani', 'To\'raqo\'rg\'on tumani', 'Uchqo\'rg\'on tumani',
                    'Uchqo\'rg\'on tumani', 'Yangiqo\'rg\'on tumani'
                ]
            },
            'Navoiy viloyati': {
                'shaharlar': ['Navoiy shahri', 'Zarafshon shahri'],
                'tumanlar': [
                    'Konimex tumani', 'Karmana tumani', 'Qiziltepa tumani', 'Xatirchi tumani',
                    'Navbahor tumani', 'Nurota tumani', 'Tomdi tumani', 'Uchquduq tumani'
                ]
            },
            'Qashqadaryo viloyati': {
                'shaharlar': ['Qarshi shahri', 'Shahrisabz shahri'],
                'tumanlar': [
                    'Chiroqchi tumani', 'Dehqonobod tumani', 'G\'uzor tumani', 'Qamashi tumani',
                    'Qarshi tumani', 'Koson tumani', 'Kasbi tumani', 'Kitob tumani',
                    'Mirishkor tumani', 'Muborak tumani', 'Nishon tumani', 'Shahrisabz tumani',
                    'Yakkabog\' tumani'
                ]
            },
            'Samarqand viloyati': {
                'shaharlar': ['Samarqand shahri', 'Kattaqo\'rg\'on shahri'],
                'tumanlar': [
                    'Bulung\'ur tumani', 'Ishtixon tumani', 'Jomboy tumani', 'Kattaqo\'rg\'on tumani',
                    'Qo\'shrabot tumani', 'Narpay tumani', 'Nurobod tumani', 'Oqdaryo tumani',
                    'Pastdarg\'om tumani', 'Paxtachi tumani', 'Payariq tumani', 'Samarqand tumani',
                    'Toyloq tumani', 'Urgut tumani'
                ]
            },
            'Sirdaryo viloyati': {
                'shaharlar': ['Guliston shahri', 'Sirdaryo shahri'],
                'tumanlar': [
                    'Boyovut tumani', 'Guliston tumani', 'Xovos tumani', 'Mirzaobod tumani',
                    'Oqoltin tumani', 'Sayxunobod tumani', 'Sardoba tumani', 'Sirdaryo tumani'
                ]
            },
            'Surxondaryo viloyati': {
                'shaharlar': ['Termiz shahri'],
                'tumanlar': [
                    'Angor tumani', 'Bandixon tumani', 'Boysun tumani', 'Denov tumani',
                    'Jarqo\'rg\'on tumani', 'Qiziriq tumani', 'Qumqo\'rg\'on tumani', 'Muzrabot tumani',
                    'Oltinsoy tumani', 'Sariosiyo tumani', 'Sherobod tumani', 'Sho\'rchi tumani',
                    'Termiz tumani', 'Uzun tumani'
                ]
            },
            'Toshkent viloyati': {
                'shaharlar': ['Nurafshon shahri', 'Olmaliq shahri', 'Angren shahri', 'Bekobod shahri', 'Chirchiq shahri', 'O\'rta Chirchiq shahri', 'Yangiyo\'l shahri'],
                'tumanlar': [
                    'Bekobod tumani', 'Bo\'stonliq tumani', 'Zangiota tumani', 'Qibray tumani',
                    'Quyichirchiq tumani', 'Oqqo\'rg\'on tumani', 'Ohangaron tumani', 'Parkent tumani',
                    'Piskent tumani', 'Toshkent tumani', 'Chinoz tumani', 'Yuqorichirchiq tumani',
                    'Yangiyo\'l tumani'
                ]
            },
            'Xorazm viloyati': {
                'shaharlar': ['Urganch shahri', 'Xiva shahri'],
                'tumanlar': [
                    'Bog\'ot tumani', 'Gurlan tumani', 'Qo\'shko\'pir tumani', 'Urganch tumani',
                    'Xiva tumani', 'Xonqa tumani', 'Yangiariq tumani', 'Yangibozor tumani',
                    'Shovot tumani', 'Hazorasp tumani'
                ]
            },
            'Qoraqalpog\'iston Respublikasi': {
                'shaharlar': ['Nukus shahri'],
                'tumanlar': [
                    'Amudaryo tumani', 'Beruniy tumani', 'Chimboy tumani', 'Ellikqal\'a tumani',
                    'Kegayli tumani', 'Mo\'ynoq tumani', 'Nukus tumani', 'Qanliko\'l tumani',
                    'Qo\'ng\'irot tumani', 'Qorao\'zak tumani', 'Shumanay tumani', 'Taxtako\'pir tumani',
                    'To\'rtko\'l tumani', 'Xo\'jayli tumani'
                ]
            }
        }

        # Mavjud ma'lumotlarni tozalash
        Viloyat.objects.all().delete()
        Tuman.objects.all().delete()

        # Viloyatlar, shaharlar va tumanlarni yuklash
        for viloyat_nomi, data in regions.items():
            viloyat = Viloyat.objects.create(nomi=viloyat_nomi)
            
            # Shaharlarni yuklash
            for shahar_nomi in data['shaharlar']:
                Tuman.objects.create(nomi=shahar_nomi, viloyat=viloyat)
            
            # Tumanlarni yuklash
            for tuman_nomi in data['tumanlar']:
                Tuman.objects.create(nomi=tuman_nomi, viloyat=viloyat)
                
            self.stdout.write(self.style.SUCCESS(f'{viloyat_nomi} va uning shaharlari, tumanlari muvaffaqiyatli yuklandi'))

        self.stdout.write(self.style.SUCCESS('Barcha viloyatlar, shaharlar va tumanlar muvaffaqiyatli yuklandi')) 