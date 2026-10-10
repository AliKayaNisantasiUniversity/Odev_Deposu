from uzay_oyunu.oyun import yakit_ekle


def test_yakit_ekle_tuzagi():
    # Fonksiyonu ilk kez çağırıyoruz
    ilk_sonuc = yakit_ekle(50)
    assert ilk_sonuc == [50]

    # İkinci kez çağırıyoruz (eğer tuzak varsa bu liste [50, 50] olur ve test patlar)
    ikinci_sonuc = yakit_ekle(30)
    assert ikinci_sonuc == [30]