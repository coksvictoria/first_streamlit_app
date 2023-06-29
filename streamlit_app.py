import streamlit
import pandas as pd
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title("Title Name")

streamlit.header('header 1')
streamlit.text('🥣 Text 1')
streamlit.text('🥗 Text 2')
streamlit.text('🥑 Text 3')

streamlit.text('🥑 Text 4')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

##display the table on the page
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(fruit_choice):
    fruitvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    # take the json version of the response and normalize it
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('what fruit you like?','kiwi')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information.")
  else:
    r=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(r)

except URLError as e:
  streamlit.error()

# streamlit.write('The user entered', fruit_choice)


##do not run anything past here while we troubleshoot
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_row)

add_my_fruit=streamlit.text_input("what fruit would like to eat?")

streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('from streamlit')")
