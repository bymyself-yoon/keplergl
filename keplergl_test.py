import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

st.write("This is a kepler.gl map in streamlit")

map_1 = KeplerGl()
keplergl_static(map_1)

col1 = st.column(1)
with col1:
  keplergl_static(map_1)
