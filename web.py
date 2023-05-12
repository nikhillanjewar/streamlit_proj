import streamlit as st

st.set_page_config(page_title="My Profile", page_icon=":tada:", layout="wide")
from PIL import Image

#set up the columns
col1, col2 = st.columns([2,3])
with col1:
	img = Image.open("profile.jpeg")
	st.image(img, width=200)
	
	
	#profile
	st.subheader("PROFILE")
	st.write("To Enhance my professional skills, capabilities and knowledge in an organization which recongnize the value of hard work and trust me with responsibilities and challenges,I am passionate about finding ways to solve problems :)")
	
	
	#contact
	st.subheader("CONTACT")
		st.write("Gmail : nikhillajewar03@gmail.com")
		st.write("linkedIn :[Nikhil's LinkedIn Profile](https://www.linkedin.com/in/nikhil-lanjewar-3b4a75205/)")
		st.write("github : [Nikhil's Github Profile(https://github.com/nikhillanjewar)")
	
	#certifications
	st.subheader("Certifications")
		st.write("Learn C++ (Codeacademy)")
		st.write("Python3 (Codeacademy)")
		st.write("JavaScript Basic (Hackerrank)")
	
	
	#personal_skills
	st.subheader("PERSONAL SKILLS")
		st.write("* Adaptable in any situation, can work in a dynamic and flexible Enviornment")
		st.write("* Ability to thing thoughtfully")

with col2:	
	st.title("Hi, I am NIKHIL LANJEWAR😎️")
	st.write("ELECTRONICS AND TELECOMMUNICATION")
	
	
	#education
	st.subheader("EDUCATION ")
	
	st.write("BACHELOR OF TECHNOLOGY")
	st.write("S.B. Jain Institute of Technology, Management and Research, Nagpur")
	st.write("Electronics and Telecommunication Engineering")
	st.write("pursuing")
	 
	st.write("HSC")
	st.write("Seth Kesrimal Porwal College, Kamptee")
	st.write("2020")

	st.write("SSC")
	st.write("Baliramji Dakhane Highschool, Kanhan")
	st.write("2018") 
	
	
	
	#projects
	st.subheader("PROJECTS")
	st.write("1. STUDENT DATABASE MANAGEMENT SYSTEM using C++")
	st.write("--Student Database Management System is a necessity of educational information can manage student data and manage many student related data needs in a school or college")
	
	st.write("2. Personal Assist-Chatbot using python")
	st.write("--Personal Assist-chatbot is a virtual software application developed is primarily avilable on laptop or personal computer devices using QT GUI Designer for creting a interfacing of assistant")
	
	
	#skills
	st.subheader("SKILLS")
	st.write("*C")
	st.write("*C++")
	st.write("*Python")
	st.write("*Javascript")
	st.write("*MYSQL")
	
	
	
	
	
	

	

	
	



