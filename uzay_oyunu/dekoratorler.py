from functools import wraps
import time
from typing import Callable, Any


def log_cagri(func: Callable[..., Any]) -> Callable[..., Any]:
    """Fonksiyon çağrılarını ve dönüş değerlerini loglayan dekoratör."""

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={v!r}" for k, v in kwargs.items()])
        tum_argumanlar = ", ".join(filter(None, [args_str, kwargs_str]))

        print(f"-> {func.__name__}({tum_argumanlar})")
        sonuc = func(*args, **kwargs)
        print(f"<<- {func.__name__} {sonuc}")
        return sonuc

    return wrapper

def sure_olc(func: Callable[..., Any]) -> Callable[..., Any]:
    """Fonksiyonun çalışma süresini ölçen ve ekrana yazdıran dekoratör"""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        baslangic = time.perf_counter()
        sonuc = func(*args, **kwargs)
        bitis = time.perf_counter()
        sure = bitis - baslangic
        print(f"{func.__name__}: {sure:.4f} sn")
        return sonuc
    return wrapper


def say(func: Callable[..., Any]) -> Callable[..., Any]:
    """Fonksiyonun kaç kez çağrıldığını bir nitelikte (çağrı) sayan dekoratör."""

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.cagri += 1
        return func(*args, **kwargs)

    wrapper.cagri = 0
    return wrapper

def sinirla(alt: int, ust: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Fonksiyonun ilk argümanının verilen [alt, ust] aralığında olmasını sınırlar."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if args:
                deger = args[0]
                if not (alt <= deger <= ust):
                    raise ValueError(f"{func.__name__}: {deger} değeri {alt}-{ust} aralığında değil")
            return func(*args, **kwargs)
        return wrapper
    return decorator


from collections import OrderedDict


def hafiza(maxsize=None):
    """functools.lru_cache kullanmadan closure ve sözlük ile çalışan önbellek dekoratörü."""
    if callable(maxsize):
        func = maxsize
        cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                return cache[key]
            sonuc = func(*args, **kwargs)
            cache[key] = sonuc
            return sonuc

        return wrapper


    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache:
                if maxsize is not None:
                    cache.move_to_end(key)  # En son kullanılanı öne/sona taşı (LRU mantığı)
                return cache[key]

            sonuc = func(*args, **kwargs)

            if maxsize is not None and len(cache) >= maxsize:
                cache.popitem(last=False)  # En eski girdiyi sil

            cache[key] = sonuc
            return sonuc

        return wrapper

    return decorator