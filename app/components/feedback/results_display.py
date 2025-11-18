from streamlit import divider, subheader, columns
from components.feedback.widgets.classification_badge import render_classification_badge
from components.feedback.widgets.confidence_indicator import render_confidence_indicator
from components.feedback.widgets.technical_details import render_technical_details


def render_results(
    is_spam: bool,
    confidence: float,
    mail_text: str,
    model_name: str = "Goodmotion/spam-mail-classifier",
) -> None:
    """
    Renderiza la visualización completa de los resultados del análisis.

    Args:
        is_spam: True si es spam, False si es legítimo
        confidence: Nivel de confianza (0.0 a 1.0)
        mail_text: Texto del email analizado
        model_name: Nombre del modelo utilizado
    """
    divider()
    subheader("Resultados del Análisis")

    # Crear columnas para mejor layout
    col1, col2 = columns(2)

    with col1:
        render_classification_badge(is_spam)

    with col2:
        render_confidence_indicator(confidence, is_spam)

    # Detalles técnicos
    render_technical_details(is_spam, confidence, mail_text, model_name)
