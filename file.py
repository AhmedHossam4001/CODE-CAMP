# 1. Importing extensions
import streamlit as st
import pandas as pd

# 2. Check Authentication
# if not st.session_state.get('logged_in', False):
#     st.warning('⚠️ Please sign in from the navbar to access the menu!')
#     st.stop()

# 3. Main menu interface   
st.title('Welcome to PizzaHub🍕', text_alignment='center')
st.success(f'Hello {st.session_state.get("name", "Customer")}, choose your order!')

# Adding menu items with prices
menu_pizza = {
    'Chicken': {'Small': 180, 'Medium': 250, 'Large': 320},
    'Margerita': {'Small': 150, 'Medium': 210, 'Large': 270}, 
    'Pepperoni': {'Small': 200, 'Medium': 280, 'Large': 350},
    'Burger': {'Small': 220, 'Medium': 320, 'Large': 400}
}
menu_pasta = {
    'Alfredo': 180,
    'Bolognese': 200,
    'Pesto': 190
}
menu_drinks = {
    'Cola': 30,
    'Sprite': 30,
    'Orange Juice': 45,
    'Water': 15
}

pizza_tab, pasta_tab, drinks_tab = st.tabs(
    ['Italian Pizza🍕', 'Italian Pasta🍝', 'Soft Drinks🥤']
)

order_items = []                                 
0