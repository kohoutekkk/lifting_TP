import streamlit as st
import json
import os

st.set_page_config(layout="wide")

with open(os.path.join(os.getcwd(),'src/cze.json'), 'r') as f:
    language = json.load(f)

st.header(language['title'])

st.subheader(language['form_header'])

with st.form(key='lifter'):
    st.subheader(language['rm_header'])

    snatch, clean, jerk, squat = st.columns(4)

    with snatch:
        squat_snatch_max = st.number_input(f'{language["squat_snatch"]} (kg)', None, 500, 0, 5)
        power_snatch_max = st.number_input(f'{language["power_snatch"]} (kg)', None, 500, 0, 5)
        snatch_deadlift_max = st.number_input(f'{language["snatch_deadlift"]} (kg)', None, 500, 0, 5)
       
    
    with clean:
        clean_and_jerk_max = st.number_input(f'{language["clean_and_jerk"]} (kg)', None, 500, 0, 5)
        squat_clean_max = st.number_input(f'{language["squat_clean"]} (kg)', None, 500, 0, 5)
        power_clean_max = st.number_input(f'{language["power_clean"]} (kg)', None, 500, 0, 5)
        clean_deadlift_max = st.number_input(f'{language["clean_deadlift"]} (kg)', None, 500, 0, 5)
    
    with jerk:
        split_jerk_max = st.number_input(f'{language["split_jerk"]} (kg)', None, 500, 0, 5)
        power_jerk_max = st.number_input(f'{language["power_jerk"]} (kg)', None, 500, 0, 5)
        push_jerk_max = st.number_input(f'{language["push_jerk"]} (kg)', None, 500, 0, 5)
    
    with squat:
        back_squat_max = st.number_input(f'{language["back_squat"]} (kg)', None, 500, 0, 5) 
        front_sqat_max = st.number_input(f'{language["front_squat"]} (kg)', None, 500, 0, 5) 
        overhed_squat_max = st.number_input(f'{language["overhead_squat"]} (kg)', None, 500, 0, 5) 

    st.subheader(language['weakness_header'])

    snatch_weakness = st.selectbox(language['snatch_weakness'], language['sw_set'])
    clean_weakness = st.selectbox(language['clean_weakness'], language['cw_set'])
    jerk_weakness = st.selectbox(language['jerk_weakness'], language['jw_set'])

    st.subheader(language['general_setup_header'])

    gender_weight_lang = st.selectbox(language['personal_info'], language['gender_weight_options'])

    cycle_length = st.selectbox(language['cycle_length'], language['cycles'])
    training_frequency = st.selectbox(language['training_frequency'], language['frequencies'])




    submitted = st.form_submit_button(language['calculate'])

if submitted:
    st.write(back_squat_max + split_jerk_max)