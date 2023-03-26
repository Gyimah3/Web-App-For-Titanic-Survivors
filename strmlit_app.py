# Importing required Library
import streamlit as st
import pandas as pd
import numpy as np
import os, pickle
from sklearn import preprocessing
from PIL import Image
# Setting up page configuration and directory path





st.set_page_config(page_title="Titanic Survival prediction App", page_icon="🛳️", layout="centered")
DIRPATH = os.path.dirname(os.path.realpath(__file__))


# Setting background image

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-color:black;
background-image:
radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px),
radial-gradient(rgba(255,255,255,.4), rgba(255,255,255,.1) 2px, transparent 30px);
background-size: 550px 550px, 350px 350px, 250px 250px, 150px 150px;
background-position: 0 0, 40px 60px, 130px 270px, 70px 100px;

}

</style>
'''
st.markdown(page_bg_img,unsafe_allow_html=True)



# Setting up logo
left1, left2, mid,right1, right2 = st.columns(5)
with left1:
    #image1= Image.open('https://github.com/Gyimah3/Streamlt_App-For-ML-Model-Project/blob/main/images/lo.jpg')
    st.image('data:image/jpeg;base64,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', width=400,caption=None, use_column_width=None, clamp=100, channels="RGB", output_format='JPEG')
with right1:
   # image= Image.open("images\loi.jpg")
    st.image('data:image/jpeg;base64,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',caption=None, use_column_width=None, clamp=50, channels="RGB", output_format='JPEG', width=550,)

# Setting up Sidebar
social_acc = ['Data Field Description', 'EDA', 'About App']
social_acc_nav = st.sidebar.radio('**INFORMATION SECTION**', social_acc)

if social_acc_nav == 'Data Field Description':
    st.sidebar.markdown("<h2 style='text-align: center;'> Data Field Description </h2> ", unsafe_allow_html=True)
    st.sidebar.markdown("**Pclass:** Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)")
    st.sidebar.markdown("**SibSp:** Number of Siblings/Spouses Aboard")
    st.sidebar.markdown("**Parch:** Number of Parents/Children Aboard")
    st.sidebar.markdown("**Fare:** Passenger Fare (British pound)")
    st.sidebar.markdown("**Embbarked:** Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)")
    st.sidebar.markdown("**Ticket:** Ticket Number")

elif social_acc_nav == 'EDA':
    st.sidebar.markdown("<h2 style='text-align: center;'> Exploratory Data Analysis </h2> ", unsafe_allow_html=True)
    st.sidebar.markdown('''---''')
    st.sidebar.markdown('''The exploratory data analysis of this project can be find in a Jupyter notebook from the linl below''')
    st.sidebar.markdown("[Open Notebook](https://github.com/Gyimah3/Store-Sales----Time-Series-Forecasting-Regression-project-/blob/main/Store%20Sales%20--%20Time%20Series%20Forecasting(Regression%20project).ipynb)")

elif social_acc_nav == 'About App':
    st.sidebar.markdown("<h2 style='text-align: center;'> Titanic Survival prediction App </h2> ", unsafe_allow_html=True)
    st.sidebar.markdown('''---''')
    st.sidebar.markdown("""
                        | Brief Introduction|
                        | :------------ |
                        The RMS Titanic, which was widely believed to be "unsinkable," perished on April 15, 1912, after striking an iceberg while on her first voyage. Unfortunately, there were not enough lifeboats to accommodate everyone, and 1502 out of 2224 passengers and staff perished. Even while survival required a certain amount of luck, it appears that some groups of people had a higher chance of living than others. Based on the data of the passenger, this app employs a classification model to predict whether or not a passenger would survive. """)

    st.sidebar.markdown("")
    st.sidebar.markdown("[ Visit Github Repository for more information](https://github.com/Gyimah3/Store-Sales----Time-Series-Forecasting-Regression-project-)")
    st.sidebar.markdown("Dedicated to: mom❄️ and Sis Evelyn❄️.")
    st.sidebar.markdown("")
    
# Config & Setup
## Variables of environment
DIRPATH = os.path.dirname(__file__)
ASSETSDIRPATH = os.path.join(DIRPATH, "asset")
ml_comp_pkl = os.path.join(ASSETSDIRPATH, "ml_comp.pkl")

@st.cache(allow_output_mutation=True)
def Load_ml_items(relative_path):
    "Load ML items to reuse them"
    with open(relative_path, 'rb') as file:
        loaded_items = pickle.load(file)
    return loaded_items

loaded_items=Load_ml_items(r'ml_comp.pkl')

## Loading of assets
# with open(ml_comp_pkl, "rb") as f:
#     loaded_items = pickle.load(f)
# print("INFO:    Loaded assets:", loaded_items)


pipeline_of_my_model = loaded_items["pipeline"]
num_cols = loaded_items['numeric_columns']
cat_cols = loaded_items['categorical_columns']



# Setting up variables for input data
@st.cache()
def setup(tmp_df_file):
    "Setup the required elements like files, models, global variables, etc"
    pd.DataFrame(
        dict(
            PeopleInTicket=[],
            Age=[],
            FarePerPerson=[],
            SibSp=[],
            Pclass=[],
            Fare=[],
            Parch=[],
            TicketNumber=[],
            Title=[],
            Embarked=[],
            Sex=[],
        )
    ).to_csv(tmp_df_file, index=False)

# Setting up a file to save our input data
tmp_df_file = os.path.join(DIRPATH, "tmp", "data.csv")
setup(tmp_df_file)

# setting Title for forms
st.markdown("<h2 style='text-align: center;'> Titanic Prediction </h2> ", unsafe_allow_html=True)
st.markdown("<h7 style='text-align: center;'> Fill in the details below and click on SUBMIT button to make a prediction for a specific date </h7> ", unsafe_allow_html=True)


# Creating columns for for input data(forms)
left_col,right_col = st.columns(2)#[#20,20],gap="small")

# Developing forms to collect input data
with st.form(key="information", clear_on_submit=True):
    # Setting up input data for 1st column
    left_col.markdown("**TITANIC NUMERIC DATA**")
    PeopleInTicket= left_col.number_input("People having Ticket:", min_value=0, max_value= 1000)
    Age = left_col.number_input("Age of the person:",  min_value=0, max_value= 1000)
    FarePerPerson = left_col.number_input("Fare Per one person:", min_value=0, max_value=1000)
    SibSp = left_col.number_input("Number of Siblings/Spouses Aboard:", min_value=0, max_value=100)
    Pclass=left_col.number_input("Passenger Class(1-3):",min_value=1, max_value=3)
    Parch = left_col.number_input("Number of Parents/Children Aboard:", min_value=0, max_value=100)
    Fare = left_col.number_input("Passenger Fare:",min_value=0, max_value=1000000)
    TicketNumber = left_col.number_input("Ticket Number of the person:", min_value=0, max_value=1000000)

    
     # Setting up input data for 2nd column
    right_col.markdown("**CATEGORICAL DATA**")
    Title = right_col.selectbox("Name Title", ["Mr","Mrs","Miss", "Master","FemaleChild","Royalty","Officer"])
    Embarked = right_col.radio("Port of Embarkation:", ["C", "Q", "S"])
    Sex = right_col.selectbox("Sex:", ["male", "female"])

    submitted = st.form_submit_button(label="Submit")
    
if submitted:
    # Saving input data as csv after submission
    pd.read_csv(tmp_df_file).append(
        dict(
            
                PeopleInTicket=PeopleInTicket,
                Age=Age,
                FarePerPerson=FarePerPerson,
                SibSp=SibSp,
                Pclass=Pclass,
                Fare=Fare,               Parch=Parch,
                TicketNumber=TicketNumber,
                Title=Title,
                Embarked=Embarked,
                Sex=Sex,
            ),
            ignore_index=True,
    ).to_csv(tmp_df_file, index=False)
    st.balloons()
     

    df = pd.read_csv(tmp_df_file)
    df= df.copy()
   
        
    # Making Predictions
    # Passing data to pipeline to make prediction
    pred_output = pipeline_of_my_model.predict(df)
    prob_output = np.max(pipeline_of_my_model.predict_proba(df))
    
    # Interpleting prediction output for display
    X= pred_output[-1]
    if X == 1:
        explanation = 'Passenger Survived'
    else: 
        explanation = 'Passenger did not Survive'
    output = explanation
    

    # Displaying prediction results
    st.markdown('''---''')
    st.markdown("<h4 style='text-align: center;'> Prediction Results </h4> ", unsafe_allow_html=True)
    st.success(f"Predicted Survival: {output}")
    st.success(f"Confidence Probability: {prob_output}")
    st.markdown('''---''')

    # Making expander to view all records
    expander = st.expander("See all records")
    with expander:
        df = pd.read_csv(tmp_df_file)
        df['Survived']= pred_output
        st.dataframe(df)