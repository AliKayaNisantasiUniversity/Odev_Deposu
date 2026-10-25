from typing import Generator
from itertools import islice
from typing import Iterator, Tuple
from functools import lru_cache
from uzay_oyunu.dekoratorler import sinirla

import time
def aralik(sure: int, adim: int) -> Generator[float, None, None]:
    """Belirtilen süre boyunca adım aralıklarıyla zaman üreten üreteç."""
    baslangic = time.time()
    while time.time() - baslangic < sure:
        yield time.time() - baslangic
        time.sleep(adim)


def rota_sayaci(baglantilar: dict):
    """Verilen bağlantılara göre lru_cache ile optimize edilmiş rota sayacı döndürür."""

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1
        if gezegen not in baglantilar:
            return 0

        toplam = 0
        for komsu in baglantilar[gezegen]:
            toplam += rota_sayisi(komsu, adim - 1)
        return toplam

    return rota_sayisi
def satirlari_oku(yol: str) -> Iterator[str]:
    """Boş ve # ile başlayan satırları atlayarak dosyadan satır okur."""
    with open(yol, "r", encoding="utf-8") as f:
        for satir in f:
            satir = satir.strip()
            if satir and not satir.startswith("#"):
                yield satir

def ayristir(satirlar: Iterator[str]) -> Iterator[Tuple[str, str, int]]:
    """Satırları (kaynak, hedef, yakit) demetine dönüştürür."""
    for satir in satirlar:
        sol, sag = satir.split("->")
        kaynak = sol.strip()
        hedef_parca = sag.strip().split()
        hedef = hedef_parca[0]
        yakit = int(hedef_parca[1])
        yield (kaynak, hedef, yakit)

def uzun_yolculuklar(kayitlar: Iterator[Tuple[str, str, int]], esik: int) -> Iterator[str]:
    """Yakıtı eşikten büyük olan kayıtların hedeflerini süzer."""
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield hedef

def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """Yolculuk simülasyonu ve yakıt kontrolü."""
    while yakit > 0:
        yakit -= tuketim
        if yakit < 0:
            yakit = 0
        yield yakit


def travel(baslangic_yakiti: int, tuketim: int) -> None:
    """Yolculuk simülasyonu ve yakıt kontrolü."""
    gosterge = yakit_gostergesi(baslangic_yakiti, tuketim)
    try:
        while True:
            kalan = next(gosterge)
            print(f"Kalan yakıt: {kalan}")
    except StopIteration:
        print("Yakıtın bitti, uzayda sürükleniyorsun...")

@sinirla(0, 100)
def yakit_harca(miktar: int) -> int:
    """Yakıt harcama simülasyonu."""
    kalan = 100 - miktar
    return kalan