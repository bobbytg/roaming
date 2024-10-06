import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./views/jaidee.png", width=230)

with col2:
    st.title("Jaidee AI Apps", anchor=False)
    st.write(
        "🥘Jaidee Dietetic Recipe Generator"
    )
    st.write("🛸 Let's go")



# --- About ---
st.write("\n")
st.subheader("About Jaidee Dietetic Recipe Generator", anchor=False)
st.write(
    """
 The JAIDEE Recipe Generator is an intelligent, interactive web application 
 designed to generate personalized, creative, and user-friendly recipes tailored to individual preferences, 
 dietary needs and more. 

 Using Streamlit for its sleek user interface and Gemini AI for powerful natural language processing, 
 this app takes culinary experiences to the next level by offering recipe suggestions 
 based on a variety of input factors, including ingredients.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("User Interaction Flow", anchor=False)
st.write(
    """
1. User Input: Users provide their preferences (cuisine, ingredients, dietary preferences, etc.) 
   using intuitive dropdowns, text inputs, and buttons.

2. AI Recipe Generation: Based on the input, a detailed prompt is constructed and sent to Gemini AI,
   which generates a customized recipe in short time.

3. Display Recipe: The app displays the recipe along with additional features like preparation time, 
   cooking instructions, wine pairing, and nutritional information.

4. Chat Interface: Users can interact with the AI in a conversational way, asking for clarification, 
   additional recipes, or substitutions.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("POWERED BY MADT", anchor=False)
st.write(
    """🚀
    """
)