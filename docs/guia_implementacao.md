# Microlearning – Guia de Implementação Narrativa

Este repositório contém o conteúdo e estrutura narrativa da aplicação de microlearning desenvolvida para apresentar o **Guia para a Avaliação de Políticas Públicas** através de um percurso prático.

## 🎯 Objetivo da aplicação

A aplicação guia o utilizador por uma sequência de secções curtas, com o objetivo de facilitar a aprendizagem de conceitos e práticas associadas à avaliação de políticas públicas. A experiência é interativa, baseada em leitura, resposta a perguntas com feedback, e pequenas simulações.

---

## 🧱 Tipos de secção suportados

Cada secção é marcada por um tipo específico que determina o seu comportamento na aplicação. Todos os tipos seguem uma estrutura previsível com campos fixos.

### 1. Secção tipo **Texto**
- Apresenta apenas informação (narrativa, contexto ou conceitos).
- O utilizador apenas lê e avança.

### 2. Secção tipo **Pergunta**
- Contém uma pergunta com resposta única.
- Inclui texto de enquadramento e feedback com explicações para todas as opções.
- O utilizador seleciona uma opção e recebe feedback imediato.

### 3. Secção tipo **Pergunta de escolha múltipla**
- Permite selecionar mais do que uma opção correta.
- Tal como nas perguntas simples, cada opção tem explicação associada.
- O utilizador pode tentar novamente se não acertar todas.

### 4. Secção tipo **Script**
- Simula uma experiência ou cenário mais complexo (ex: dilemas éticos).
- Permite interações encadeadas e múltiplas perguntas no mesmo contexto.

---

## 📐 Estrutura dos ficheiros de conteúdo

Cada secção deve seguir o seguinte padrão:

```plaintext
Secção [número]
Título:
[Título da secção — se não existir no original, indicar com "[sem título disponível no texto original]"]

Texto: (caso seja secção tipo Texto)
[Texto narrativo ou introdutório]

Pergunta: (caso seja secção tipo Pergunta ou Escolha múltipla)
[Texto completo da pergunta, incluindo o enquadramento se aplicável]

Opções:
[Lista de todas as opções apresentadas ao utilizador, sem bullets para facilitar copy-paste para Word]

Explicações:
[Explicação para cada opção. Se não existir, usar: "[sem explicação disponível no texto original]"]

Respostas certas:
[Listar as respostas corretas. Se alguma estiver marcada a amarelo no original, usar a marcação: "[texto marcado a amarelo no texto original, será certo?]"]


Secção 4
Título:
[sem título disponível no texto original] Estudo inicial da Ema

Pergunta:
A Ema começa por estudar o programa... A avaliação de que a Ema está encarregada, portanto, é uma…

Opções:
Avaliação ex ante  
Avaliação ongoing  
Avaliação ex post

Explicações:
[sem explicação disponível no texto original] Avaliação ex ante – ocorre antes da implementação de uma política  
[sem explicação disponível no texto original] Avaliação ongoing – acompanha a execução em curso e apoia decisões de ajustamento  
[sem explicação disponível no texto original] Avaliação ex post – analisa os efeitos após a conclusão da execução  

Respostas certas:
Avaliação ongoing
