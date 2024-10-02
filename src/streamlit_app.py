import streamlit as st

st.write("Hello world!")

st.header('st.button')

if st.button('say hello'):
    st.write('hello')
else:
    st.write('goodbye')

age = st.slider('how old are you', 0,130,25)
st.write(f'im {age} years old')

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")
   number = st.number_input("Insert a number", 0, 500, 0, 5)

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val, 'number', number)

st.write("Outside the form")

with st.form(key='multiple columns'):
    lcol, rcol = st.columns(2)
    
    with lcol:
        st.write("Inside the form l ")
        slider_val_l = st.slider("Form slider")
        checkbox_val_l = st.checkbox("Form checkbox")
        number_l = st.number_input("Insert a number", 0, 500, 0, 5)

    with rcol:
        st.write("Inside the form r")
        slider_val_r = st.slider("Form slider2")
        checkbox_val_r = st.checkbox("Form checkbox2")
        number_r = st.number_input("Insert a number2", 0, 500, 0, 5)

    submitted2 = st.form_submit_button("Submit2")
    if submitted2:
       st.write(number_l, number_r)