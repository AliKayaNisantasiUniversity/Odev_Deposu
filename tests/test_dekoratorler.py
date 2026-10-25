from uzay_oyunu.dekoratorler import sure_olc, say

def test_sure_olc_meta_ve_sonuc():
    @sure_olc
    def ornek_topla(a: int, b: int) -> int:
        """Toplama yapar."""
        return a + b


    assert ornek_topla.__name__ == "ornek_topla"
    assert ornek_topla.__doc__ == "Toplama yapar."


    sonuc = ornek_topla(a=5, b=10)
    assert sonuc == 15

    @lru_cache(maxsize=None)
    @say
    def fib_3(n: int) -> int:
        if n < 2:
            return n
        return fib_3(n - 1) + fib_3(n - 2)

from functools import lru_cache
from uzay_oyunu.dekoratorler import hafiza

def test_hafiza_vs_lru_cache():

    @hafiza(maxsize=2)
    def kare_al(x: int) -> int:
        return x * x

    assert kare_al(5) == 25
    assert kare_al(5) == 25


    @lru_cache(maxsize=2)
    def kare_al_lru(x: int) -> int:
        return x * x

    assert kare_al_lru(5) == 25
    assert kare_al_lru(5) == 25