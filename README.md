# SMS Spam Detection with NLP

Bu projede, SMS mesajlarının spam olup olmadığını sınıflandıran bir makine öğrenmesi modeli geliştirildi. Model, temel metin ön işleme adımlarını, TF-IDF vektörleştirme yöntemini ve Naive Bayes algoritmasını kullanmaktadır.

## Kullanılan Veri Seti

- [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- `spam.csv` dosyası, projenin kök dizininde yer almaktadır.

## Proje Adımları

1. **Veri Yükleme ve Temizleme**
   - Gereksiz sütunlar çıkarıldı.
   - Mesajlar temizlendi ve küçük harfe çevrildi.

2. **Özellik Çıkarımı**
   - Metinler TF-IDF ile vektörleştirildi.

3. **Model Eğitimi**
   - Naive Bayes algoritması ile eğitim yapıldı.
   - Model, %95 doğruluk oranına ulaştı.

4. **Anahtar Kelime Çıkarımı**
   - Mesajlardan en sık geçen anahtar kelimeler tespit edildi ve görselleştirildi.

## Sonuçlar

- Model doğruluk oranı: **%95**
- En sık geçen anahtar kelimeler grafiklerle gösterildi.

## Kullanılan Kütüphaneler

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## Nasıl Çalıştırılır?

1. Gerekli kütüphaneleri yükleyin:
2. Jupyter Notebook ortamında `spam_detection.ipynb` dosyasını açın ve adımları sırayla çalıştırın.
3. Sonuçları ve grafikleri görüntüleyin.

---

**Proje Notları:**
- Daha gelişmiş özellikler için farklı model veya ek metin ön işleme teknikleri denenebilir.
- Proje örnek bir NLP çalışmasıdır, eğitim amaçlı hazırlanmıştır.

