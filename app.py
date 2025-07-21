# main.py
import streamlit as st
from src.components import render_static_content, render_question_content, render_script_content, render_navigation_buttons, load_quiz_data
from src.features.sidebar import configure_sidebar, render_progress_indicator, render_section_navigation, render_current_section_info

def run():
    st.set_page_config(
        page_title="Guia para a Avaliação de Políticas Públicas",
        page_icon="🎯",
    )

    # CSS personalizado para os botões
    st.markdown("""
    <style>
    div.stButton > button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)


    if 'current_section' not in st.session_state:
        st.session_state.current_section = 0

    # Carrega os dados do quiz
    section_structure = load_quiz_data('content/sections_structure.json')
    
    # Configura dados para progresso e navegação (excluindo a primeira seção "Objetivo")
    st.session_state.total_sections = len(section_structure) - 1
    st.session_state.section_titles = [section.get('title', f'Seção {i+1}') for i, section in enumerate(section_structure[1:])]  # Pula primeira seção

    def render_section(section):
        render_static_content(section)
        render_question_content(section)
        render_script_content(section)
        render_navigation_buttons(section)

    # Renderizar a secção atual
    current_section = st.session_state.current_section

    # Configurar sidebar com funcionalidades avançadas
    configure_sidebar()
    render_progress_indicator()
    render_current_section_info()
    render_section_navigation()

    if current_section < len(section_structure):
        render_section(section_structure[current_section])
    else:
        st.markdown(f"""
            <div style="text-align: center;">
                <h3> 🎯Parabéns! Você concluiu a sessão de microlearning sobre o Guia para a Avaliação de Políticas Públicas. 🎯</h3>
            </div>
            """, unsafe_allow_html=True)
        st.subheader('', divider='rainbow')
        st.image("content/Assets/endsection.png")
        st.subheader('', divider='rainbow')
        st.markdown(f"""
            <div style="text-align: center;"><h4><a href='https://planapp.gov.pt/wp-content/uploads/2024/12/PlanAPP_Guia-Avaliacao-PP.pdf'target='_blank'>Ver Guia para a Avaliação de Políticas Públicas</a></h4>
            </div>""", unsafe_allow_html=True)
        st.markdown(f"""
            <div style="text-align: center;">
                <h4>Acompanhe o trabalho do PlanAPP em <a href='https://linktr.ee/planapp' target='_blank'>diferentes plataformas</a>.</h4>
            </div>
            """, unsafe_allow_html=True)
        st.balloons()

        # Botão para reiniciar
        if st.button("Reiniciar"):
            st.session_state.current_section = 0
            st.rerun()

if __name__ == "__main__":
    run()
