import streamlit as st

def app():
    header1, header2, header3 = st.columns([1,5,1])
    with header2:
        st.title(":blue[Our Services & Solutions]")

    st.markdown("""At RADOKI STATISTICS SOLUTIONS, we offer a comprehensive suite of statistical solutions tailored to meet the unique needs of our clients. 
                Our team of seasoned statisticians and data scientists is dedicated to transforming raw data into actionable insights, driving informed decision-making and strategic outcomes.""")    
    
    service1, service2, service3 = st.columns(3)
     
    with service1:
        container = st.container(border=True)
        container.subheader(":blue[WRITING]")
        container.markdown("""
                - RESEARCH PROPOSAL
                - DESSERTATION
                - CONCEPT NOTE
                - REPORT
                - ASSIGNMENT                     
                """) 
    with service2:
        container = st.container(border=True)
        container.subheader(":blue[DESIGNING]")
        container.markdown("""
                - DIGITAL RESUME/CV
                - GRAPHIC DESIGN
                - COVER LETTER
                - WEB APPS DESIGN AND DEVELOPMENT                                 
                """)
    with service3:
        container = st.container(border=True)
        container.subheader(":blue[TRAINING]")
        container.markdown("""
                - STATISTICS SOFTWARES (SPSS,STATA,EXCELL, R, PYTHON)
                - WEB APPLICATIONS DEVELOPMENT
                - 3D RENDERING
                - BASIC COMPUTER TRAINING           
                """)
    service4, service5, service6 = st.columns(3)
    with service4:
        container = st.container(border=True)
        container.subheader(":blue[RESEARCH CONSULTANCY]")
        container.markdown("""
                - Study Design and Protocol Development
                - Sample Size Determination
                - Statistical Review and Validation
                 """)

    with service5:
        container = st.container(border=True)
        container.subheader(":blue[COACHING]")

    with service6:
        container = st.container(border=True)
        container.subheader(":blue[DATA COLLECTION AND ANALYSIS]")  
        container.markdown("""
                - Descriptive Statistics
                - Inferential Statistics
                - Exploratory Data Analysis (EDA)
                - Statistical Hypothesis Testing
                """)  

    
    st.video("10.mp4")
    col1, col2, col3 = st.columns([1,3,1]) 
    with col2:
        st.link_button("**Ready to master the skills of data analysis? Enroll today**", "https://docs.google.com/forms/d/e/1FAIpQLSeY_gQuvNCBiklGcTvOb45A3k1PwqMauDJx147dqrxIt1gk6Q/viewform?usp=sharing", help="Click to access the registration form and register yourselt into our statistical softwares training program")


    st.header(":blue[Why Choose RADOKI STATISTICS SOLUTIONS!!]")
    
    st.markdown("""we bring data to life. Specializing in cutting-edge statistical analysis, predictive modeling, and data-driven insights, we empower businesses to make informed decisions. 
            Our expert team harnesses the power of data to uncover patterns, trends, and opportunities that drive success. 
            From comprehensive data analytics to bespoke statistical solutions, we tailor our expertise to meet your unique needs. 
            Elevate your decision-making process with RADOKI and transform raw data into actionable intelligence. Discover the potential within your data – because every number tells a story, and we're here to help you interpret it.
        """)
    st.image("4.jpeg", width=700)
    st.write("###")
    st.header(":blue[Frequently asked Questions (FAQs)]")
    with st.expander("**What industries does RADOKI work with?**"):
        st.write("RADOKI serves clients across diverse industries, including healthcare, finance and banking, manufacturing, retail, technology and IT, government, and education.")
    with st.expander("**Can RADOKI handle customized statistical solutions for specific business needs?**"):
        st.write("Yes, absolutely! RADOKI specializes in providing customized statistical solutions tailored to address unique challenges in different industries. We work closely with clients to understand their specific needs and deliver bespoke solutions.")
    with st.expander("**How do I stay updated on RADOKI's latest insights and content?**"):
        st.write("Stay informed by following us on [LinkedIn], [Twitter], and [Facebook] for real-time updates.")
    with st.expander("**How can I request a consultation with RADOKI?**"):
        st.markdown("""To request a consultation, please reach out through our contact form, email us at raymondkishiwa47@gmail.com, or call our client support hotline at **+255 753 093 786**.
                If you have additional questions or need further assistance, feel free to contact us. We're here to help!
                """) 


    st.write(" --- ") 
    #------FOOTER--------
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
