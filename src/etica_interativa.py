import streamlit as st

def slider_app():
    """Interactive ethics scenarios for public policy evaluation"""
    
    # CSS for styling
    st.markdown("""
        <style>
        .scenario-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .principle-box {
            background-color: #e8f4f8;
            padding: 15px;
            border-radius: 8px;
            margin: 5px 0;
            border-left: 4px solid #0e2a49;
        }
        </style>
    """, unsafe_allow_html=True)

    scenarios = [
        {
            "title": "Cenário 1: Confidencialidade vs Transparência",
            "description": "A Ema descobriu informações sensíveis sobre falhas no programa que podem comprometer alguns beneficiários se divulgadas, mas são importantes para a avaliação.",
            "principle": "Princípio da Confidencialidade",
            "explanation": "A avaliadora deve proteger a privacidade e confidencialidade dos dados, especialmente quando podem prejudicar os participantes."
        },
        {
            "title": "Cenário 2: Independência da Avaliação",
            "description": "O diretor do organismo pressiona a Ema para destacar apenas os aspectos positivos do programa na avaliação final.",
            "principle": "Princípio da Independência",
            "explanation": "A avaliação deve ser conduzida de forma imparcial, sem interferências políticas ou organizacionais que comprometam a objetividade."
        },
        {
            "title": "Cenário 3: Competência Técnica",
            "description": "A Ema percebe que precisa de conhecimentos específicos sobre habitação social que não possui para fazer uma avaliação adequada.",
            "principle": "Princípio da Competência",
            "explanation": "Os avaliadores devem reconhecer os limites das suas competências e procurar formação ou apoio especializado quando necessário."
        },
        {
            "title": "Cenário 4: Utilidade e Relevância",
            "description": "A avaliação está a ser feita principalmente para cumprir uma obrigação legal, sem interesse real nos resultados.",
            "principle": "Princípio da Utilidade",
            "explanation": "As avaliações devem ser desenhadas para serem úteis aos decisores e stakeholders, contribuindo para a melhoria das políticas."
        }
    ]

    # Create tabs for each scenario
    tab_names = [f"Cenário {i+1}" for i in range(len(scenarios))]
    tabs = st.tabs(tab_names)
    
    for i, (tab, scenario) in enumerate(zip(tabs, scenarios)):
        with tab:
            st.markdown(f"""
                <div class="scenario-box">
                    <h4>{scenario['title']}</h4>
                    <p>{scenario['description']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Interactive element - user selects the principle
            st.write("**Que princípio ético está em causa?**")
            
            options = [
                "Princípio da Confidencialidade",
                "Princípio da Independência", 
                "Princípio da Competência",
                "Princípio da Utilidade"
            ]
            
            selected = st.radio(
                "Selecione o princípio:",
                options,
                key=f"scenario_{i}",
                label_visibility="collapsed"
            )
            
            if st.button(f"Ver resposta", key=f"answer_{i}"):
                if selected == scenario['principle']:
                    st.success(f"✅ Correto! **{scenario['principle']}**")
                    st.markdown(f"""
                        <div class="principle-box">
                            <strong>Explicação:</strong> {scenario['explanation']}
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"❌ Não é a melhor resposta. A resposta correta é: **{scenario['principle']}**")
                    st.markdown(f"""
                        <div class="principle-box">
                            <strong>Explicação:</strong> {scenario['explanation']}
                        </div>
                    """, unsafe_allow_html=True)

# Ensure the script can be run standalone for testing
if __name__ == "__main__":
    slider_app()
