from streamlit import markdown, progress


def render_confidence_indicator(confidence: float, is_spam: bool) -> None:
    """
    Renderiza el indicador de confianza con colores según el nivel.

    Args:
        confidence: Nivel de confianza (0.0 a 1.0)
        is_spam: True si es spam, False si es legítimo
    """
    confidence_percent = confidence * 100

    # Determinar color según nivel de confianza
    if confidence_percent >= 80:
        color = "red" if is_spam else "green"
    elif confidence_percent >= 60:
        color = "orange"
    else:
        color = "gray"

    markdown(
        f"**Nivel de Confianza:** "
        f"<span style='color:{color}; font-size:1.2em;'>"
        f"{confidence_percent:.2f}%</span>",
        unsafe_allow_html=True,
    )

    # Barra de progreso visual
    progress(confidence)
