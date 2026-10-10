import json

def yakit_ekle(miktar: int, depo: list | None = None) -> list:
    """
    Varsayılan mutable argüman tuzağını (None kalıbı) önleyerek yakıt ekler.
    """
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo

def galaksi_kur(gezegenler: list[str], baglantilar: dict, baslangic: str, **kwargs) -> dict:
    """
    Verilen gezegen ve bağlantı bilgilerine göre oyun galaksi sözlüğünü kurar.
    """
    # Başlangıç gezegeni gezegenler listesinde yoksa hata fırlatıyoruz
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde bulunmuyor!")

    # Yakıt verilmemişse kwargs.get ile varsayılan 50 değerini alıyoruz
    yakit = kwargs.get("yakit", 50)

    # Kurulan galaksi sözlüğünü döndürüyoruz
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }

def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """
    Oyuncunun mevcut envanter durumuna göre metin oluşturur.
    Saf fonksiyondur, print kullanmaz, sadece string döndürür.
    """
    parcalar = []
    if credits:
        parcalar.append("bol kredi")
    if engines:
        parcalar.append("güçlü motor")
    if copilot:
        parcalar.append("yetenekli bir pilot")

    if not parcalar:
        return ""

    return "Sende: " + ", ".join(parcalar)


def hedef_menusu(hedefler: list[str]) -> str:
    """
    Gidilebilecek hedefleri numaralandırılmış bir menü metni olarak döndürür.
    """
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, 1):
        satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)