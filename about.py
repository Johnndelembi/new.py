import streamlit as st
def app():
    header1, header2, header3 = st.columns([2,2,3])
    with header2:
        st.title(":blue[About Us]")

    st.subheader("A deep dive into :blue[RADOKI STATISTICS SOLUTIONS]")
    st.markdown("""RADOKI STATISTICS SOLUTIONS, founded 2023, is a dynamic team of seasoned statisticians, data scientists, and industry experts. 
        With a passion for unraveling the complexities of data, we have successfully partnered with diverse businesses to enhance decision-making processes, drive efficiency, and unlock new opportunities. 
        Our commitment to excellence, coupled with a client-focused approach, sets us apart as a trusted partner for organizations seeking to harness the full potential of their data.
    """)
    
    st.image("mvv.png")
    col1, col2, col3 = st.columns(3)
    with col1:
        container = st.container(border=True)
        container.subheader(":blue[Our Mission]")
        container.markdown("""At RSS, our mission is to empower organizations through innovative statistical solutions. 
                        We are committed to unraveling the potential within data, providing clients with actionable insights that drive informed decision-making. 
                        By blending cutting-edge statistical methodologies with a client-centric approach, we aim to be the catalyst for transformative change in the way businesses leverage data.
                        in such we believe we can bring about change and development in institutions       
                    """)    
    with col2:
        container = st.container(border=True)
        container.subheader(":blue[Our Vision]")
        container.markdown("""Our vision at RSS is to be a leading organization in statistical analysis and data management in Tanzania, recognized for excellence in transforming complex data into clear, strategic insights. 
                        We envision a future where businesses, regardless of size or industry, harness the power of data to achieve unparalleled success. 
                        Through continuous innovation and a passion for problem-solving, we strive to redefine the landscape of data-driven decision-making.
                        while making the world a better place by providing data oriented solutions.   
                    """)
    with col3:
        container = st.container(border=True)
        container.subheader(":blue[Our Values]")
        container.markdown("""
            - **Excellence:** We are dedicated to delivering statistical solutions of the highest quality, setting the bar for excellence in every aspect of our work. 
            - **Integrity:** We uphold the highest standards of integrity, ensuring transparency, honesty, and ethical conduct in all our interactions.
            - **Innovation:** We embrace a culture of innovation, constantly exploring new statistical methodologies and technologies just to stay at the forefront.
            """) 


    
    st.subheader(":blue[Our Expert Team]")    
    st.markdown("""At RADOKI STATISTICS SOLUTIONS, our success is attributed to the exceptional individuals who make up our talented team. 
        Each member brings a wealth of expertise, a passion for data, and a commitment to delivering unparalleled statistical solutions.
    """)

    col4, col5, col6 = st.columns([1,4,1])
    with col5:
        st.subheader("Raymond D. Kishiwa | Founder & CEO")
        st.image("ray.png")
        st.markdown("""
                B.A in Statistics UDSM Graduate.  
                - Hands on experience in the field of Research, Data collection and analysis
                - Well versed around Python, SPSS, STATA, R and Excell.
                """)
        st.link_button("Read More", "")


        st.subheader("John Ndelembi | Data analyst ")
        st.image("IMG_7119.JPG", width=450)
        st.markdown("""
                B.A in Statistics | University of Dar es Salaaam
                - Hands on experience in the field of data science.
                - Well versed around Python, R, STATA and Excell for data science
                - Web developer at Py.Hub
                """)
        st.link_button("Read More", "https://johnndelembi.streamlit.app/")

    st.markdown("""Meet the minds behind RADOKI STATISTICS SOLUTIONS, a team dedicated to transforming raw data into strategic insights. 
                Our collective experience, passion for innovation, and commitment to excellence drive the success of our statistical solutions.""")    

    st.write(" ---- ")

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
    footer5, footer6, footer7 = st.columns([2,3,1])
    with footer5:
        st.subheader("Contacts") 
        st.markdown("+255 753 093 786")
        st.markdown("+255 625 232 734") 
        st.markdown("Email: radokistatisticssolutions@gmail.com")
        st.markdown("Ubungo, Dar es Salaam")
    
    with footer7:
        st.image("3.png")
    


