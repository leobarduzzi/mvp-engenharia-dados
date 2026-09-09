# Definições operacionais

> [← Voltar para o README do tópico](README.md)

> Registro das decisões de escopo que tornam as perguntas **mensuráveis** e a análise **reprodutível**.
> Itens marcados como **pendente** serão decididos após exploração dos dados e registrados aqui (mantendo o histórico da decisão).

---

## 1. O que é uma "casa" no universo analisado

- Universo: áreas declaradas no CNO com destinação **`Residencial unifamiliar`** ou **`Casa popular`** (códigos RFB `0` e `5`).
- **Decidido:** **não incluir** **`Conjunto habitacional popular`** (código `6`) — tipicamente projeto coletivo, não "casa individual". Universo aplicado na análise.
- Excluído por definição: residencial multifamiliar (apartamentos), demais destinações comerciais/industriais.

## 2. Métrica de tamanho da casa

- **Métrica principal:** `metragem` (área da área declarada no CNO), **não** `area_total` (área da obra, repetida por linha de área na `fato_obras`).
- **Decidido:** considerar **somente a metragem da área `Principal`** (`tipo_de_area = 'Principal'`) — a "casa" em si. Áreas **Complementares** (piscina, estacionamento térreo, quadra) não representam a casa e ficam fora da métrica.

## 3. Período

- Obras com `data_de_inicio >= 1990-01-01` (alinhado ao intervalo da `gold.dim_data`, 1990–2030).

## 4. Filtros de validade

- **Situação:** **decidido** — considerar **todas as situações** (a análise não filtra por situação; a P3 avalia a distribuição por situação).
- **Categoria:** **decidido** — considerar `'Existente'` e `'Obra Nova'` (universo usado na análise; ver [`qualidade/cadastro_nacional_obras.ipynb`](../../qualidade/cadastro_nacional_obras.ipynb)).
- **Unidade de medida:** **decidido** — considerar apenas `m2` (metro quadrado). O CSV da RFB traz o literal `m2` (sem o caractere `²`); a análise de qualidade ([`qualidade/cadastro_nacional_obras.ipynb`](../../qualidade/cadastro_nacional_obras.ipynb)) confirmou que não há outras unidades válidas na fonte, e ocorrências como `km` e `,m2` (erros de digitação) foram descartadas na camada silver (sem correção automática).

## 5. População

- Fonte: `fato_populacao` (município × ano, 1991–2025), via `dim_municipio`.
- **Região geográfica imediata:** soma da população dos municípios da região no mesmo ano; metragem média das casas dos municípios da região.
- **Alinhamento temporal:** **decidido** — população **no ano da obra** (join `fato_populacao.ano` = ano do início). Obras em anos sem estimativa (ex.: 1990, 2026+) ficam sem pareamento (documentado na análise).

## 6. Limitações conhecidas

- O CNO é um cadastro de **finalidade tributária**: obras informais/sem regularização podem estar sub-representadas.
- **Sub-representação de pequenas construções:** a legislação do CNO prevê dispensa de registro para residências unifamiliares de até **70 m²** em condições específicas — a distribuição observada tende a sub-representar casas pequenas (ver [`qualidade/cadastro_nacional_obras.ipynb`](../../qualidade/cadastro_nacional_obras.ipynb)).
- Situações e datas podem apresentar lacunas (tratadas na camada silver — registros inválidos descartados).
- As decisões deste documento afetam diretamente os resultados; por isso o **histórico das decisões** deve ser mantido na Análise.