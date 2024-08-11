import streamlit as st

# Define the menu data
menu = {
    'Coffee': {
        'Espresso': 3.00,
        'Latte': 4.00,
        'Cappuccino': 4.50
    },
    'Snacks': {
        'French Fries': 2.50,
        'Onion Rings': 3.00,
        'Nachos': 4.00
    },
    'Main Course': {
        'Cheeseburger': 8.00,
        'Grilled Chicken': 10.00,
        'Vegetarian Pasta': 9.00
    },
    'Dessert': {
        'Chocolate Cake': 5.00,
        'Ice Cream': 3.50,
        'Fruit Salad': 4.00
    }
}

# Streamlit app
st.title('Restaurant Menu')

for category, items in menu.items():
    st.header(category)
    for item, price in items.items():
        st.write(f"{item}: ${price:.2f}")

