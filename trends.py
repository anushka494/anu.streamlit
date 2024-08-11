import streamlit as st
import pandas as pd

# Sample Data (Replace with real data or integrate with a database)
outfits = {
    "Children": {
        "5-10": [
            {"name": "Kids T-Shirt", "price": 15.00, "image": "https://via.placeholder.com/150?text=Kids+T-Shirt"},
            {"name": "Kids Jeans", "price": 20.00, "image": "https://via.placeholder.com/150?text=Kids+Jeans"}
        ],
        "11-14": [
            {"name": "Teen T-Shirt", "price": 18.00, "image": "https://via.placeholder.com/150?text=Teen+T-Shirt"},
            {"name": "Teen Shorts", "price": 22.00, "image": "https://via.placeholder.com/150?text=Teen+Shorts"}
        ]
    },
    "Boys": {
        "15-18": [
            {"name": "Boy's Hoodie", "price": 30.00, "image": "https://via.placeholder.com/150?text=Boy%27s+Hoodie"},
            {"name": "Boy's Jacket", "price": 45.00, "image": "https://via.placeholder.com/150?text=Boy%27s+Jacket"}
        ]
    },
    "Girls": {
        "15-18": [
            {"name": "Girl's Dress", "price": 35.00, "image": "https://via.placeholder.com/150?text=Girl%27s+Dress"},
            {"name": "Girl's Skirt", "price": 28.00, "image": "https://via.placeholder.com/150?text=Girl%27s+Skirt"}
        ]
    },
    "Men": {
        "19-25": [
            {"name": "Men's Suit", "price": 150.00, "image": "https://via.placeholder.com/150?text=Men%27s+Suit"},
            {"name": "Men's Jeans", "price": 50.00, "image": "https://via.placeholder.com/150?text=Men%27s+Jeans"}
        ],
        "26-35": [
            {"name": "Men's Blazer", "price": 120.00, "image": "https://via.placeholder.com/150?text=Men%27s+Blazer"},
            {"name": "Men's Chinos", "price": 60.00, "image": "https://via.placeholder.com/150?text=Men%27s+Chinos"}
        ]
    },
    "Women": {
        "19-25": [
            {"name": "Women's Dress", "price": 80.00, "image": "https://via.placeholder.com/150?text=Women%27s+Dress"},
            {"name": "Women's Top", "price": 35.00, "image": "https://via.placeholder.com/150?text=Women%27s+Top"}
        ],
        "26-35": [
            {"name": "Women's Coat", "price": 120.00, "image": "https://via.placeholder.com/150?text=Women%27s+Coat"},
            {"name": "Women's Skirt", "price": 45.00, "image": "https://via.placeholder.com/150?text=Women%27s+Skirt"}
        ]
    }
}

def main():
    st.title("Trendy Outfit Store")

    st.sidebar.header("Order Details")

    # Selection of Age Group and Gender
    gender = st.sidebar.selectbox("Select Gender", ["Children", "Boys", "Girls", "Men", "Women"])
    age_group = st.sidebar.selectbox("Select Age Group", list(outfits[gender].keys()))

    # Display Items Based on Selection
    st.subheader(f"Available Outfits for {gender} ({age_group})")
    selected_items = outfits[gender][age_group]

    item_options = [item["name"] for item in selected_items]
    selected_item_name = st.sidebar.selectbox("Select Item", item_options)

    # Get details of the selected item
    selected_item = next(item for item in selected_items if item["name"] == selected_item_name)
    st.image(selected_item["image"], caption=selected_item["name"], use_column_width=True)
    st.write(f"**Price:** ${selected_item['price']:.2f}")

    quantity = st.sidebar.number_input("Quantity", min_value=1, value=1)
    total_price = selected_item["price"] * quantity

    st.write(f"**Total Price:** ${total_price:.2f}")

    # Address Input
    address = st.text_area("Enter Delivery Address")
    
    # Review Section
    review = st.text_area("Leave a Review (optional)")

    # Payment Section (Mock)
    if st.button("Proceed to Payment"):
        if address:
            st.write("Thank you for your order!")
            st.write(f"Your total amount to be paid is: ${total_price:.2f}")
            st.write(f"**Delivery Address:** {address}")
            if review:
                st.write(f"**Review:** {review}")
            st.write("Your order will be processed and delivered to the address provided.")
        else:
            st.write("Please enter a delivery address before proceeding.")

if __name__ == "__main__":
    main()
