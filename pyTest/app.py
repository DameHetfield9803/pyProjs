import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("This is to run a few of my Python files. \n")

st.text("It is a web app to explore some of the things I do in my own free time using Python. \n")

st.markdown("1. Earthquake Data Explorer \n")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
    st.header('Data Statistics')
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())
    
    st.header('Data Header')
    st.write(df.head())

    fig,ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y =df['Mag'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)

else:
    print("No file uploaded! Please upload a file. \n")
