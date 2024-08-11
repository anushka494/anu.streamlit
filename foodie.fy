import streamlit as st
import pandas as pd

# Sample Data (Replace with real data or integrate a database)
items = {
    "Coffees": [
        {"name": "Espresso", "price": 3.00},
        {"name": "Latte", "price": 4.00},
        {"name": "Cappuccino", "price": 4.50},
    ],
    "Snacks": [
        {"name": "Chips", "price": 1.50},
        {"name": "Nuts", "price": 2.00},
        {"name": "Cookies", "price": 2.50},
    ],
    "Veg": [
        {"name": "Veg Burger", "price": 5.00},
        {"name": "Veg Pasta", "price": 6.00},
    ],
    "Non-Veg": [
        {"name": "Chicken Sandwich", "price": 6.50},
        {"name": "Beef Steak", "price": 8.00},
    ],
    "Main Course": [
        {"name": "Spaghetti Bolognese", "price": 7.50},
        {"name": "Chicken Alfredo", "price": 8.50},
    ],
    "Desserts": [
        {"name": "Cheesecake", "price": 4.00},
        {"name": "Brownie", "price": 3.50},
    ]
}

def main():
    st.title("Food & Drink Ordering System")

    st.sidebar.header("Order Details")

    # Selection of Category
    category = st.sidebar.selectbox("Select Category", list(items.keys()))
    
    # Display Items Based on Category
    st.subheader(f"Available {category}")
    selected_items = items[category]

    item_options = [item["name"] for item in selected_items]
    selected_item = st.sidebar.selectbox("Select Item", item_options)
    
    # Get price of the selected item
    item_price = next(item["price"] for item in selected_items if item["name"] == selected_item)
    
    quantity = st.sidebar.number_input("Quantity", min_value=1, value=1)
    total_price = item_price * quantity
    
    st.write(f"**Selected Item:** {selected_item}")
    st.write(f"**Price per Item:** ${item_price:.2f}")
    st.write(f"**Quantity:** {quantity}")
    st.write(f"**Total Price:** ${total_price:.2f}")

    # Address Input
    address = st.text_area("Enter Delivery Address")
    if address:
        st.write(f"**Delivery Address:** {address}")

    # Payment Section (Mock)
    if st.button("Proceed to Payment"):
        if address:
            st.write("Thank you for your order!")
            st.write(f"Your total amount to be paid is: ${total_price:.2f}")
            st.write("Your order will be processed and delivered to the address provided.")
        else:
            st.write("Please enter a delivery address before proceeding.")

if __name__ == "__main__":
    main()
