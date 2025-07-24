import streamlit as st
import numpy as np
import pandas as pd
import time 

st.title("Welcome(Title)")
st.header("To my Home Page(Header)")
st.subheader("Lets step up our career(Subheader)")
st.write("It is more than just a motto — it’s a movement. Join us as we explore new skills, seize opportunities, and grow together toward a brighter, more successful future")
st.markdown("Empower yourself with the right tools, guidance, and mindset to unlock your true potential in today’s evolving professional world")
st.caption("Your career won't wait—why should you? Let's level up together.")

st.image("streamlit/image.png")
st.audio("streamlit/speech.wav")
st.video("streamlit/video.mp4")

# st.checkbox('Select from these:'['jungkook','taehyung', 'namjoon', 'yoongi']) <-- wrong
# Python doesn’t allow strings to be indexed with lists, only integers. That’s why it raised a TypeError.Use multiple st.checkbox() calls for each name, or use st.multiselect() to let users select multiple options from a list.
# st.checkbox('Select from these:'[0,1,2,3,4]) <-- wrong // string indices must be integers, not 'tuple'
st.checkbox('checkbox')
st.button('Click button')
st.radio('Pick one',['bts', 'ateez', 'blackpink', 'newjeans'])
st.selectbox('Pick one',['webdev', 'blockchain', 'dsa', 'da', 'cloud'])
st.multiselect('Pick one',['jk', 'v', 'rm', 'suga'])
st.select_slider('Give a remark',['Good', 'Better', 'Best'])
st.slider('Your marks',50,100)
st.slider('Select a float value', min_value=0.0, max_value=10.0, step=0.01) # for float

on = st.toggle("Activate Feature")
if on:
    st.write('Feature Activated')

number = st.number_input('Insert a number')
st.write('The current number is',number)

d = st.date_input('When is your birthday', value= None)
st.write('Your birthday is:', d)

t = st.time_input('Set an alarm for', value= None)
st.write('Alarm is set for', t)

st.number_input('Enter your marks',0,100)
st.text_input('Enter text') # used when we want to take input of atleast 1-2 lines from users
st.date_input('Exam date')
st.time_input('Exam time')
st.text_area('Description') # used for large documents, like multiple paragraphs and all
st.file_uploader('Upload files') # streamlit gives a capacity of max 200 mb to upload any file
st.color_picker('Choose a color')

# following will be user message not system message, for e.g., if i want to show my message in the highlight of green color we will use success, similarly error for red and so on, it doesnt show that user input have messed with system it simply highlights in diff colors
st.success('Success')
st.error('Error')
st.warning('Warning')
st.info('Information')
st.exception(RuntimeError('RuntimeError execption'))

st.sidebar.title('Keep Learning')
st.sidebar.image('image.png')
# in sidebar, the img, text, audio, video anythinng will simply be displayed on the side of the page, and to apply sidebar we can simply add .sidebar inbetween the st. commands, for e.g., st.sidebar.image("image.png")

df = pd.DataFrame(np.random.randn(50,20), columns=("col %d"%i for i in range(20)))
st.dataframe(df)

df = pd.DataFrame(np.random.randint(1,100,size=(10,5)), columns = ("col %d"%i for i in range(5)))
st.dataframe(df)
# dataframes can be created using csv files also, refer to the session of df, pandas(notes, jupyter nb). Difference between randn and randint is, randn have random floating-point numbers from a standard normal distribution (mean = 0, std = 1) Values can be positive or negative, and randint have random integers in the specified range, You set min and max range                                 

df = pd.DataFrame(np.random.randn(10,10), columns= ("col %d"%i for i in range(10)))
st.table(df)
# minor difference between df and table, df have curved edges with highlighted titles(col1, col2,...), whereas table have cornered edges, no highlighted titles 
# Aspect	   |       df (DataFrame)	                |      Table
# Type	       |      Python object (Pandas DataFrame)	|     General data structure (visual or logical)
# Editable?	   |      Yes, programmatically	            |     Usually not editable (unless UI allows it)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature","70 F","1.2 F")
col2.metric("wind","9 mph","-8%")
col3.metric("Humidity","86%",'4%')
# we first made columns by st.columns and gave content to each column

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
# whenever we want to make chatbot, the first command is chat input, {prompt} → captures the user's message,        f → allows inserting the prompt into the display message

with st.status('Step 1'):
    st.write('Step 2')
    time.sleep(1)
    st.write('Step 3')
    time.sleep(1)
    st.write('Step 4')
    time.sleep(1)
st.button('Rerun')
# here we used time module imported initially, status shows status for e.g., installing a file shows status like exporting the file, extracting the file, finishing the operation, we show these labeled operations by status, and then there is rerun, which will perform all status again , time.sleep(1) - Pause the execution of the program for 1 second

chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.area_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.bar_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.line_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.scatter_chart(chart_data) 

df = pd.DataFrame({'lat':[23.210169],
                   'lon':[72.635160]})
st.map(df)

with st.chat_message('user'):
    st.write('Khopdi Tod Saale ka')
# 2 roles in chatbot : user role, assisstant role, if we want to show the communication of both then we've to metion from whom the chat meessage is sent and write it, here it is user role 
# 'with' have the main heading, below that there are icons, here 'with' will contain the main icon of user and below that is message 
