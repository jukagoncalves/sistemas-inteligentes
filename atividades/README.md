# Atividades de Sistemas Inteligentes

Notebooks desenvolvidos ao longo da disciplina, com exercícios de regressão, classificação supervisionada, processamento de texto e lógica fuzzy.

**Autor:** Juka Francis Pereira Gonçalves

## Índice

| Atividade | Tema | Notebook |
|---|---|---|
| 01 | Consumo de cerveja: regressão linear e KNN | [Ver atividade](atividade-01.ipynb) |
| 02 | Classificação de vinhos com KNN | [Ver atividade](atividade-02.ipynb) |
| 03 | Árvore de decisão e KNN com validação cruzada | [Ver atividade](atividade-03.ipynb) |
| 04 | Detecção de spam com Naive Bayes e regressão logística | [Ver atividade](atividade-04.ipynb) |
| 05 | Sistema fuzzy para cálculo de gorjetas | [Ver atividade](atividade-05.ipynb) |
| 06 | Controle fuzzy de velocidade com temperatura e umidade | [Ver atividade](atividade-06.ipynb) |

## Atividade 01 — Consumo de cerveja: regressão linear e KNN

**Objetivo:** analisar a relação entre variáveis meteorológicas e consumo de cerveja e construir modelos de regressão.

- Leitura do arquivo `Consumo_cerveja.csv`, com separador `;`, e análise de covariância e correlação.
- Uso da temperatura máxima (`temp_max`) como variável explicativa do consumo.
- Divisão de 80% dos dados para treino e 20% para teste, com `random_state=42`.
- Ajuste de regressão linear, obtenção do intercepto (Beta 1) e do coeficiente angular (Beta 2), cálculo de R² e visualização da reta.
- Comparação com `KNeighborsRegressor`, explorando valores de k de 1 a 20 e treinando um modelo com k = 9.

**Dados necessários:** o CSV precisa estar disponível no diretório de execução; ele não está incluído nesta pasta.

