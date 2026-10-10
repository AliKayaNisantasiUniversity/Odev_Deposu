import time
from functools import wraps


def hamle_sayaci():
    """
    Closure kullanarak her çağrıldığında 1 artan bir sayaç fonksiyonu döndürür.
    nonlocal anahtar kelimesi ile dış değişkene erişilir.
    """
    sayac = 0

    def say():
        nonlocal sayac
        sayac += 1
        return sayac

    return say


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """
    Gezegenleri bağlantı (komşu) sayılarına göre azalan,
    eşitlik durumunda ise alfabetik (artan) sırayla döndürür.
    sorted() ve lambda kullanılır.
    """
    baglantilar = galaksi.get("baglantilar", {})

    # Gezegenleri sıralıyoruz:
    # 1. Kriter (-len(komşular)): Bağlantı sayısına göre azalan sırada (eksi işareti büyükten küçüğe sıralatır)
    # 2. Kriter (gezegen_adi): Eşitlik durumunda alfabetik sırada
    sirali_gezegenler = sorted(
        baglantilar.keys(),
        key=lambda gezegen: (-len(baglantilar[gezegen]), gezegen)
    )
    return sirali_gezegenler


# --- BONUS (+10 Puan) ---
def sure_olc(fonk):
    """
    Verilen bir fonksiyonun çalışma süresini ölçen bir sarmalayıcı (decorator) döndürür.
    """

    @wraps(fonk)
    def sarmalayici(*args, **kwargs):
        baslangic_zamani = time.time()
        sonuc = fonk(*args, **kwargs)
        bitis_zamani = time.time()
        sure = bitis_zamani - baslangic_zamani
        print(f"[{fonk.__name__}] Çalışma Süresi: {sure:.6f} saniye")
        return sonuc

    return sarmalayici

# Bonus'u en_bagli_gezegenler fonksiyonu üzerinde test etme örneği:
# en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)