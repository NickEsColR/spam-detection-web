import streamlit as st
from services.spam_detector import SpamDetector
from components.ui.footer import render_footer


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

    # Título y descripción
    st.title("📧 Spam Email Detector")
    st.markdown(
        """
        Esta aplicación utiliza un modelo de Machine Learning para detectar 
        si un mensaje de correo electrónico es **spam** o **legítimo**.
        
        **Instrucciones:** Escribe o pega el texto del email y presiona el botón para analizar.
    """
    )

    # Cargar el modelo
    with st.spinner("Cargando modelo..."):
        detector = load_model()

    # Área de texto para el input
    st.subheader("Ingresa el texto del email")
    email_text = st.text_area(
        label="Texto del email",
        placeholder="Escribe o pega aquí el contenido del email...",
        height=200,
        label_visibility="collapsed",
    )

    # Botón para clasificar
    if st.button("🔍 Analizar Email", type="primary", use_container_width=True):
        if not email_text.strip():
            st.warning("⚠️ Por favor, ingresa un texto para analizar.")
        else:
            with st.spinner("Analizando..."):
                # Clasificar el email
                is_spam, confidence = detector.is_spam(email_text)

            # Mostrar resultados
            st.divider()
            st.subheader("Resultados del Análisis")

            # Crear columnas para mejor layout
            col1, col2 = st.columns(2)

            with col1:
                if is_spam:
                    st.error("🚫 **SPAM DETECTADO**")
                else:
                    st.success("✅ **EMAIL LEGÍTIMO**")

            with col2:
                # Mostrar confianza con color según el nivel
                confidence_percent = confidence * 100

                if confidence_percent >= 80:
                    color = "green" if not is_spam else "red"
                elif confidence_percent >= 60:
                    color = "orange"
                else:
                    color = "gray"

                st.markdown(
                    f"**Nivel de Confianza:** "
                    f"<span style='color:{color}; font-size:1.2em;'>"
                    f"{confidence_percent:.2f}%</span>",
                    unsafe_allow_html=True,
                )

            # Barra de progreso visual
            st.progress(confidence)

            # Información adicional
            with st.expander("ℹ️ Detalles Técnicos"):
                st.json(
                    {
                        "clasificacion": "Spam" if is_spam else "Legítimo",
                        "confianza": f"{confidence_percent:.4f}%",
                        "modelo": "Goodmotion/spam-mail-classifier",
                        "longitud_texto": len(email_text),
                    }
                )

    # Footer
    render_footer()


if __name__ == "__main__":
    main()
