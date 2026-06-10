import streamlit as st
import string
import random

st.title("Şifre oluşturalım!")

if st.button("Şifre Oluştur"):
    sifre=(
                 random.choice(string.ascii_lowercase)+
                 random.choice(string.ascii_uppercase)+
                 random.choice(string.digits)+
                 random.choice(string.punctuation)
       )

    kalan= ''.join(random.choices(
        string.ascii_letters + string.digits + string.punctuation,k=4))

    sifre += kalan

    st.write("Oluşturulan şifre:")
    st.code(sifre)