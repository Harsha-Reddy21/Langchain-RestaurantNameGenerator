import streamlit as st
import helper

st.title("Restaurant Game Generator")

cuisine=st.sidebar.selectbox("Pick a Cuisine",('Indian','Mexican','Arabic','Italic'))

if cuisine:
    response=helper.generate_restaurant_name_and_items(cuisine)
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)