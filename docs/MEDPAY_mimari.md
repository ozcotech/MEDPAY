
# MEDPAY Yazılım Mimarisi

## Genel Bakış

MEDPAY, 2025 yılı Arabuluculuk Ücret Tarifesi'ne göre geliştirilen, mobil uyumlu ve grafik kullanıcı arayüzüne (GUI) sahip bir ücret hesaplama uygulamasıdır. Program, Model-View-Controller (MVC) mimarisine göre yapılandırılmıştır.

---

## Katmanlar ve Görevleri

### 1. 🧱 Model Katmanı (`models/`)
Veri yapıları ve iş mantığı bu katmanda yer alır.

- **TarifeModel:** 
  - 2025 ve gelecekteki yıllara ait sabit tarife verilerini içerir.
  - constants klasöründeki verileri kullanarak hesaplamaya temel sağlar.
- **UyusmazlikModel:** 
  - Uyuşmazlık türü bilgilerini içerir (ad, id, parasal mı, sabit ücretler).
- **HesaplamaModel:** 
  - Arabuluculuk ücretini hesaplayan ana sınıftır.
  - Dilim hesaplaması, minimum ücret, seri uyuşmazlık gibi kuralları içerir.

---

### 2. 🖼️ View Katmanı (`screens/`)
Kivy framework'ü kullanılarak oluşturulan kullanıcı arayüzü ekranlarıdır.

- **AnaSayfa:** Giriş ekranı
- **UyusmazlikSecimEkrani:** Para olan/olmayan uyuşmazlık seçimi
- **AnlasmaDurumuEkrani:** Anlaşma yapılıp yapılmadığı seçimi
- **UyusmazlikTuruEkrani:** Uyuşmazlık türü seçimi (Aile, Ticari, vb.)
- **TarafBilgiEkrani:** Taraf sayısı, tutar ve arabulucu sayısı girişi
- **SonucEkrani:** Hesaplama sonuçlarının gösterimi

---

### 3. 🧠 Controller Katmanı (`controllers/`)
İş akışını ve kullanıcı etkileşimlerini yöneten katmandır.

- **UygulamaController:** 
  - Ekranlar arası geçişleri ve genel uygulama akışını kontrol eder.
- **HesaplamaController:** 
  - Kullanıcının girdiği verileri alır, modele gönderir ve sonucu uygun ekrana aktarır.

---

### 4. 📦 Constants Katmanı (`constants/`)
Tarife verileri ve sabit yapıların tutulduğu yerdir.

- **tariffs_2025.py:** 2025 yılına ait tarife oranlarını içerir.
- **tariffs_2026.py (örnek):** Gelecek yıllar için uyarlanabilir.
- Yapı, yıl bazında veri güncellemesini kolaylaştırır.

---

### 5. 🛠️ Utils Katmanı (`utils/`)
Ortak yardımcı fonksiyonlar burada tanımlanır.

- Hata mesajı gösterimi (popup)
- Metin biçimlendirme
- Girdi doğrulama gibi tekrar eden işlemler

---

### 6. 🧪 Tests Katmanı (`tests/`)
Birime ve bütünlüğe yönelik testler içerir.

- Pytest ile entegre test senaryoları yazılabilir.
- `test_hesaplama.py`, `test_tarife_verisi.py` gibi test dosyaları içerir.

---

## Genişletilebilirlik

- Yıl değiştikçe sadece `constants` klasörü güncellenir.
- Yeni ekran veya hesaplama eklenecekse, sadece ilgili klasöre yeni dosya eklenmesi yeterlidir.
- PDF çıktısı, dil desteği, veri kaydı gibi özellikler kolayca entegre edilebilir.

---

## Kullanım Ortamı

- **İşletim Sistemi:** macOS
- **Editör:** Visual Studio Code
- **Arayüz Kütüphanesi:** Kivy
- **Python Versiyonu:** 3.11+
