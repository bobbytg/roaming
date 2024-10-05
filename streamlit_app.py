import streamlit as st
import logging
from datetime import date, timedelta
import requests  # Use for API calls to Gemini AI (replace with actual Gemini API endpoint)

# configure logging
logging.basicConfig(level=logging.INFO)

# Function to call Gemini API
def get_gemini_response(prompt, config):
    # Placeholder for the actual Gemini API call.
    # You would replace this with your real API request
    url = "https://api.gemini-ai.com/v1/generate"  # Replace with actual Gemini API URL
    headers = {"Authorization": "Bearer YOUR_API_KEY"}  # Replace with your API key
    data = {
        "prompt": prompt,
        "temperature": config['temperature'],
        "max_output_tokens": config['max_output_tokens']
    }
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("text", "")
    else:
        st.error("Error calling Gemini API.")
        return ""

# Streamlit UI elements
st.header("Gemini AI Recipe Generator", divider="gray")

cuisine = st.selectbox(
    "What cuisine do you desire?",
    ("American", "Chinese", "French", "Indian", "Italian", "Japanese", "Mexican", "Turkish"),
    index=None,
    placeholder="Select your desired cuisine."
)

dietary_preference = st.selectbox(
    "Do you have any dietary preferences?",
    ("Diabetese", "Glueten free", "Halal", "Keto", "Kosher", "Lactose Intolerance", "Paleo", "Vegan", "Vegetarian", "None"),
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

wine = st.radio(
    "What is your customer's wine preference?",
    ["Red", "White", "None"],
    index=None,
)

# Prompt creation
prompt = f"""I am a Chef.  I need to create {cuisine} \n
recipes for customers who want {dietary_preference} meals. \n
However, don't include recipes that use ingredients with the customer's {allergy} allergy. \n
I have {ingredient_1}, \n
{ingredient_2}, \n
and {ingredient_3} \n
in my kitchen and other ingredients. \n
The customer's wine preference is {wine} \n
Please provide some meal recommendations.
For each recommendation include preparation instructions,
time to prepare
and the recipe title at the beginning of the response.
Then include the wine pairing for each recommendation.
At the end of the recommendation provide the calories associated with the meal
and the nutritional facts.
"""

# Configuration for generation
config = {
    "temperature": 0.8,
    "max_output_tokens": 2048,
}

# Button to generate recipes
generate_t2t = st.button("Generate my recipes.", key="generate_t2t")
if generate_t2t and prompt:
    with st.spinner("Generating your recipes using Gemini..."):
        response = get_gemini_response(prompt, config)
        if response:
            st.write("Your recipes:")
            st.write(response)
            logging.info(response)
        else:
            st.error("Failed to retrieve recipes from Gemini API.")