[Abrir no Colab](https://colab.research.google.com/github/jukagoncalves/sistemas-inteligentes/blob/main/atividades/atividade-01.ipynb)

## Atividade 02 — Classificação de vinhos com KNN

**Objetivo:** classificar amostras do dataset Wine a partir de suas características químicas.

- Carregamento do dataset pelo `load_wine`, do scikit-learn: 178 amostras, 13 atributos e três classes.
- Divisão holdout com 70% dos dados para treino e 30% para teste.
- Padronização com `StandardScaler`, ajustado somente nos dados de treino.
- Avaliação de k de 1 a 20, com gráficos de acurácia, precisão e recall.
- Treinamento de um classificador KNN com k = 5 e apresentação das previsões e métricas, com média ponderada para precisão e recall.

**Observação:** a divisão não fixa `random_state`, portanto os resultados podem variar entre execuções. A escolha de k é explorada no próprio conjunto de teste.

[Abrir no Colab](https://colab.research.google.com/github/jukagoncalves/sistemas-inteligentes/blob/main/atividades/atividade-02.ipynb)

## Atividade 03 — Árvore de decisão e KNN com validação cruzada

**Objetivo:** comparar dois classificadores no dataset Wine usando validação cruzada estratificada.

- Padronização das características com `StandardScaler`.
- Árvore de decisão com critério de entropia e `random_state=42`.
- KNN com cinco vizinhos.
- Validação cruzada com `StratifiedKFold`, cinco folds, embaralhamento e `random_state=42`.
- Apresentação das médias de acurácia, precisão macro, recall macro e F1 macro.
- Geração de matrizes de confusão e relatórios de classificação.

**Como interpretar:** no código atual, a padronização acontece antes da validação cruzada. Além disso, as matrizes e os relatórios usam o estimador do último fold para prever todo o dataset, incluindo dados usados no treinamento; não representam uma avaliação em teste independente. As médias impressas são provenientes da validação cruzada.

[Abrir no Colab](https://colab.research.google.com/github/jukagoncalves/sistemas-inteligentes/blob/main/atividades/atividade-03.ipynb)

## Atividade 04 — Detecção de spam

**Objetivo:** classificar mensagens como spam ou ham (não spam), comparando Naive Bayes multinomial e regressão logística.

- Leitura das mensagens e categorias de um CSV disponível no repositório [Spam-and-ham-data](https://github.com/GehadGad/Spam-and-ham-data).
- Tokenização com `RegexpTokenizer` e remoção de stopwords em inglês com NLTK.
- Construção de representações Bag-of-Words e TF-IDF.
- Treinamento de `MultinomialNB` e `LogisticRegression` com Bag-of-Words na configuração salva.
- Divisão com 70% para treino e 30% para teste, com `random_state=42`.
- Avaliação por precisão, recall e F1, considerando `spam` como classe positiva.

**Como interpretar:** o TF-IDF é calculado, mas não é usado no treinamento salvo. Os vetorizadores são ajustados antes da divisão dos dados; para uma avaliação mais rigorosa, o vocabulário deve ser aprendido somente no treino.

**Dados necessários:** conexão com a internet para carregar o CSV e baixar as stopwords do NLTK.

[Abrir no Colab](https://colab.research.google.com/github/jukagoncalves/sistemas-inteligentes/blob/main/atividades/atividade-04.ipynb)

## Atividade 05 — Sistema fuzzy para gorjetas

**Objetivo:** estimar a porcentagem de gorjeta com base na qualidade da comida e do serviço, utilizando lógica fuzzy.

- Instalação e uso da biblioteca `scikit-fuzzy`.
- Entradas de qualidade e serviço em uma escala de 0 a 10.
- Saída de gorjeta em uma escala de 0% a 20%, com conjuntos baixa, média e alta.
- Definição e visualização de funções de pertinência, incluindo sigmoidal, gaussiana e Pi para a saída.
- Construção de um sistema de controle com as 20 regras implementadas no notebook.
- Simulação com qualidade = 10 e serviço = 10, seguida da exibição da gorjeta calculada.

**Observação:** o texto introdutório apresenta três regras ilustrativas; o sistema executado utiliza a lista ampliada de 20 regras.

[Abrir no Colab](https://colab.research.google.com/github/jukagoncalves/sistemas-inteligentes/blob/main/atividades/atividade-05.ipynb)

## Atividade 06 — Controle fuzzy de velocidade

**Objetivo:** determinar uma velocidade de saída a partir de temperatura e umidade.

- Uso de `scikit-fuzzy==0.5.0`, NumPy, Matplotlib e NetworkX.
- Temperatura no intervalo de 0 a 40, com cinco conjuntos linguísticos.
- Umidade no intervalo de 0 a 100, com quatro conjuntos linguísticos.
- Velocidade no intervalo de 0 a 100, classificada como baixa, média ou alta.
- Funções de pertinência triangulares e 20 regras que combinam os conjuntos de temperatura e umidade.
- Defuzzificação pelo método do centroide.
- Simulação com temperatura = 30 e umidade = 70 e visualização da saída.

[Abrir no Colab](https://colab.research.google.com/github/jukagoncalves/sistemas-inteligentes/blob/main/atividades/atividade-06.ipynb)

## Como executar

1. Abra o link do Colab da atividade desejada.
2. Conecte-se a um ambiente de execução.
3. Execute as células na ordem em que aparecem, incluindo as instalações de bibliotecas quando presentes.
4. Na atividade 01, envie o arquivo `Consumo_cerveja.csv` para o ambiente antes da leitura dos dados.

As atividades 02 e 03 carregam o Wine diretamente pelo scikit-learn. As atividades 05 e 06 definem as entradas e regras no próprio código, sem arquivo externo de dados.

Estas descrições refletem o código salvo nos notebooks. Os exercícios registram diferentes etapas do aprendizado na disciplina; os resultados devem ser interpretados de acordo com o procedimento de avaliação usado em cada atividade.

## Projeto final

O projeto final está documentado separadamente em [Phishing Detector](../phishing-detector/README.md).
