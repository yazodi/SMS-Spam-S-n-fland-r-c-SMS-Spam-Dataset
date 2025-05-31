# 📩 SMS Spam Detection with NLP

Bu projede, SMS mesajlarının spam olup olmadığını sınıflandıran bir makine öğrenmesi modeli geliştirildi.  
Model, temel metin ön işleme adımlarını, **TF-IDF vektörleştirme** yöntemini ve **Naive Bayes algoritmasını** kullanmaktadır.

---

## 📊 Kullanılan Veri Seti

- [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- `spam.csv` dosyası, projenin kök dizininde yer almaktadır.

---

## ⚙️ Proje Adımları

1. **Veri Yükleme ve Temizleme**
   - Gereksiz sütunlar çıkarıldı.
   - Mesajlar temizlendi ve küçük harfe çevrildi.

2. **Özellik Çıkarımı**
   - Metinler TF-IDF ile vektörleştirildi.

3. **Model Eğitimi**
   - Naive Bayes algoritması ile eğitim yapıldı.
   - Model, %95 doğruluk oranına ulaştı.

4. **Tahmin Uygulaması (Streamlit)**
   - Kullanıcıdan SMS alınıp modelle sınıflandırma yapıldı.

5. **Anahtar Kelime Çıkarımı**
   - Mesajlardan en sık geçen anahtar kelimeler tespit edildi ve görselleştirildi.

---

## ✅ Sonuçlar

- Model doğruluk oranı: **%95**
- En sık geçen anahtar kelimeler grafiklerle gösterildi.
- Basit ve hızlı çalışan bir web arayüz ile kullanıcı mesajları test edebilir.

---

## 🚀 Nasıl Çalıştırılır?

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt


Streamlit uygulamasını başlatın:
streamlit run app.py
Açılan web arayüzden SMS mesajınızı girin ve sınıflandırmayı görün.


🔐 Örnek SPAM Mesajları
Aşağıdaki mesajlar büyük ihtimalle "SPAM" olarak sınıflandırılacaktır:

"Congratulations! You've won a free ticket to Bahamas. Text WIN to 12345 now!"

"Claim your free prize now by clicking this link: www.scamlink.com"

"URGENT! You have won a $1000 gift card. Call now!"

"Get cheap loans instantly. Apply now without any credit check!"

"Free ringtone offer just for you! Send 'TONE' to 55555!"



🧰 Kullanılan Kütüphaneler
pandas

numpy

scikit-learn

joblib

streamlit

matplotlib

seaborn


🤖 Model Paylaşımı
Eğitimli modeli Hugging Face üzerinde incelemek ve kullanmak için aşağıdaki bağlantıyı ziyaret edebilirsiniz:

🔗 Hugging Face – yazodi/sms-spam-detector


📝 Notlar
Proje eğitim amaçlıdır.

Farklı modeller ve ön işleme teknikleri denenerek geliştirme yapılabilir.