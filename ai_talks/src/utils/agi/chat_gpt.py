import logging
from os import getenv
from typing import List  # NOQA: UP035

import openai
import streamlit as st


@st.cache_data()
def create_gpt_completion(messages: List[dict], promt) -> dict:
    try:
        openai.api_key = getenv("API_KEY")
    except (KeyError, AttributeError):
        st.error(st.session_state.locale.empty_api_handler)
    logging.info(f"{messages=}")
    completion = openai.ChatCompletion.create(
        model=promt.model,
        messages=messages,
        temperature=promt.temperature,
        max_tokens=promt.max_tokens,
    )
    logging.info(f"{completion=}")
    return completion
