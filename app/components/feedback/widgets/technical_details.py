from streamlit import expander, json


def render_technical_details(
    is_spam: bool,
    confidence: float,
    mail_text: str,
    model_name: str = "Goodmotion/spam-mail-classifier",
) -> None:
    """
    Renderiza un expander con detalles técnicos del análisis.

    Args:
        is_spam: True si es spam, False si es legítimo
        confidence: Nivel de confianza (0.0 a 1.0)
        mail_text: Texto del email analizado
        model_name: Nombre del modelo utilizado
    """
    with expander("ℹ️ Detalles Técnicos"):
        confidence_percent = confidence * 100

        json(
            {
                "clasificación": "Spam" if is_spam else "Legítimo",
                "confianza": f"{confidence_percent:.2f}%",
                "modelo": model_name,
                "longitud_texto": len(mail_text),
            }
        )
