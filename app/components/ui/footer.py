from streamlit import divider, markdown


def render_footer():
    """Renderiza el footer de la aplicación con información del proyecto."""
    divider()
    markdown(
        """
        <div style='text-align: center; color: gray; font-size: 0.8em;'>
            Proyecto desarrollado para el curso de MSc Applied Artificial Intelligence - ICESI University<br>
            Modelo: <a href='https://huggingface.co/Goodmotion/spam-mail-classifier' target='_blank'>
            Goodmotion/spam-mail-classifier</a>
        </div>
    """,
        unsafe_allow_html=True,
    )
