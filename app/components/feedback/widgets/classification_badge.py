from streamlit import error, success


def render_classification_badge(is_spam: bool) -> None:
    """
    Renderiza el badge de clasificación (Spam o Legítimo).

    Args:
        is_spam: True si es spam, False si es legítimo
    """
    if is_spam:
        error("🚫 **SPAM DETECTADO**")
    else:
        success("✅ **EMAIL LEGÍTIMO**")
