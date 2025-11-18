from streamlit import subheader, text_area


def render_mail_input(
    placeholder: str = "Escribe o pega aquí el contenido del correo...",
    height: int = 200,
    max_length: int | None = None,
) -> str:
    """
    Renderiza el área de texto para ingresar el correo.

    Args:
        placeholder: Texto de placeholder
        height: Altura del text area en pixeles
        max_length: Longitud máxima del texto (None = sin límite)

    Returns:
        str: Texto ingresado por el usuario
    """
    subheader("Ingresa el texto del correo a analizar")

    mail_text = text_area(
        label="Texto del correo",
        placeholder=placeholder,
        height=height,
        label_visibility="collapsed",
        max_chars=max_length,
    )

    return mail_text
