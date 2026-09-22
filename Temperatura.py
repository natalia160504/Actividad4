import streamlit as st

st.title("Clasificador de temperatura")

temperatura= st.number_input(
  "Introduce la temperatura en °c:",
  value=20
                            )

if temperatura < 5:
  st.write("Esta ice frio hielo")
elif temperatura < 27:
  st.write("Esta bombastic")
else:
  st.write("Estan planchando al diabolo")
