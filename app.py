import streamlit as st
from streamlit.elements.lib.layout_utils import WidthWithoutContent

st.set_page_config(page_title="Can You Hear It?", layout="centered")

st.markdown("<h1>CAN YOU HEAR IT?</h1>", text_alignment="center", unsafe_allow_html=True)

if "state" not in st.session_state:
    st.session_state.state = {"YES": False, "NO": False}

def click(btn):
    st.session_state.state[btn] = True
    other = "NO" if btn == "YES" else "YES"
    st.session_state.state[other] = False

col1, col2 = st.columns([1,1])

with col1:
    st.button("YES", on_click=lambda: click("YES"), width="stretch")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.button("NO", on_click=lambda: click("NO"), width="stretch")
    st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.state["YES"]:
    st.success("You chose YES!")
    st.link_button(
        "LET'S GO!!!!",
        "https://www.youtube.com/watch?v=WJitbK6CSTM&list=RDWJitbK6CSTM&start_radio=1"
    )

elif st.session_state.state["NO"]:
    st.error("You chose NO!")
    st.link_button(
        "ah hell naw!!",
        "https://www.youtube.com/watch?v=Xn4yAbA9cZw"
    )
