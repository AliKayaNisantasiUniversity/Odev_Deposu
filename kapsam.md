# Kapsam (Scope) ve UnboundLocalError Raporu

## 1. Kapsam Örnekleri Tahminleri ve Sonuçları
- **Yerel Kapsam (Local Scope):** Bir fonksiyonun içinde tanımlanan değişkenler sadece o fonksiyonun içinde geçerlidir, dışarıdan erişilemez.
- **Global Kapsam (Global Scope):** Dosyanın en üst seviyesinde tanımlanan değişkenlere hem ana koddan hem de fonksiyonların içerisinden (okuma amaçlı) erişilebilir.
- **Enclosing Kapsam (İç içe fonksiyonlar):** İç içe fonksiyon (closure) durumunda, içteki fonksiyon dıştaki fonksiyonun değişkenlerine erişebilir.

## 2. UnboundLocalError Açıklaması
Python'da bir fonksiyon içinde global bir değişkene değer atamaya (`x = x + 1` gibi) çalıştığınızda, Python o değişkeni otomatik olarak o fonksiyonun **yerel (local)** değişkeni olarak algılar. Ancak atama işleminden önce değişkeni okumaya (`x`'in değerini almaya) kalkarsanız, Python yerel değişkenin henüz tanımlanmadığını düşünür ve **`UnboundLocalError`** hatası fırlatır. Bunu önlemek için global değişkenleri değiştireceksek `global` anahtar kelimesi (ödev kurallarınca yasaksa closure/parametre yöntemleri) kullanılmalıdır.