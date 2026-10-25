from itertools import islice
import time
from uzay_oyunu.akis import (
    fibonacci,
    yakit_gostergesi,
    satirlari_oku,
    ayristir,
    uzun_yolculuklar,
    rota_sayaci
)


def test_rota_sayaci_performans():
    ornek_baglantilar = {
        "dünya": ["sirius", "orion"],
        "sirius": ["orion", "kara_delik"],
        "orion": ["centauri", "sirius"],
        "centauri": ["orion"],
        "kara_delik": []
    }

    sayici = rota_sayaci(ornek_baglantilar)

    baslangic = time.perf_counter()
    sonuc = sayici("dünya", 5)
    bitis = time.perf_counter()

    assert sonuc > 0

def test_veri_boru_hatti():
    dosya_yolu = "veri/seyir.txt"
    kayitlar = ayristir(satirlari_oku(dosya_yolu))

    toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku(dosya_yolu)))
    assert toplam_yakit == 88

    uzunlar = list(uzun_yolculuklar(ayristir(satirlari_oku(dosya_yolu)), 10))
    assert uzunlar == ["sirius", "centauri", "orion", "kara_delik"]

def test_yakit_gostergesi():
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]

def test_fibonacci():
    g = fibonacci()
    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 1
    assert list(islice(fibonacci(), 12)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    tekrar_g = fibonacci()
    ilk_tur = list(islice(tekrar_g, 5))
    ikinci_tur = list(islice(tekrar_g, 3))
    assert ikinci_tur == [5, 8, 13]