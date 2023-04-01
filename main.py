import streamlit as st

st.title("Aplikasi perhitungan molaritas ngab")

bobot = st.number_input("Masukan nilai bobot coy")
volume = st.number_input("Masukan nilai volume coy")
mr = st.number_input("Masukan nilai Mr")

tombol = st.button("Hitung nilai Molaritas")

if tombol:
    nilai_molaritas = bobot/(mr*volume)
    st.success(f'Nih ngab Nilai Molaritasnya adalah {nilai_molaritas}')
               