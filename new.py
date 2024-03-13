import streamlit as st
from streamlit_option_menu import option_menu
import about, account, contact, home
import time



st.set_page_config(
    page_title="RADOKI STATISTICS SOLUTIONS",
    page_icon="3.png"
)


page_bg_img = """
<style>
#[data-testid="stAppViewContainer"] {
#background-image: url("https://images.unsplash.com/photo-1476673160081-cf065607f449?q=80&w=1472&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
#}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"] {
right: 1rem;
}

[data-testid="stSidebar"] {
background-image: url("https://images.unsplash.com/photo-1468581264429-2548ef9eb732?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
}

</style>
"""


st.markdown(page_bg_img, unsafe_allow_html=True)





class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })    
    def run():
        #with st.sidebar:
        app = option_menu(
                menu_title=None,
                options=['Home','About','Services','Contacts'],
                icons=['house-fill','info-circle-fill','trophy-fill','chat-fill'],
                menu_icon='cast',
                orientation="horizontal", 
                default_index=0,
                #styles={
                #    "container": {"padding": "5!important","background-color":'black'},
                #    "icon": {"color": "white", "font-size": "23px"}, 
                #    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#02ab21"},
                #    "nav-link-selected": {"background-color": "blue" }}
                     
                )
            
        #st.write("RSS")
        #st.write("Copyright 2024")
            
            
        if app=='Home':
            home.app()
        if app=='Services':
            account.app()
        if app=='About':
            about.app()
        if app=='Contacts':
            contact.app()
    run()
    
