# Autoavaliação

> Documento principal do tópico **"Autoavaliação"** — atingimento dos objetivos, dificuldades, aprendizados e trabalhos futuros.

---

## Atingimento dos objetivos

* **P1 — Variação temporal da área média:** **não respondida de forma conclusiva**. As mudanças na cobertura do cadastro, decorrentes da substituição do CEI pelo CNO e da incorporação de registros do cadastro anterior, somadas à sub-representação de casas com até 70 m², impedem afirmar, com segurança, que o tamanho médio das casas aumentou ou diminuiu ao longo do tempo. A limitação foi identificada durante a análise e discutida em conjunto com os resultados. [Discussão](../analise-de-dados/README.md#p1--houve-variação-no-tempo-da-área-média-das-casas).

* **P2 — Relação entre população e área construída:** **respondida**. Foi identificada uma associação entre população e área média: regiões imediatas mais populosas apresentaram, em geral, maior metragem média. Entretanto, por se tratar de uma análise agregada e observacional, o resultado não permite estabelecer relação de causalidade.

* **P3 — Situação da obra por porte:** **respondida**. A hipótese de maior ocorrência dos status `PARALISADA` e `NULA` entre obras menores não foi confirmada na base analisada.

Assim, os objetivos foram **majoritariamente atingidos**. Um dos principais aprendizados foi perceber que a resposta de uma análise de dados nem sempre é um resultado numérico ou uma confirmação de hipótese: em P1, a impossibilidade de chegar a uma conclusão confiável também representa um resultado relevante, pois evidencia uma limitação estrutural da fonte utilizada e evita uma interpretação incorreta dos dados.


## Qualidade dos dados

Os dados de **população estimada e municípios**, provenientes de bases curadas do IBGE/Base dos Dados, apresentaram **boa qualidade**. A etapa de validação identificou poucos ou nenhum registro inválido, o que reduziu a necessidade de tratamentos complexos nesses domínios e permitiu concentrar os esforços de qualidade e integração no CNO.

No CNO, por outro lado, as principais dificuldades não estavam apenas relacionadas a registros inválidos, mas à **compreensão da origem, cobertura e significado dos dados**. Isso reforçou a importância de diferenciar problemas de qualidade propriamente ditos de limitações inerentes à fonte.

## Elogio à plataforma

O **Databricks** foi um ponto positivo do desenvolvimento. A plataforma integrou engenharia, processamento, análise e visualização em um único ambiente, atendendo adequadamente ao escopo do MVP mesmo com as limitações do ambiente gratuito e do cluster disponível.

A utilização de tabelas Delta também facilitou a persistência, organização e consulta dos dados ao longo das diferentes etapas do pipeline. Apesar da curva de aprendizado inicial, o contato com a plataforma contribuiu para uma experiência mais próxima de um fluxo de engenharia de dados aplicado a um projeto real.

## Dificuldades encontradas

* **Integração geográfica CNO × IBGE:** o CNO utiliza o código de município no padrão **TOM**, associado ao SIAFI, enquanto o IBGE e a Base dos Dados utilizam o **código IBGE**. Foi necessária a utilização da biblioteca `cidade-ibge-tom` para realizar essa correspondência. Entretanto, a base estática disponibilizada pela biblioteca não contempla todos os municípios, fazendo com que alguns códigos não encontrassem correspondência e resultassem em `null`. Esses casos precisaram ser tratados na camada silver.

* **Instalação da biblioteca:** o wheel da `cidade-ibge-tom` disponível no PyPI apresentou problemas, sendo necessário realizar a instalação diretamente a partir do código-fonte disponibilizado no GitHub.

* **Interpretação da cobertura do CNO:** compreender que a ausência ou baixa frequência de determinados registros pode estar relacionada às próprias regras de registro da fonte, e não necessariamente à inexistência dessas construções na realidade, foi uma das principais dificuldades conceituais do projeto.

## Trabalhos futuros

* Investigar **outra fonte para o relacionamento TOM ↔ IBGE**, como listas oficiais de municípios disponibilizadas pelo SIAFI/Tesouro Transparente, buscando reduzir a quantidade de códigos sem correspondência.

* Avaliar **fontes complementares ao CNO** que representem melhor o universo de imóveis e residências, como cadastros imobiliários municipais, dados de IPTU e registros imobiliários, especialmente para ampliar a cobertura de residências pequenas.

* Expandir a análise para diferentes níveis geográficos, como **estados e regiões**, permitindo identificar padrões que podem não ser observados apenas no nível de região imediata.

* Realizar uma análise específica de **Conjunto habitacional popular**, caso seja possível definir adequadamente seu universo e comparabilidade com as demais categorias.

* Comparar os resultados do CNO com fontes externas para avaliar **cobertura, representatividade e possíveis vieses** da base.

## O que faria diferente

Em uma próxima execução, dedicaria mais tempo, ainda na etapa inicial, à **definição do universo de análise, das métricas e das limitações da fonte de dados**. Também buscaria validar antecipadamente a cobertura do CNO e seus principais campos com documentação oficial e fontes externas.

Essa etapa inicial poderia reduzir retrabalho nas fases posteriores e permitiria definir desde o começo quais perguntas são efetivamente respondíveis com a fonte escolhida.

O principal aprendizado foi que, em um projeto de dados, **a qualidade da análise depende não apenas do processamento correto dos dados, mas também da compreensão de como, por que e em quais condições esses dados foram produzidos**.
