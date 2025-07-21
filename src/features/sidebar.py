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


def render_section_navigation():
    """Renderiza navegação rápida entre seções na sidebar."""
    if 'current_section' in st.session_state and 'section_titles' in st.session_state:
        st.sidebar.subheader("Navegação Rápida")
        section_titles = st.session_state.section_titles
        current_section = st.session_state.current_section
        
        for i, title in enumerate(section_titles):
            # Ajustar índice para corresponder ao current_section (que começa em 1)
            section_index = i + 1
            
            # Limpa o título removendo emojis e limitando tamanho
            clean_title = title.replace("🎯", "").replace("🏠", "").replace("📋", "").strip()
            if len(clean_title) > 25:
                clean_title = clean_title[:22] + "..."
            
            if section_index == current_section:
                st.sidebar.markdown(f"**▶ {section_index}. {clean_title}**")
            elif section_index < current_section:
                if st.sidebar.button(f"✓ {section_index}. {clean_title}", key=f"nav_{section_index}"):
                    st.session_state.current_section = section_index
                    st.rerun()
            else:
                st.sidebar.markdown(f"⏸ {section_index}. {clean_title}")
        
        st.sidebar.divider()

            # Links úteis
        st.sidebar.subheader("Links Úteis 🔗")
        st.sidebar.markdown("[📘 Ver Guia para a Avaliação de PP](https://planapp.gov.pt/wp-content/uploads/2024/12/PlanAPP_Guia-Avaliacao-PP.pdf)")
        st.sidebar.markdown("[🫶 Acompanhe o PlanAPP](https://linktr.ee/planapp)")
        st.sidebar.divider()


def render_current_section_info():
    """Renderiza informações sobre a secção atual."""
    if 'current_section' in st.session_state and 'section_titles' in st.session_state:
        current = st.session_state.current_section
        total = st.session_state.total_sections
        section_titles = st.session_state.section_titles
        
        # Ajustar índice porque current_section inclui seção 0, mas section_titles começa na seção 1
        title_index = current - 1 if current > 0 else 0
        
        # Verificar se o índice ajustado está dentro do range válido
        if 0 <= title_index < len(section_titles):
            st.sidebar.subheader("Secção Atual")
            title = section_titles[title_index][:30]
            if len(section_titles[title_index]) > 30:
                title += "..."
            st.sidebar.info(f"**{current + 1}/{total + 1}** - {title}")
            st.sidebar.divider()
