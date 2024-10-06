import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_page.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
jaidee_page = st.Page(
    "views/jaidee.py",
    title="Jaidee AI Apps",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [jaidee_page]
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("views/jaidee.png")
st.sidebar.markdown("Made with ❤️ by [Bobby]")


# --- RUN NAVIGATION ---
pg.run()