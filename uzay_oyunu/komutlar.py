
from functools import wraps
from typing import Callable, Dict, Any, Tuple


KOMUTLAR: Dict[str, Tuple[Callable[..., str], str]] = {}


def komut(ad: str, aciklama: str = "") -> Callable[[Callable[..., str]], Callable[..., str]]:
    """Komutları KOMUTLAR sözlüğüne kaydeden dekoratör."""

    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten kayıtlı!")

        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            return func(*args, **kwargs)

        KOMUTLAR[ad] = (wrapper, aciklama)
        return wrapper

    return decorator




@komut("yardim", "komutları ve açıklamalarını listeler")
def komut_yardim(durum: dict) -> str:
    """Mevcut komutları listeler."""
    satirlar = []
    for ad, (_, aciklama) in KOMUTLAR.items():
        satirlar.append(f"{ad}: {aciklama}")
    return "\n".join(satirlar)


@komut("envanter", "envanter eşyalarını gösterir")
def komut_envanter(durum: dict) -> str:
    """Oyuncunun envanterindeki eşyaları gösterir."""
    credits = durum.get("credits", 0)
    engines = durum.get("engines", 0)
    copilot = durum.get("copilot", "Yok")
    return f"Credits: {credits}, Engines: {engines}, Copilot: {copilot}"


@komut("harita", "gidebileceğin gezegenleri gösterir")
def komut_harita(durum: dict) -> str:
    """Mevcut konumdan gidilebilecek bağlantıları gösterir."""
    konum = durum.get("konum", "Bilinmiyor")
    baglantilar = durum.get("baglantilar", {})
    komsumlar = baglantilar.get(konum, [])
    return f"Şu an {konum}desin. Gidebileceğin yerler: {', '.join(komsumlar)}"