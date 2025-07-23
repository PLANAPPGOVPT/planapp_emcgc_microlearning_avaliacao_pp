# src/components.py
import streamlit as st
import os
import json
from PIL import Image


def render_question_content(section):
    """Render question and handle user response."""
    question_key = "question_multiple" if "question_multiple" in section else "question"
    if question_key in section:
        st.write(section[question_key])
        options = section.get("options", [])
        
        feedback_placeholder = st.empty()

        if not st.session_state.get("response_submitted", False):
            selected_options = st.multiselect("Selecione uma ou mais opções", options, placeholder="Selecione uma opção", key="multiselect") if question_key == "question_multiple" else st.radio("Selecione uma opção", options)

            if selected_options:
                if st.button(section.get("button_text", "Responder")):
                    st.session_state.response_submitted = True
                    st.session_state.selected_options = selected_options
                    st.rerun()  # Changed from st.experimental_rerun() to st.rerun()
        
        if st.session_state.get("response_submitted", False):
            selected_options = st.session_state.get("selected_options", [])
            
            # Garantir que selected_options é sempre uma lista
            if not isinstance(selected_options, list):
                selected_options = [selected_options] if selected_options else []
            
            correct_count = 0
            incorrect_count = 0

            # Contar respostas corretas e incorretas
            for option in selected_options:
                if option in section["answer"]:
                    correct_count += 1
                else:
                    incorrect_count += 1

            # Verificar se acertou completamente
            is_fully_correct = False
            if question_key == "question":  # Resposta única
                is_fully_correct = correct_count == 1 and incorrect_count == 0
                if is_fully_correct:
                    feedback_placeholder.success("Resposta correta!")
                else:
                    feedback_placeholder.error("Resposta incorreta.")
            else:  # Múltiplas respostas
                is_fully_correct = correct_count == len(section["answer"]) and incorrect_count == 0
                if is_fully_correct:
                    feedback_placeholder.success("Todas as respostas estão corretas!")
                elif correct_count > 0 and incorrect_count > 0:
                    feedback_placeholder.warning("Existem respostas corretas, mas também existem respostas incorretas.")
                elif correct_count == 1 and incorrect_count == 0:
                    feedback_placeholder.warning("Resposta correta, mas ainda incompleta.")
                elif correct_count > 1 and correct_count < len(section["answer"]) and incorrect_count == 0:
                    feedback_placeholder.warning("Respostas corretas, mas incompletas.")
                else:
                    feedback_placeholder.error("Existem respostas incorretas.")
            
            # Quando acerta, mostrar explicações de todas as opções (corretas e incorretas)
            if is_fully_correct:
                st.markdown("---")
                st.markdown("### 💡 **Explicações de todas as opções:**")
                
                # Mostrar opções corretas
                st.success("✅ **Opções corretas:**")
                for option in section["answer"]:
                    explanation = section["explanations"].get(option, "")
                    st.write(f"• **{option}**: {explanation}")
                
                # Mostrar opções incorretas (se existirem)
                incorrect_options = [opt for opt in options if opt not in section["answer"]]
                if incorrect_options:
                    st.error("❌ **Opções incorretas:**")
                    for option in incorrect_options:
                        explanation = section["explanations"].get(option, "")
                        st.write(f"• **{option}**: {explanation}")
            else:
                # Quando não acerta, mostrar apenas o feedback das opções selecionadas (como antes)
                for option in selected_options:
                    explanation = section["explanations"].get(option, "")
                    if option in section["answer"]:
                        st.success(f"{option}: {explanation}")
                    else:
                        st.error(f"{option}: {explanation}")
            
            # Botões de navegação
            if is_fully_correct:
                # Quando acerta, só mostra botão continuar (sem "tentar novamente")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(section.get("button_answer", "Continuar")):
                        st.session_state.current_section += 1
                        st.session_state.response_submitted = False
                        st.rerun()
                if st.session_state.current_section > 0:
                    with col2:
                        if st.button("Voltar"):
                            st.session_state.current_section -= 1
                            st.session_state.response_submitted = False
                            st.rerun()
            else:
                # Quando não acerta, mostra botões continuar, tentar novamente e voltar
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button(section.get("button_answer", "Continuar")):
                        st.session_state.current_section += 1
                        st.session_state.response_submitted = False
                        st.rerun()
                with col2:
                    if st.button("Tentar novamente"):
                        st.session_state.response_submitted = False
                        st.rerun()
                if st.session_state.current_section > 0:
                    with col3:
                        if st.button("Voltar"):
                            st.session_state.current_section -= 1
                            st.session_state.response_submitted = False
                            st.rerun()
def render_static_content(section):
    """Render title, image, and text from the section."""
    if "title" in section:
        st.markdown(f"<h3 style='text-align: center;'>{section['title']}</h3>", unsafe_allow_html=True)
    if "image_path" in section:
        if os.path.exists(section["image_path"]):
            st.image(section["image_path"])
        else:
            st.info(f"📷 Imagem: {section['image_path']} (não encontrada)")
        st.divider()
    if "text" in section:
        st.markdown(section["text"].replace("\n", "  \n"))


def render_script_content(section):
    """Execute script if present in the section."""
    if "script_path" in section:
        script_path = section["script_path"]
        script_dir, script_name = os.path.split(script_path)
        script_module_name = script_name.replace('.py', '')

        # Add script directory to the system path
        import sys
        sys.path.append(script_dir)

        # Import and run the script
        script_module = __import__(script_module_name)
        script_module.slider_app()

def render_navigation_buttons(section):
    """Render navigation buttons."""
    if "button_text" in section:
        if st.session_state.current_section > 0:
            st.subheader('', divider='rainbow')
            col1, col2 = st.columns(2)
            with col1:
                if st.button(section["button_text"]):
                    st.session_state.current_section += 1
                    st.rerun()
            with col2:
                if st.button("Voltar"):
                    st.session_state.current_section -= 1
                    st.rerun()
        else:
            if st.button(section["button_text"]):
                st.session_state.current_section += 1
                st.rerun()

def load_quiz_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
