# SALInA Assistente do Aluno da Universidade de Aveiro 🎓🤖

O **SALInA** (Sistema de Apoio e Ligação de Informação ao Aluno) é uma solução analítica e operacional desenvolvida no âmbito da unidade curricular de **Seminário de Business Cases** do Mestrado em Ciência de Dados para Ciências Sociais da Universidade de Aveiro.

O objetivo principal é mitigar a assimetria de informação e apoiar a tomada de decisão dos estudantes (atuais e candidatos) ao longo de todo o ciclo de vida académico na UA (admissões, matrículas, propinas, bolsas, alojamento, serviços académicos e biblioteca).

- Arquitetura e Metodologia (Fluxo KDD)

O projeto foi estruturado de forma incremental e iterativa seguindo o processo KDD (Knowledge Discovery in Databases), dividido em 4 etapas fundamentais:

1. **Base de Conhecimento (Milestone 1):** Curadoria e mapeamento de 44 pares estruturados de perguntas, respostas detalhadas e links oficiais da UA.
2. **Análise Exploratória e Qualidade de Dados (Milestone 2):** Auditoria de qualidade em Python, análise de distribuição de categorias e tamanho de strings para garantir a consistência das respostas.
3. **Automação e Orquestração (Milestone 3):** Criação de um pipeline *backend* sem servidor na plataforma **n8n**, que consome dinamicamente a base de conhecimento via Google Drive e processa a lógica de correspondência de texto.
4. **Interface do Utilizador / UI (Milestone 4):** Desenvolvimento de uma aplicação web demonstradora (*frontend* responsivo em HTML/CSS/JS) com a identidade institucional da Universidade de Aveiro.
