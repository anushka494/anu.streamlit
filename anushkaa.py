import streamlit as st

# Sample data (Replace these URLs with actual image URLs or paths)
outfits = {
    "children": {
        "5-10": {
            "girls": "https://via.placeholder.com/150?text=Girls+Outfit+5-10",
            "boys": "https://via.placeholder.com/150?text=Boys+Outfit+5-10"
        },
        "11-14": {
            "girls": "https://via.placeholder.com/150?text=Girls+Outfit+11-14",
            "boys": "https://via.placeholder.com/150?text=Boys+Outfit+11-14"
        }
    },
    "teens": {
        "15-18": {
            "girls": "https://via.placeholder.com/150?text=Girls+Outfit+15-18",
            "boys": "https://via.placeholder.com/150?text=Boys+Outfit+15-18"
        }
    },
    "adults": {
        "19-25": {
            "women": "https://via.placeholder.com/150?text=Women+Outfit+19-25",
            "men": "https://via.placeholder.com/150?text=Men+Outfit+19-25"
        },
        "26-35": {
            "women": "https://via.placeholder.com/150?text=Women+Outfit+26-35",
            "men": "https://via.placeholder.com/150?text=Men+Outfit+26-35"
        },
        "36-50": {
            "women": "https://via.placeholder.com/150?text=Women+Outfit+36-50",
            "men": "https://via.placeholder.com/150?text=Men+Outfit+36-50"
        }
    }
}

def main():
    st.title("Trendy Outfit Finder")

    age_group = st.selectbox("Select Age Group", ["5-10", "11-14", "15-18", "19-25", "26-35", "36-50"])
    gender = st.selectbox("Select Gender", ["Girls", "Boys", "Women", "Men"])

    category = None

    if age_group in ["5-10", "11-14"]:
        category = "children"
    elif age_group in ["15-18"]:
        category = "teens"
    elif age_group in ["19-25", "26-35", "36-50"]:
        category = "adults"

    if category:
        if gender in ["Girls", "Boys"]:
            outfit_key = outfits[category].get(age_group, {}).get(gender.lower())
        else:
            outfit_key = outfits[category].get(age_group, {}).get(gender.lower())

        if outfit_key:
            st.image(outfit_key, caption=f"{gender} Outfit for {age_group}", use_column_width=True)
        else:
            st.write("No outfit available for this selection.")

if __name__ == "__main__":
    main()
