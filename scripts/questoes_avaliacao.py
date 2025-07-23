import streamlit as st

def slider_app():
    """
    Script interativo para seleção das questões de avaliação.
    O utilizador pode selecionar múltiplas questões através de checkboxes.
    """
    
    # Título da seção
    st.markdown("### Questões de Avaliação Sugeridas")
    st.markdown("**Selecione as questões que considera mais adequadas para incluir na avaliação:**")
    
    # Definir todas as questões disponíveis
    questoes = [
        "Quais os objetivos estabelecidos aquando da criação do programa estão a ser cumpridos e quais não estão a ser cumpridos?",
        "Quantas pessoas que tiveram acesso a habitação através deste programa é plausível acreditar que não o teriam sem o programa?",
        "Qual é o nível de satisfação dos beneficiários relativamente à qualidade da sua habitação antes e depois do programa?",
        "O programa teve efeitos indesejados no mercado de compra ou arrendamento de imóveis?",
        "Quais as transformações de dinâmicas comunitárias resultantes do programa?",
        "Os objetivos do programa mantêm-se relevantes à luz da realidade atual?",
        "Quais os obstáculos que se colocam a uma implementação mais eficaz do programa?",
        "Como se distribuem os efeitos positivos do programa pelos cidadãos consoante o seu nível de rendimentos, género, idade e origem racial e étnica?",
        "Em que locais do país resultou melhor ou pior o programa, e porquê?",
        "Os recursos investidos no programa estão a ser usados do modo mais eficiente possível?",
        "Como se comparam os resultados do programa com os resultados de programas alternativos implementados com o mesmo objetivo noutros países?",
        "O programa é uma boa ou uma má opção política?",
        "Quais os efeitos positivos ou negativos do programa para a popularidade do governo junto dos cidadãos?"
    ]
    
    # Questões corretas (baseadas no JSON original)
    questoes_corretas = {
        0, 1, 3, 5, 6, 7  # Índices das questões corretas
    }
    
    # Inicializar estado da sessão se não existir
    if 'questoes_selecionadas' not in st.session_state:
        st.session_state.questoes_selecionadas = set()
    if 'mostrar_resultado' not in st.session_state:
        st.session_state.mostrar_resultado = False
    
    # Criar checkboxes para cada questão
    st.markdown("---")
    for i, questao in enumerate(questoes):
        checkbox_key = f"questao_{i}"
        
        # Verificar se a questão está selecionada
        is_checked = st.checkbox(
            f"**{i+1}.** {questao}",
            key=checkbox_key,
            value=i in st.session_state.questoes_selecionadas
        )
        
        # Atualizar estado da seleção
        if is_checked:
            st.session_state.questoes_selecionadas.add(i)
        else:
            st.session_state.questoes_selecionadas.discard(i)
    
    st.markdown("---")
    
    # Botão de verificação
    if st.button("✅ Verificar Seleção", type="primary"):
        st.session_state.mostrar_resultado = True
    
    # Mostrar resultado se solicitado
    if st.session_state.mostrar_resultado:
        st.markdown("---")
        st.markdown("### 📊 Resultado da Seleção")
        
        # Verificar se a seleção está correta
        if st.session_state.questoes_selecionadas == questoes_corretas:
            st.success("🎉 **Parabéns! Seleção totalmente correta!**")
            st.markdown("A equipa decidiu incluir exatamente estas questões na avaliação.")
        else:
            # Mostrar análise detalhada
            corretas_selecionadas = st.session_state.questoes_selecionadas & questoes_corretas
            incorretas_selecionadas = st.session_state.questoes_selecionadas - questoes_corretas
            corretas_nao_selecionadas = questoes_corretas - st.session_state.questoes_selecionadas
            
            st.markdown(f"**Questões corretas selecionadas:** {len(corretas_selecionadas)}/6")
            
            if corretas_selecionadas:
                st.success("✅ **Questões corretas que selecionou:**")
                for i in corretas_selecionadas:
                    st.write(f"• {questoes[i]}")
            
            if corretas_nao_selecionadas:
                st.info("ℹ️ **Questões corretas que não selecionou:**")
                for i in corretas_nao_selecionadas:
                    st.write(f"• {questoes[i]}")
            
            if incorretas_selecionadas:
                st.warning("⚠️ **Questões que selecionou mas não deveria:**")
                for i in incorretas_selecionadas:
                    st.write(f"• {questoes[i]}")
        
        # Explicação pedagógica
        st.markdown("---")
        st.markdown("### 💡 **Reflexão Pedagógica**")
        st.info("""
        **Por que estas questões específicas?**
        
        A equipa da Ema escolheu questões que:
        - São objetivamente mensuráveis e factualmente respondíveis
        - Focam-se nos aspetos técnicos da avaliação (processo e impacto)
        - Evitam juízos de valor político ou ideológico
        - Permitem uma avaliação construtiva do programa
        
        Questões sobre "popularidade do governo" ou "boa/má opção política" foram excluídas por serem demasiado subjetivas para uma avaliação técnica.
        """)
    
    return False

if __name__ == "__main__":
    slider_app()
