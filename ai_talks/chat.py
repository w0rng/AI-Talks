from os import getenv
from pathlib import Path

import openai
import streamlit as st
from src.utils.conversation import show_chat_buttons, show_conversation
from src.utils.lang import ru

openai.api_key = getenv("API_KEY")

# --- PATH SETTINGS ---
current_dir: Path = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file: Path = current_dir / "src/styles/.css"
assets_dir: Path = current_dir / "assets"
icons_dir: Path = assets_dir / "icons"
img_dir: Path = assets_dir / "img"
tg_svg: Path = icons_dir / "tg.svg"

# --- GENERAL SETTINGS ---
PAGE_TITLE: str = "AI Talks"
PAGE_ICON: str = "🤖"
LANG_EN: str = "En"
LANG_RU: str = "Ru"
AI_MODEL_OPTIONS = [i["id"] for i in openai.Model.list().get("data")]

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

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
    c1, c2 = st.columns(2)
    with c1, c2:
        c1.selectbox(
            label=st.session_state.locale.select_placeholder1,
            key="model",
            options=AI_MODEL_OPTIONS,
            index=AI_MODEL_OPTIONS.index("gpt-3.5-turbo"),
        )
        c2.selectbox(
            label=st.session_state.locale.select_placeholder2,
            key="role",
            options=st.session_state.locale.ai_role_options,
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
