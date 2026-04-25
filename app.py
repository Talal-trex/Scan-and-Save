import streamlit as st
from PIL import Image

st.set_page_config(page_title="Scan & Save", layout="centered")

st.title("🍏 Scan & Save")
st.write("Reduce food waste with smart freshness detection")

uploaded_file = st.file_uploader("Upload food image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Food", use_column_width=True)

    st.subheader("Quick Info")

    food_type = st.selectbox(
        "What type of food is this?",
        ["Fruit", "Vegetable", "Dairy", "Meat", "Cooked Food"]
    )

    storage = st.selectbox(
        "How was it stored?",
        ["Fridge", "Room Temperature", "Freezer"]
    )

    days = st.slider("How many days since you got it?", 0, 14)

    def check_freshness(food, storage, days):
        base_days = {
            "Fruit": 7,
            "Vegetable": 5,
            "Dairy": 4,
            "Meat": 3,
            "Cooked Food": 2
        }

        bonus = 0
        if storage == "Fridge":
            bonus = 2
        elif storage == "Freezer":
            bonus = 5

        max_days = base_days[food] + bonus

        if days < max_days * 0.6:
            return "Fresh ✅", max_days - days
        elif days < max_days:
            return "Eat Soon ⚠️", max_days - days
        else:
            return "Not Safe ❌", 0

    status, remaining = check_freshness(food_type, storage, days)

    st.subheader("Result")

    if "Fresh" in status:
        st.success(status)
    elif "Eat Soon" in status:
        st.warning(status)
    else:
        st.error(status)

    if remaining > 0:
        st.write(f"Estimated time left: {remaining} days")
    else:
        st.write("Do not consume")

    st.progress(min((14 - days) / 14, 1.0))

    st.subheader("Smart Suggestion")

    suggestions = {
        "Fruit": "Make a smoothie or fruit salad 🍓",
        "Vegetable": "Cook a stir fry or soup 🥦",
        "Dairy": "Use it in pancakes or sauces 🥛",
        "Meat": "Cook thoroughly in a dish 🍗",
        "Cooked Food": "Reheat properly before eating 🍲"
    }

    st.info(suggestions[food_type])

    st.subheader("Impact")

    st.write("🌍 You helped reduce food waste and save resources!")