from hashlib import sha256
from os import getenv
from string import punctuation

import requests
import streamlit as st
from openai.error import InvalidRequestError, OpenAIError
from requests.exceptions import TooManyRedirects
from src.utils.agi.bard import BardChat
from src.utils.agi.chat_gpt import create_gpt_completion
from streamlit_chat import message

new_punctuation = "".join([i for i in punctuation if i not in ".,!?:'"])


def clear_chat() -> None:
    st.session_state.generated = []
    st.session_state.past = []
    st.session_state.messages = []
    st.session_state.user_text = ""


def show_chat_buttons() -> None:
    st.text_area(label=st.session_state.locale.chat_placeholder, value=st.session_state.user_text, key="user_text")
    b0, b1 = st.columns([3, 1])
    with b0, b1:
        b0.button(label=st.session_state.locale.chat_run_btn, use_container_width=True)
        b1.button(
            label=st.session_state.locale.chat_clear_btn,
            on_click=clear_chat,
            use_container_width=True,
        )


def get_balance() -> float:
    session = getenv("OPENAI_SESSION")
    if not session:
        return -1
    try:
        data = requests.get(
            "https://api.openai.com/dashboard/billing/credit_grants", headers={"Authorization": f"Bearer {session}"}
        ).json()["grants"]["data"][0]
        return (data["grant_amount"] - data["used_amount"]) / data["grant_amount"]
    except:
        return -1


def show_chat(ai_content: str, user_text: str) -> None:
    if ai_content not in st.session_state.generated:
        # store the ai content
        st.session_state.past.append(user_text)
        st.session_state.generated.append(ai_content)
    if st.session_state.generated:
        for i in range(len(st.session_state.generated)):
            user_input = st.session_state.past[i]
            ai_answer = st.session_state.generated[i]
            seed = int(sha256(user_input.encode()).hexdigest(), base=16) % 10**3
            message(user_input, is_user=True, key=str(i) + "_user", avatar_style="micah", seed=seed)
            if any(p in st.session_state.generated[i] for p in new_punctuation):
                message("", key=str(i), seed=seed)
                st.markdown(ai_answer)
            else:
                message(ai_answer, key=str(i), seed=seed)


def show_gpt_conversation() -> None:
    try:
        completion = create_gpt_completion(st.session_state.model, st.session_state.messages)
        ai_content = completion.get("choices")[0].get("message").get("content")
        st.session_state.messages.append({"role": "assistant", "content": ai_content})
        if ai_content:
            show_chat(ai_content, st.session_state.user_text)
            st.divider()
    except InvalidRequestError as err:
        if err.code == "context_length_exceeded":
            st.session_state.messages.pop(1)
            if len(st.session_state.messages) == 1:
                st.session_state.user_text = ""
            show_conversation()
        else:
            st.error(err)
    except (OpenAIError, UnboundLocalError) as err:
        st.error(err)


def show_bard_conversation() -> None:
    try:
        bard = BardChat(st.secrets.api_credentials.bard_session)
        ai_content = bard.ask(st.session_state.user_text)
        st.warning(ai_content.get("content"))
    except (TooManyRedirects, AttributeError) as err:
        st.error(err)


def show_conversation() -> None:
    if st.session_state.messages:
        st.session_state.messages.append({"role": "user", "content": st.session_state.user_text})
    else:
        ai_role = f"{st.session_state.locale.ai_role_prefix} {st.session_state.role}. {st.session_state.locale.ai_role_postfix}"  # NOQA: E501
        st.session_state.messages = [
            {"role": "system", "content": ai_role},
            {"role": "user", "content": st.session_state.user_text},
        ]
    if st.session_state.model == "bard":
        show_bard_conversation()
    else:
        show_gpt_conversation()
