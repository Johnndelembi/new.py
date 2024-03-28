import streamlit as st
import time


def app():
    st.image("header1.png")
    st.write("""At RADOKI STATISTICS SOLUTIONS, we bring data to life. Specializing in cutting-edge statistical analysis, predictive modeling, and data-driven insights, we empower businesses to make informed decisions.
    We aim to provide comprehensive support and expertise where you need in research proposal and dissertation writing, curriculum vitae creation, 
    data collection and analysis, training, concept note writing, graphic design, and coaching.""")
    st.video("RADOKI PLUS.mp4")
     
    Read_More = """ Our expert team harnesses the power of data to uncover patterns, trends, and opportunities that drive success. From comprehensive data analytics to bespoke statistical solutions, we tailor our expertise to meet your unique needs. Elevate your decision-making process with RADOKI and transform raw data into actionable intelligence. Discover the potential within your data – because every number tells a story, and we're here to help you interpret it.
     """
    def stream_data():
            for word in Read_More.split():
              yield word + " "
              time.sleep(0.05)
    
    if st.button("Read More"):
        st.write_stream(stream_data)

    st.subheader(":blue[THE DATA ANALYSIS PROCESS]")
    st.image("process.PNG")    

    with st.expander("**OUR SERVICES**"):
        st.video("7.mp4")    
        st.markdown("""Our services cater to individuals and organizations seeking high-quality assistance in various aspects of research and data analysis. 
            Our team of seasoned statisticians and data scientists is dedicated to transforming raw data into actionable insights, driving informed decision-making and strategic outcomes.""")
        
        read_more = """At RADOKI STATISTICS SOLUTIONS, we are dedicated to delivering exceptional results and exceeding your expectations. 
        Trust us with your statistical and research needs, and let us empower you to succeed in your academic or professional endeavors.
        With us you dont have to worry about how your tasks because we got you covered"""
        
        def stream_data():
            for word in read_more.split():
              yield word + " "
              time.sleep(0.05)

        if st.button("Read more"):
            st.write_stream(stream_data)      

        st.write(" ### ")
        st.write(" ### ")
        st.subheader("STATISTICS SOFTWARES TRAINING FOR DATA ANALYSIS")
        st.video("6.mp4")
        st.link_button("Sign Up", "https://forms.gle/Xnu8tWWAzJXFVJeb8", help="Are you interested to learn the ways of data analysis and related software packages? Sign Up today and get the best guidance from our qualified tutors")
        st.write(" ### ")
     
    #st.image("assignment.PNG")
    #col6, col7 = st.columns(2, gap="small")
    #with col6:
       # st.markdown("""
        #Feeling overwhelmed by statistics homework? We understand – college can be hectic! We offer "Statistics Assignment Help" to ease your workload and ensure top-notch support:

       # **Experienced tutors:** Our experts can help you with statistics, programming, assignments, homework, and projects. They're familiar with various statistical tools like SPSS, Python, R, Excel & STATA.
        #**Focus on learning, not deadlines:** 
        #- Free up your time to truly understand the concepts. We'll handle the assignments, allowing you to focus on other areas.
        #**Stay ahead of the curve:** 
       # - Our tutors are well-versed in the latest data science, big data, and machine learning algorithms used in college curriculums.
        #Get the support you deserve and achieve academic success!""")

    #with col7:    
        3#st.markdown("""
        #We offer statistics assignment help, ranging from          
        #Organizing and graphing data.
        #Probability.
        #Numerical descriptive measures.
        #Continuos random variables and distributions.
        #Sampling distribution.
        #Hypothesis testing about mean and proportion.
        #Regression analysis, inferential analysis and related statisitcs topics.
        #""")
        #st.subheader(":blue[Statistics Assignments Help from Statistics Experts]")
        #st.link_button("Upload Your Assignment", "https://forms.gle/kuExVCZeAXtCtSHb7")    

    
    st.write(" ### ")    
       
    st.subheader(":blue[Share your statistics and data challenges with us]")
    st.caption("Allow our team of data experts to tap into your challenge and come up with a solution by messaging us via the form below")
    with st.form("my_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1.text_input("Enter your Email")
        col2.text_input("Phone Number")    
        message = st.text_area("Message")
        send = st.form_submit_button("Send")

        if send:
            with st.spinner("Sending..."):
                time.sleep(3)
                st.success("Sent and Received successfull")


    st.write(" --- ") 
    #------FOOTER--------
    st.write(" ### ")    
    footer1, footer2, footer3, footer4 = st.columns(4)

    with footer1:
        st.write("instagram")

    with footer2:    
        st.write("facebook")
    
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
        st.markdown("Email: raymondkishiwa47@gmail.com") 
        st.markdown("Ubungo, Dar es Salaam")
    
    with footer7:
        st.image("3.png")     

    



        
