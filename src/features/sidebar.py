"""
Sidebar feature for the microlearning application.
Contains all sidebar-related functionality.
"""
import streamlit as st
import os


def configure_sidebar():
    """Configura a sidebar do Streamlit."""
    logo_path = "content/Assets/logo.png"
    icon_path = "content/Assets/logo.png"
    
    # Verifica se os arquivos existem
    if os.path.exists(logo_path) and os.path.exists(icon_path):
        st.logo(logo_path, icon_image=icon_path)
    else:
        st.warning("📷 Logo não encontrado (usando placeholder)")

    st.sidebar.title("Microlearning Guia para a Avaliação de Políticas Públicas 🎯")
    st.sidebar.divider()
    
    st.sidebar.subheader("Objetivo 🎯")
    st.sidebar.markdown("""**Apresentar o Guia para a Avaliação de Políticas Públicas, através de um caso prático, ficcionado com base em experiências reais.**
    
    Neste microlearning irá:
    - Conhecer a Ema e o seu desafio
    - Compreender tipos e focos de avaliação
    - Definir questões e métodos de avaliação  
    - Identificar princípios éticos
    - Aprender gestão de controvérsias
    - Acompanhar o seguimento das recomendações
    """)
    st.sidebar.divider()


    
    # Botão para reiniciar no final
    if st.sidebar.button("🔄 Voltar ao início", use_container_width=True):
        st.session_state.current_section = 1  # Reinicia na seção 1, não na 0
        st.rerun()


def render_progress_indicator():
    """Renderiza um indicador de progresso na sidebar."""
    if 'current_section' in st.session_state and 'total_sections' in st.session_state:
        current = st.session_state.current_section
        total = st.session_state.total_sections
        
        # Ajustar cálculo de progresso considerando que começamos na seção 1
        progress = (current) / (total + 1) if total > 0 else 0
        
        st.sidebar.subheader("Progresso")
        st.sidebar.progress(progress)
        st.sidebar.text(f"Secção {current} de {total + 1}")
        st.sidebar.divider()

        # Links úteis
        st.sidebar.subheader("Links Úteis 🔗")
        st.sidebar.markdown("[📘 Ver Guia para a Avaliação de PP](https://planapp.gov.pt/wp-content/uploads/2024/12/PlanAPP_Guia-Avaliacao-PP.pdf)")
        st.sidebar.markdown("[🫶 Acompanhe o PlanAPP](https://linktr.ee/planapp)")
        st.sidebar.divider()

