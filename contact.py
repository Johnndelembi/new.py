import streamlit as st
import time

def app():
    st.title(":blue[Get in Touch with Us]")
    st.markdown("""
            We value your inquiries and are here to assist you. 
            Feel free to reach out to us through any of the following contact options:
            """)
    
    st.write("###")
    st.subheader(" Email 📧 ")
    st.markdown("General Enquiries: radokistatisticssolutions@gmail.com")
    st.markdown("Client Support: williamjohnie61@gmail.com")

    st.write("###")
    st.subheader("Phone :phone:")
    st.markdown("Main office: +255 753 093 786")
    st.markdown("Client Support: +255 625 232 734")

    st.write("###")
    st.subheader("Physical Address")
    st.markdown("Ubungo, Dar es Salaam")
    st.markdown("Tanzania")

    st.write("###")
    st.subheader("Contact Form")
    st.markdown("Fill out our contact form below for a quick response. Fields marked with (*) are required.")

    with st.form("my_form2", clear_on_submit=True):
        contact1, contact2 = st.columns(2)
        contact1.text_input("Enter your name")
        contact2.text_input("Enter your Email")
        message = st.text_area("Enter your Message")
        send = st.form_submit_button("Send")

        if send:
            with st.spinner("Sending..."):
                time.sleep(3)
                st.success("Sent and Received successfull")        
        st.caption("***You can email us directly at raymondkishiwa47@gmail.com***")

    #---------FOOTER--------
    st.write(" ### ")    
    footer1, footer2, footer3, footer4 = st.columns(4)

    with footer1:
        st.write("Instagram")

    with footer2:    
        st.write("Facebook")
    
    with footer3:    
        st.write("Youtube")

    with footer4:
        st.write("LinkedIn")    

    st.write("###")
    footer5, footer6, footer7 = st.columns([1,3,1])
    
    with footer7:
        st.image("3.png")   
        st.write("Copyright 2024")    
