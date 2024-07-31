import streamlit as st
# Exemple d'utilisation de st.components.v1.iframe
iframe_src ="https://app.powerbi.com/view?r=eyJrIjoiNzg4M2E3YzQtYmUyZS00MWE1LTlhYTMtYWZhYjAxMzcyNGM0IiwidCI6ImRiZDY2NjRkLTRlYjktNDZlYi05OWQ4LTVjNDNiYTE1M2M2MSIsImMiOjl9" 

st.components.v1.iframe(
    src=iframe_src,
    width=800,
    height=900,
    scrolling=True  # Permet le défilement si nécessaire
)

