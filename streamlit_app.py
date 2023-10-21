from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

"""
# Welcome to Pet Financer!

Whether you are expecting a new fluffy friend or just want to compare prices we're here to help :)

First of all, tell me a little more about your pet
"""

# This will appear above everything written in the form.
sound = st.selectbox('Your pet sounds like...', ['meow','woof','squeak','tweet', 'blub'])

"Feel free to add some item you want to buy below"

# Create an empty list to store form data
if 'form_data' not in st.session_state:
    st.session_state.form_data = []

# Define the form fields
import streamlit as st

item_type = st.radio(
    "Item Type",
    ["Food :knife_fork_plate:", "Toy :teddy_bear:", "Enclosure :house: ", "Bed :bed:", "Cleaning :soap:"])
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


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
