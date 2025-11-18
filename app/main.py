import streamlit as st
from services.spam_detector import SpamDetector
from components.ui.footer import render_footer
from components.ui.header import render_header
from components.inputs.mail_input import render_mail_input
from components.buttons.analysis_button import render_analysis_button
from components.feedback.results_display import render_results


@st.cache_resource
def load_model():
    """Carga el modelo una sola vez y lo cachea."""
    return SpamDetector()


def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Spam Detector",
        page_icon="📧",
        layout="centered",
    )

    render_header()

    # Cargar el modelo
    with st.spinner("Cargando modelo..."):
        detector = load_model()

    # Input del email
    mail_text = render_mail_input()

    # Análisis del email
    result = render_analysis_button(mail_text, detector.is_spam)

    # Mostrar resultados si se analizó
    if result is not None:
        is_spam, confidence = result
        render_results(is_spam, confidence, mail_text)

    render_footer()


if __name__ == "__main__":
    main()
