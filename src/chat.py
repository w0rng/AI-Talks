from os import getenv
from pathlib import Path

import openai
import streamlit as st
from utils.conversation import get_balance, get_promts, show_chat_buttons, show_conversation
from utils.lang import ru

openai.api_key = getenv("API_KEY")

# --- PATH SETTINGS ---
current_dir: Path = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file: Path = current_dir / "src/styles/.css"
# --- GENERAL SETTINGS ---
AI_MODEL_OPTIONS = [i["id"] for i in openai.Model.list().get("data")]

st.set_page_config(page_title=ru.page_title, page_icon=ru.page_icon)

# --- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# Storing The Context
if "locale" not in st.session_state:
    st.session_state.locale = ru
if "generated" not in st.session_state:
    st.session_state.generated = []
if "past" not in st.session_state:
    st.session_state.past = []
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_text" not in st.session_state:
    st.session_state.user_text = ""


def main() -> None:
    balance = get_balance()
    if balance != -1:
        l, p = st.columns([1, 4])
        with l, p:
            l.text(ru.balance_handler + f" {balance:.2f}/1 : ")
            p.progress(balance)
    c1, c2 = st.columns(2)
    with c1, c2:
        c1.selectbox(
            label=st.session_state.locale.select_placeholder1,
            key="model",
            options=AI_MODEL_OPTIONS,
            index=AI_MODEL_OPTIONS.index(ru.default_model),
        )
        c2.selectbox(
            label=st.session_state.locale.select_placeholder2,
            key="role",
            options=get_promts().keys(),
        )

    if st.session_state.user_text:
        show_conversation()
        st.session_state.user_text = ""
    show_chat_buttons()


def run_agi():
    st.session_state.locale = ru
    st.markdown(
        f"<h1 style='text-align: center;'>{st.session_state.locale.title}</h1>",
        unsafe_allow_html=True,
    )
    main()


if __name__ == "__main__":
    run_agi()
