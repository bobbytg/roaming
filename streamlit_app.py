import streamlit as st
import logging
from datetime import date, timedelta
import google.generativeai as genai

# configure logging
logging.basicConfig(level=logging.INFO)

# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []  # Initialize chat history

# Capture Gemini API Key 
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password") 

# Initialize the Gemini Model 
model = None
if gemini_api_key: 
    try: 
        # Configure Gemini with the provided API Key 
        genai.configure(api_key=gemini_api_key) 
        model = genai.GenerativeModel("gemini-pro") 
        st.success("Gemini API Key successfully configured.") 
    except Exception as e: 
        st.error(f"An error occurred while setting up the Gemini model: {e}")

# Streamlit UI elements
st.header("Jaidee Dietetic Recipe Generator", divider="gray")

cuisine = st.selectbox(
    "What cuisine do you desire?",
    ("American", "Chinese", "French", "Indian", "Italian", "Japanese", "Mexican", "Turkish"),
    index=None,
    placeholder="Select your desired cuisine."
)

dietary_preference = st.selectbox(
    "Do you have any dietary preferences?",
    ("Diabetese", "Gluten free", "Halal", "Keto", "Kosher", "Lactose Intolerance", "Paleo", "Vegan", "Vegetarian", "None"),
    index=None,
    placeholder="Select your desired dietary preference."
)

allergy = st.text_input(
    "Enter your food allergy:  \n\n", key="allergy", value="peanuts"
)

ingredient_1 = st.text_input(
    "Enter your first ingredient:  \n\n", key="ingredient_1", value="ahi tuna"
)

ingredient_2 = st.text_input(
    "Enter your second ingredient:  \n\n", key="ingredient_2", value="chicken breast"
)

ingredient_3 = st.text_input(
    "Enter your third ingredient:  \n\n", key="ingredient_3", value="tofu"
)

drink = st.radio(
    "What is your drink preference?",
    ["Green Tea","Mint Tea", "Smoothies", "Coconut Water","None"],
    index=None,
)

language = st.selectbox(
    "What language of recipe do you desire?",
    ("English", "Spanish", "Chinese", "French", "Japanese", "Thai"),
    index=None,
    placeholder="Select your desired language of recipe."
)


# Prompt creation
prompt = f"""Hello there! I am Jaidee, the Dietitian and Chef. \n
From your request healthty {cuisine} recipes and want {dietary_preference} meals. \n
And don't include recipes that use ingredients with your {allergy} allergy. \n
You have {ingredient_1}, \n
{ingredient_2}, \n
and {ingredient_3} \n
in your kitchen and other ingredients. \n
From your drink preference is {drink} \n
Below is meal recommendations from your ingredients.
For each recommendation include preparation instructions,
time to prepare
and the recipe title at the beginning of the response.
Then include the wine pairing for each recommendation.
At the end of the recommendation provide the calories associated with the meal
and the detalied nutritional facts. \n
Please provide the recipe in {language}.
"""

# Button to generate recipes
generate_t2t = st.button("Generate my recipes.", key="generate_t2t")

# Display previous chat history using st.chat_message
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

# Generating the recipe
if generate_t2t and prompt:
    st.session_state.chat_history.append(("user", prompt))
    st.chat_message("user").markdown(prompt)
    
    # Use Gemini AI to generate a bot response 
    if model: 
        try: 
            # Use Gemini to generate a response for the recipe prompt
            response = model.generate_content(prompt)
            bot_response = response.text
            st.session_state.chat_history.append(("assistant", bot_response)) 
            st.chat_message("assistant").markdown(bot_response) 
        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")