import streamlit as st

st.title("Clasificador de temperatura")

temperatura= st.number_input(
  "Introduce la temperatura en °c:",
  value=20
                            )

if temperatura < 10:
  st.write("Esta ice frio hielo")
elif temperatura < 25:
  st.write("La temperatura es agradable")
else:
  st.write("Hace calor")
