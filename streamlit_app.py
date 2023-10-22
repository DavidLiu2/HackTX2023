from collections import namedtuple
import random
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
st.session_state.text = f"Hi I'll be your purr-sonal assistant for this purchase {sound}"

if 'image' not in st.session_state:
    st.session_state.image = "tile0" + str(random.randint(10, 45)) + ".png"


def plot():
    # Parameters for the normal distribution
    mean = 0
    std_dev = 1
    sample_size = 200
    desired_percentile = 25

    if item_type == "Food :knife_fork_plate:":
        mean = 7
        std_dev = 5
    elif item_type == "Toy :teddy_bear:":
        mean = 2
        std_dev = 10
    elif item_type == "Enclosure :house:":
        mean = 100
        std_dev = 100
        desired_percentile = 40
    elif item_type == "Bed :bed:":
        mean = 20
        std_dev = 10
    elif item_type == "Cleaning :soap:":
        mean = 7
        std_dev = 3
    elif item_type == "Fish Tank :fish:":
        mean = 200
        std_dev = 100
        desired_percentile = 10
    else:
        return

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
    ax.set_xlabel('Price USD')
    ax.set_ylabel('Frequency')
    ax.set_title('Your Item Price Compared')

    fig  # 👈 Draw a Matplotlib chart

def sidebar():
    with st.sidebar:
        st.image(st.session_state.image)
        st.write(st.session_state.text)



"Feel free to add some item you want to buy below"

# Create an empty list to store form data
if 'form_data' not in st.session_state:
    st.session_state.form_data = []
if 'total_price' not in st.session_state:
    st.session_state.total_price = 0

# Define the form fields
import streamlit as st

item_type = st.radio(
    "Item Type",
    ["Food :knife_fork_plate:", "Toy :teddy_bear:", "Enclosure :house:", "Bed :bed:", "Cleaning :soap:", "Fish Tank :fish:", "Other :alien:"])
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
    st.session_state.total_price += item_price
    st.session_state.image = "tile0" + str(random.randint(10, 45)) + ".png"
    with st.sidebar:
        cat_phrases = [
            "Purr-fectly soothing sounds for relaxation.",
            "Whisker-twitching tunes for a purr-fect day.",
            "Meow-sic to your ears!",
            "Let's turn up the 'purr-sound-ality' in here.",
            "Cat-chy beats for your feline mood.",
            "Pawsitively delightful melodies.",
            "These tunes are the cat's whiskers!",
            "Purr-suasive sounds that'll whisk you away.",
            "Purronounceable hits for your playlist.",
            "A symphony of meow-sical delights."
        ]

        # Select and display a random phrase
        random_phrase = random.choice(cat_phrases)
        st.session_state.text = random_phrase
        sidebar()
        st.write("## Price Total: " + str(st.session_state.total_price))
        plot()


st.table(st.session_state.form_data)

# clear the form data
if st.button("Clear Form"):
    st.session_state.form_data = []

if st.session_state.text == f"Hi I'll be your purr-sonal assistant for this purchase {sound}":
    sidebar()