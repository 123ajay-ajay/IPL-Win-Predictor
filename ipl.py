import streamlit as st
import pickle
import pandas as pd
import os
teams = ['Sunrisers Hyderabad',
         'Mumbai Indians', 
         'Royal Challengers Bangalore',
        'Kolkata Knight Riders',
        'Kings XI Punjab',
        'Chennai Super Kings', 
        'Rajasthan Royals',
         'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))

st.title('IPL Win Predictor')


col1, col2 = st.columns(2)


with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))
selected_city = st.selectbox('Select host city',sorted(cities))

# target = st.number_input('Target')
target = st.number_input('Target', min_value=0, step=1)

col3,col4,col5 = st.columns(3)

with col3:
    # score = st.number_input('Score')
    score = st.number_input('Score', min_value=0, step=1)
with col4:
    # overs = st.number_input('overs')
    overs = st.number_input('overs', min_value=0, max_value=20, step=1)

with col5:
    # wickets = st.number_input('Wickets out')
    wickets = st.number_input('Wickets out', min_value=0, max_value=10, step=1)

if st.button('Predict Probability'):
    runs_left = target - score 
    ball_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/ball_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],
                             'city':[selected_city],'runs_left':[runs_left],'ball_left':[ball_left],
                             'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    # st.table(input_df)
    result = pipe.predict_proba(input_df)
    # st.text(result)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + " - " + str(round(win*100)) + "%")
    st.header(bowling_team + " - " + str(round(loss*100)) + "%")

    # header ke place per text bhi lihk sakte hai


