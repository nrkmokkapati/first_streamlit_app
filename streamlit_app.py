import streamlit

streamlit.title('My parents new healthy diner')
streamlit.title('🍞 Breakfast menu')
streamlit.title('🥣 Omega3 and Oatmeal buleberry')
streamlit.title('🥗 🥑Kales Spinach and Rocket Smoothie')
streamlit.title('🐔 Hard Boiled Free Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
