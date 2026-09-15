import streamlit as st

st.title("Clasificador de temperatura")

temperatura= st.number_input("Introduce la temperatura en °c:", value=20)

if temperatura <10:
  st.write("Hace frio")
elif temperatura >=10 and temperatura <=24:
  st.write("La temperatura es agradable")
  else
  st.write("Hace calor")
