from streamlit import button, spinner, warning
from typing import Tuple, Callable


def render_analysis_button(
    mail_text: str,
    analyze_callback: Callable[[str], Tuple[bool, float]],
    button_text: str = "🔍 Analizar Email",
) -> Tuple[bool, float] | None:
    """
    Renderiza el botón de análisis y maneja la lógica de validación.

    Args:
        email_text: Texto del email a analizar
        analyze_callback: Función que realiza el análisis
        button_text: Texto del botón

    Returns:
        Tuple[bool, float] | None: (is_spam, confidence) si se analizó, None en otro caso
    """
    if button(button_text, type="primary", use_container_width=True):
        if not mail_text.strip():
            warning("⚠️ Por favor, ingresa un texto para analizar.")
            return None

        with spinner("Analizando..."):
            return analyze_callback(mail_text)

    return None
