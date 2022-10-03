import snowflake.connector
import streamlit
import requests
import pandas
from urllib.error import URLError


streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect('Pick some fruits' , list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]



streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice= streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    streamlit.text(fruityvice_response.json())
except URLError as e:
  streamlit.error()



# write your own comment -what does the next line do? 

# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
fruit_choice2 = streamlit.text_input('What fruit would you like information about?','Now')
streamlit.write('The user entered now', fruit_choice2)



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values('from streamlit')")
my_data_row = my_cur.fetchall()
streamlit.header("LISTA")
streamlit.dataframe(my_data_row)
streamlit.text(my_data_row)
