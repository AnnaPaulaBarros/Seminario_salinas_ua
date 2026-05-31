# SALInA Assistente do Aluno da Universidade de Aveiro

Durante as últimas semanas, no âmbito do Mestrado em Ciência de Dados para Ciências Sociais na Universidade de Aveiro, eu desenvolvi o projeto para ajudar alunos imigrantes a encontrarem respostam que precisam no site da UA, sem precisar contratar empresas de suporte para estudar em universidades estrangeiras. 

O desafio era claro: mitigar a assimetria de informação e ajudar candidatos e estudantes a navegarem pelas dúvidas mais frequentes da vida académica (matrículas, propinas, bolsas, alojamento, etc.).

Em vez de criar apenas uma análise teórica, desennhei e implementei um fluxo completo ponta-a-ponta (Pipeline KDD):

Base de Conhecimento & EDA: Consolidação e auditoria de qualidade (em Python) de uma base de dados com as principais FAQs da UA.
Automação & Backend: Criação de um pipeline dinâmico sem servidor (stateless) utilizando a plataforma n8n para orquestrar a lógica de resposta.
 Interface (UI): Desenvolvimento de um protótipo web interativo (HTML/CSS/JS) para simular a experiência real de um utilizador.

O sistema conta ainda com um mecanismo de contingência proativo: quando uma dúvida foge ao escopo mapeado, o assistente reencaminha de forma inteligente o utilizador para os canais de atendimento oficiais, garantindo que ninguém fica sem resposta.

Olhando para o futuro, o próximo passo lógico para este projeto seria evoluir a arquitetura para um sistema RAG (Retrieval-Augmented Generation) com embeddings vetoriais e integração de LLMs para uma compreensão semântica ainda mais profunda.
