from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

"""
# Welcome to Pet Budget Simulator!

Whether you are expecting a new fluffy friend or just want to compare prices we're here to help :)

First of all, tell me a little more about your pet
"""

# This will appear above everything written in the form.
sound = st.selectbox('Your pet sounds like...', ['meow','woof','squeak','tweet', 'blub', 'pika'])

"Feel free to add some item you want to buy below"

# Create an empty list to store form data
if 'form_data' not in st.session_state:
    st.session_state.form_data = []

# Define the form fields
import streamlit as st

item_type = st.radio(
    "Item Type",
    ["Food :knife_fork_plate:", "Toy :teddy_bear:", "Enclosure :house: ", "Bed :bed:", "Cleaning :soap:", "Fish Tank :fish:"])
item_quantity = st.number_input("Quantity", min_value=1)
item_price = st.number_input("Price", min_value=0.01)

# Define a button to add an item to the list
if st.button("Add Item"):
    # Create a dictionary to store the item data
    item = {
        "Item Type": item_type,
        "Quantity": item_quantity,
        "Price": item_price
    }
    # Append the item to the list
    st.session_state.form_data.append(item)

st.table(st.session_state.form_data)

# Display the list of items
if st.session_state.form_data:
    st.write("Items Added:")
    for i, item in enumerate(st.session_state.form_data):
        st.write(f"Item {i + 1}: Name - {item['Item Type']}, Quantity - {item['Quantity']}, Price - {item['Price']}")

# Optionally, you can choose to clear the form data
if st.button("Clear Form"):
    st.session_state.form_data = []




arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart

