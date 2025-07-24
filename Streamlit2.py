# re- regular expression which will be further used in nlp, we can give a pattern through regular expression, and the user input which can validate the pattern fully, can be validated as a user name

import re 
import streamlit as st
user_input = st.text_area('Enter your email ID')

pattern = re.compile(r'([A-Za-z0-9]+[.])*[A-Za-z0-9]+@[A-Za-z0-9]+(.[A-Z|a-z]{2,})+')

def check(email):
    if re.fullmatch(pattern,email):
        return "Valid email ID"
    else:
        return "Invalid email ID"
    
if (st.button('check')):
        response = check(user_input)
        st.success(response)
# a function 'check' created, with parameter 'user input', the user given email is compared with the pattern(pattern,email), by re.fullmatch method, this all will be triggred by button
# the button will check, whether it is clicked, if yes then check func is called with parameter as user input, then send success message