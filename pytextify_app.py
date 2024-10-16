import streamlit as st
st.set_page_config(layout="wide")

from cookies_file import cookies

login_page = st.Page("accounts/login.py", title="Pytextify - Log in & Sign up", icon=":material/login:")
logout_page = st.Page("accounts/logout.py", title="Log out", icon=":material/logout:")
profile_page = st.Page("accounts/profile.py", title="Profile", icon=":material/account_circle:")


dashboard = st.Page("reports/dashboard.py", title="Pytextify", icon=":material/dashboard:", default=True)
transcriptions = st.Page("reports/transcription.py", title="Transcriptions", icon=":material/description:")
chat = st.Page("reports/chat.py", title="Chats", icon=":material/chat:")

search = st.Page("tools/pyimageify.py", title="PyImageify", icon=":material/search:")
history = st.Page("tools/pydataify.py", title="PyDataify", icon=":material/history:")


if cookies.get("logged_in") == "true":
    st.session_state.logged_in = True

else: st.session_state.logged_in = False

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [profile_page, logout_page],
            "Reports": [dashboard, transcriptions, chat],
            "Tools": [search, history],
        }
    )
else: pg = st.navigation([login_page])

pg.run()