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
    ["Food :knife_fork_plate:", "Toy :teddy_bear:", "Enclosure :house:", "Bed :bed:", "Cleaning :soap:", "Fish Tank :fish:"])
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



# Parameters for the normal distribution
mean = 0
std_dev = 1
sample_size = 200
desired_percentile = 25

if item_type == "Food :knife_fork_plate:":
    mean = 10
    std_dev = 3
if item_type == "Toy :teddy_bear:":
    mean = 2
    std_dev = 10
if item_type == "Enclosure :house:":
    mean = 100
    std_dev = 100
    desired_percentile = 40
if item_type == "Bed :bed:":
    mean = 20
    std_dev = 10
if item_type == "Cleaning :soap:":
    mean = 7
    std_dev = 3
if item_type == "Fish Tank :fish:":
    mean = 200
    std_dev = 100
    desired_percentile = 10

# Generate a normal distribution
normal_data = np.random.normal(mean, std_dev, sample_size)

# Calculate the threshold value for the desired percentile
threshold = np.percentile(normal_data, desired_percentile)

if threshold < 0:
    threshold = 1

# Filter the data to retain values above the threshold
filtered_data = normal_data[normal_data >= threshold]


fig, ax = plt.subplots()
ax.hist(filtered_data, bins=20)

ax.axvline(x=item_price, color='red', linestyle='--', label=f'Item Price: {item_price}')
ax.legend()

# Customize the plot as needed (e.g., labels, titles, etc.)
ax.set_xlabel('Price')
ax.set_ylabel('Frequency')
ax.set_title('Your Item Price Compared')

fig  # 👈 Draw a Matplotlib chart

