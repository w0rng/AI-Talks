from dataclasses import dataclass
from typing import List  # NOQA: UP035


@dataclass
class Locale:
    ai_role_options: List[str]
    ai_role_prefix: str
    ai_role_postfix: str
    title: str
    language: str
    lang_code: str
    donates: str
    donates1: str
    donates2: str
    chat_placeholder: str
    chat_run_btn: str
    chat_clear_btn: str
    chat_save_btn: str
    speak_btn: str
    input_kind: str
    input_kind_1: str
    input_kind_2: str
    select_placeholder1: str
    select_placeholder2: str
    select_placeholder3: str
    radio_placeholder: str
    radio_text1: str
    radio_text2: str
    stt_placeholder: str
    footer_title: str
    footer_option0: str
    footer_option1: str
    footer_option2: str
    footer_chat: str
    footer_channel: str
    responsibility_denial: str
    donates_info: str
    empty_api_handler: str


AI_ROLE_OPTIONS_RU = [
    "ассистент, который готов помочь",
    "ассистент программиста",
    "рецензент кода программиста",
    "эксперт по улучшению текста",
    "эксперт по кинематографу",
    "эксперт в области спорта",
    "эксперт в онлайн-играх",
    "эксперт по рецептам блюд",
    "эксперт по английской грамматике",
    "эксперт по русской грамматике",
    "дружелюбный и полезный помощник преподавателя",
    "лаконичный помощник",
    "полезный помощник, следующий шаблонам",
    "переводчик корпоративного жаргона на простой русский",
]

ru = Locale(
    ai_role_options=AI_ROLE_OPTIONS_RU,
    ai_role_prefix="Вы девушка",
    ai_role_postfix="Отвечай максимально лаконично.",
    title="Разговорчики с ИИ",
    language="Russian",
    lang_code="ru",
    donates="Поддержать Проект",
    donates1="Россия",
    donates2="Остальной Мир",
    chat_placeholder="Начните Вашу Беседу с ИИ:",
    chat_run_btn="Спросить",
    chat_clear_btn="Очистить",
    chat_save_btn="Сохранить",
    speak_btn="Нажмите и Говорите",
    input_kind="Вид ввода",
    input_kind_1="Текст",
    input_kind_2="Голос [тестовый режим]",
    select_placeholder1="Выберите Модель",
    select_placeholder2="Выберите Роль",
    select_placeholder3="Создайте Роль",
    radio_placeholder="Взаимодествие с Ролью",
    radio_text1="Выбрать",
    radio_text2="Создать",
    stt_placeholder="Чтобы Услышать ИИ Нажми Кнопку Проигрывателя",
    footer_title="Поддержка и Обратная Связь",
    footer_option0="Чат",
    footer_option1="Инфо",
    footer_option2="Донаты",
    footer_chat="Чат Разговорчики с ИИ",
    footer_channel="Канал Разговорчики с ИИ",
    responsibility_denial="""
        `Разговорчики с ИИ` использует API `Open AI` для взаимодействия с `ChatGPT`, ИИ, генерирующим информацию.
        Пожалуйста, учтите, что ответы нейронной сети могут быть недостоверными, неточными или нерелевантными.
        Мы не несём ответственности за любые последствия,
        связанные с использованием или доверием к информации сгенерированныой нейронной сетью.
        Используйте полученные данные генераций на своё усмотрение.
    """,
    donates_info="""
        `AI Talks` собирает донаты исключительно с целью оплаты API `Open AI`.
        Это позволяет обеспечить доступ к общению с ИИ для всех желающих пользователей.
        Поддержите нас для совместного развития и взаимодействия с интеллектом будущего!
    """,
    empty_api_handler=f"""
        Ключ API не найден. Создайте `.streamlit/secrets.toml` с вашим ключом API.
    """,
)
