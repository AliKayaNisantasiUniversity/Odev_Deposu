from functools import reduce


galaksi_verisi = [
    {"ad": "dünya", "baglanti_sayisi": 3},
    {"ad": "centauri", "baglanti_sayisi": 2},
    {"ad": "sirius", "baglanti_sayisi": 4},
    {"ad": "orion", "baglanti_sayisi": 2},
    {"ad": "kara_delik", "baglanti_sayisi": 1}
]


buyuk_harfler_map = list(map(lambda g: g["ad"].upper(), galaksi_verisi))


buyuk_harfler_liste = [g["ad"].upper() for g in galaksi_verisi]



en_az_iki_filter = list(map(lambda g: g["ad"], filter(lambda g: g["baglanti_sayisi"] >= 2, galaksi_verisi)))


en_az_iki_liste = [g["ad"] for g in galaksi_verisi if g["baglanti_sayisi"] >= 2]


toplam_baglanti_reduce = reduce(lambda acc, g: acc + g["baglanti_sayisi"], galaksi_verisi, 0)


toplam_baglanti_sum = sum(g["baglanti_sayisi"] for g in galaksi_verisi)



from functools import partial

def genel_yolculuk(hiz: int, mesafe: int) -> float:
    return mesafe / hiz


hizli_yolculuk = partial(genel_yolculuk, hiz=3)