from streamlit import title, markdown


def render_header():
    title("📧 Spam Email Detector")
    markdown(
        """
        Esta aplicación utiliza un modelo de Machine Learning para detectar 
        si un mensaje de correo electrónico es **spam** o **legítimo**.
        
        **Instrucciones:** Escribe o pega el texto del email y presiona el botón para analizar.
    """
    )
