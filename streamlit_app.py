import streamlit
import pandas as pd

streamlit.title("Title Name")

streamlit.header('header 1')
streamlit.text('🥣 Text 1')
streamlit.text('🥗 Text 2')
streamlit.text('🥑 Text 3')


streamlit.dataframe(my_fruit_list)
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
