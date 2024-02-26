import streamlit as st
from streamlit_option_menu import option_menu
import about, account, contact, home

st.set_page_config(
    page_title="RADOKI STATISTICS SOLUTIONS",
    page_icon="3.png"
)

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })    
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='RSS ',
                options=['Home','About','Services','Contacts'],
                icons=['house-fill','info-circle-fill','trophy-fill','chat-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#02ab21"},
        "nav-link-selected": {"background-color": "blue" },}
                
                )
            st.write("RSS")
            st.write("Copyright 2024")
            
            
        if app=='Home':
            home.app()
        if app=='Services':
            account.app()
        if app=='About':
            about.app()
        if app=='Contacts':
            contact.app()
    run()
    
