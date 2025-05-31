import streamlit as st
import joblib

# Başlık
st.title("📩 SMS Spam Sınıflandırıcı")
st.write("Bir SMS mesajı girin, spam olup olmadığını tahmin edelim.")

# Modeli yükle
model = joblib.load("sms_spam_model.pkl")

# Kullanıcıdan mesaj al
user_input = st.text_area("Mesajınızı buraya girin:")

if st.button("Tahmin Et"):
    if user_input.strip() == "":
        st.warning("Lütfen bir mesaj girin.")
    else:
        prediction = model.predict([user_input])[0]
        label = "📢 SPAM" if prediction == 1 else "✅ Normal"
        st.subheader("Sonuç:")
        st.success(label if prediction == 0 else label)
