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

    snatch_weakness_list = [
        'no_weakness',
        'oh_stability',
        'incomplete_pull',
        'barbell_hip_swing',
        'shoulders_behind_barbell',
        'foot_stability',
        'slow_under_barbell',
        ]
    
    clean_weakness_list = [
        'no_weakness',
        'incomplete_pull',
        'barbell_hip_swing',
        'shoulders_behind_barbell',
        'foot_stability',
        'slow_elbow_rotation',
        'barbell_falls_on_you'
        ]
    
    jerk_weakness_list = [
        'no_weakness',
        'incomplete_drive',
        'skewed_drive',
        'unequal_split',
        'slow_under_barbell'
    ]



 
    snatch_weakness = st.selectbox(language['snatch_weakness'], snatch_weakness_list, 
                                   format_func = lambda x: language['sw_set'][x])
    clean_weakness = st.selectbox(language['clean_weakness'], clean_weakness_list,
                                   format_func = lambda x: language['cw_set'][x])
    jerk_weakness = st.selectbox(language['jerk_weakness'], jerk_weakness_list,
                                 format_func = lambda x: language['jw_set'][x])

    st.subheader(language['general_setup_header'])

    gender_weight_lang = st.selectbox(language['personal_info'], language['gender_weight_options'])

    cycle_length = st.selectbox(language['cycle_length'], language['cycles_lengths'])
    training_frequency = st.selectbox(language['training_frequency'], language['frequencies'])




    submitted = st.form_submit_button(language['calculate'])

if submitted:
    st.write(snatch_weakness)
    st.write(clean_weakness)
    st.write(jerk_weakness)
    st.write(back_squat_max + split_jerk_max)