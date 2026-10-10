def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler) -> None:
    """
    Görev başlığını, adımları ve ek bilgileri istenen formatta ekrana yazdırır.
    """
    # Önceliği büyük harfe çevirip başlıkla beraber yazdırıyoruz
    print(f"[{oncelik.upper()}] {baslik}")

    # Adımları 1'den başlayarak numaralandırıp yazdırıyoruz
    for i, adim in enumerate(adimlar, 1):
        print(f"{i}. {adim}")

    # Ekstra gelen anahtar-değer çiftlerini yazdırıyoruz (örn: sorumlu: Ayşe)
    for anahtar, deger in ekler.items():
        print(f"{anahtar}: {deger}")


if __name__ == "__main__":
    # 1. Doğrudan çağrı biçimi
    print("--- Doğrudan Çağrı ---")
    gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Ayşe"
    )

    # 2. Liste ve sözlüğü açarak (*) ve (**) ile çağrı biçimi
    print("\n--- Unpacking (Açarak) Çağrı ---")
    liste_adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    sozluk_ekler = {"sorumlu": "Ayşe"}

    gorev_kaydi(
        "Kara deliğe atla",
        *liste_adimlar,
        oncelik="yüksek",
        **sozluk_ekler
    )