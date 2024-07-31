import streamlit as st
from streamlit_option_menu import option_menu

# Inclure le logo
st.image('agris-removebg-preview.png', width=700)  # Adjust the width as needed

# Description de l'application
st.markdown("""
    <div style="color: #000000; font-size: 20px; font-weight: bold; text-align: center; margin-bottom: 20px;">
This application helps farmers detect plant leaf diseases and generate reports with recommended solutions. Additionally, it offers a weather dashboard to help you plan your agricultural activities.
    </div>
""", unsafe_allow_html=True)




selected = option_menu(
        menu_title=None,
        options=["home","Today's weather", "Leaf disease detection"],
        icons=['weather', 'image'],
        menu_icon="cast", default_index=0, orientation="horizontal",
        
    )
if selected == "Today's weather":
    st.switch_page('pages/Weather.py')
elif selected == "Leaf disease detection":
     st.switch_page('pages/LeafDiseaseDetection.py')



