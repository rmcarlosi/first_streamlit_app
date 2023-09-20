import streamlit

streamlit.title ("My parents new healthy dinner")
streamlit.header('Breakfast menu')
streamlit.text('🥣Omega 3 and blueberries oatmeal')
streamlit.text('🥗Kale, spinach and rocket smoothie')
streamlit.text('🐔Hard Boiled free range egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),["Avocado","Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(fruits_to_show)
# h

streamlit.header("Fruityvice Fruit Advice!")


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
"""streamlit.text(fruityvice_response.json())"""



# write your own comment -what does the next line do? 
# This line takes the converts the respond in json format an then into a pandas object.

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
# and then uses a method from pandas to convertid in a data frame.

