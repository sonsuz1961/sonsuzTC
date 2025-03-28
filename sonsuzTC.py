import pyfiglet
import random
from colorama import Fore, Back, Style, init

# Renkli yazı için başlangıç
init(autoreset=True)

# RGB renk seçimi
def random_rgb_color():
    return f"\033[38;2;{random.randint(0,255)};{random.randint(0,255)};{random.randint(0,255)}m"

# Banner'ı yazdırma
def print_banner():
    banner_text = "SONSUZ TC"
    ascii_banner = pyfiglet.figlet_format(banner_text, font="slant")  # "slant" fontu kullan
    color = random_rgb_color()  # RGB karışık renk seç
    print(f"{color}{ascii_banner}")

# TC sorgulama ve diğer fonksiyonlar burada olacak...
def veri_dosyasini_oku(dosya_adi):
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as file:
            # Dosyadaki her satırdaki boşlukları temizle ve virgülle ayır
            veriler = [satir.strip().split(', ') for satir in file]
            return veriler
    except FileNotFoundError:
        print(f"{dosya_adi} dosyası bulunamadı.")
        return []

def tc_bul(tc):
    # Dosyadaki verileri al
    veriler = veri_dosyasini_oku("tcveri.txt")  # Dosya adı burada güncellendi
    bulunan_kisiler = []

    for veri in veriler:
        # Eğer veri satırı 5 elemandan oluşuyorsa işlemi yap
        if len(veri) == 5:
            dosya_tc, dosya_isim, dosya_soyisim, dosya_il, dosya_ilce = [v.strip() for v in veri]
            
            # TC numarası 11 haneli ve kullanıcı TC ile eşleşiyor mu kontrol et
            if len(dosya_tc) == 11 and dosya_tc == tc:
                bulunan_kisiler.append(veri)

    return bulunan_kisiler

def tc_sorgula():
    while True:
        # Banner'ı yazdır
        print_banner()

        # TC numarası isteği kalın yazı ile
        tc = input(f"{Style.BRIGHT}TC Numaranızı Girin (11 haneli): ").strip()

        # TC numarasının 11 haneli olup olmadığını kontrol et
        if len(tc) != 11 or not tc.isdigit():
            print(f"{Style.BRIGHT}{Fore.RED}Geçersiz TC numarası. Lütfen 11 haneli bir TC numarası girin.")
            continue

        # Eşleşen kişileri bul
        bulunan_kisiler = tc_bul(tc)

        if bulunan_kisiler:
            # Kişi bulunduğunda kalın yazı ile çıktı ver
            print(f"\n{Style.BRIGHT}Kişi bulundu:")
            for kisi in bulunan_kisiler:
                print(f"\n{Style.BRIGHT}TC: {Style.NORMAL}{kisi[0]}")         # TC
                print(f"{Style.BRIGHT}İsim: {Style.NORMAL}{kisi[1]}")         # İsim
                print(f"{Style.BRIGHT}Soyisim: {Style.NORMAL}{kisi[2]}")     # Soyisim
                print(f"{Style.BRIGHT}İl: {Style.NORMAL}{kisi[3]}")          # İl
                print(f"{Style.BRIGHT}İlçe: {Style.NORMAL}{kisi[4]}")        # İlçe
        else:
            # Kişi bulunamadığında kırmızı renkte ve kalın yazı ile çıktı ver
            print(f"{Style.BRIGHT}{Fore.RED}Kişi bulunamadı.")

        # Yeni sorgu veya çıkış seçeneğini alt alta, kalın yazıyla ver
        print(f"\n{Style.BRIGHT}Yeni sorgu (1)")
        print(f"{Style.BRIGHT}Çıkış (2)")

        secim = input("Seçiminizi yapın: ").strip()

        if secim == '2':
            print("Çıkılıyor...")
            break
        elif secim != '1':
            print("Geçersiz seçenek. Çıkılıyor...")
            break

# Banner'ı yazdırma ve sorgulamayı başlatma
tc_sorgula()
