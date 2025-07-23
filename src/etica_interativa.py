import streamlit as st

def slider_app():
    """Interactive ethical dilemmas for public policy evaluation"""
    
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
            "title": "Dilema 1: Pressão Externa",
            "description": "A Ema, enquanto coordenadora da equipa de avaliação, é contactada por um fundo imobiliário que pretende acompanhar os trabalhos da avaliação.",
            "principle": "Independência",
            "explanation": "pressupõe que o avaliador age livre de condicionamentos ou pressões externas que possam comprometer a credibilidade e integridade da avaliação. Com amabilidade e assertividade, a Ema recusa o pedido.",
            "missing_explanations": ["Imparcialidade", "Credibilidade"]
        },
        {
            "title": "Dilema 2: Enviesamento Pessoal",
            "description": "Um dos membros da equipa de avaliação tem, desde o início, uma opinião muito vincada acerca do mercado de arrendamento. Misturando por vezes a sua opinião com a análise de evidências, dá grande importância aos dados que corroboram a sua opinião e desvaloriza aqueles que a refutam.",
            "principle": "Imparcialidade",
            "explanation": "diz respeito à capacidade de o avaliador ser justo durante a avaliação, considerando diversas perspetivas e evidências, sem deixar que preconceitos ou preferências pessoais enviesem o trabalho de análise. Pedagogicamente, a Ema explica ao colega a importância de suspender a nossa opinião quando estamos a realizar uma avaliação.",
            "missing_explanations": ["Independência", "Credibilidade"]
        },
        {
            "title": "Dilema 3: Licença de Parentalidade",
            "description": "Durante a avaliação, um membro da equipa ausenta-se em licença de parentalidade.",
            "principle": "Nenhum princípio ético está ameaçado",
            "explanation": "Para substituir o membro da equipa ausente em licença de parentalidade, um outro colega é designado. O organismo apoia incondicionalmente o exercício dos direitos de parentalidade.",
            "missing_explanations": ["Independência", "Imparcialidade", "Credibilidade"]
        },
        {
            "title": "Dilema 4: Rigor na Fundamentação",
            "description": "Ao ler uma versão preliminar do relatório de avaliação, Ema apercebe-se de que existe um conjunto de dados recolhidos que, por lapso, não foi incluído no relatório, pelo que algumas das recomendações apresentadas não estão devidamente fundamentadas em dados empíricos.",
            "principle": "Credibilidade",
            "explanation": "pressupõe que a avaliação é rigorosa, mobiliza os métodos mais adequados, apresenta conclusões robustas e fundamentadas em evidências, bem como recomendações claras, concisas e equilibradas. A Ema reúne a equipa e revêem o relatório, de forma a corrigir essa falha.",
            "missing_explanations": ["Independência", "Imparcialidade"]
        }
    ]

    # Create tabs for each scenario
    tab_names = [f"Dilema {i+1}" for i in range(len(scenarios))]
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
            st.write("**Que princípio ético está ameaçado?**")
            
            options = [
                "Independência",
                "Imparcialidade", 
                "Credibilidade",
                "Nenhum princípio ético está ameaçado"
            ]
            
            selected = st.radio(
                "Selecione o princípio:",
                options,
                key=f"scenario_{i}",
                label_visibility="collapsed"
            )
            
            if st.button("Ver resposta", key=f"answer_{i}"):
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
                
                # Show missing explanations
                if scenario.get('missing_explanations'):
                    st.warning("⚠️ **Explicações em falta no texto original:**")
                    for missing in scenario['missing_explanations']:
                        st.write(f"• **{missing}**: [sem explicação disponível no texto original]")

# Ensure the script can be run standalone for testing
if __name__ == "__main__":
    slider_app()
