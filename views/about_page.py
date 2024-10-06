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
    if st.button("🛸 Let's go"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("About Jaidee Dietetic Recipe Generator", anchor=False)
st.write(
    """
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

