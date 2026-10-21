
# Phishing Detector — Detecção de URLs com Machine Learning

Sistema de classificação de URLs desenvolvido como projeto acadêmico
da disciplina de Sistemas Inteligentes.

A aplicação utiliza técnicas de Machine Learning para identificar
padrões associados a URLs de phishing e URLs legítimas, disponibilizando
os modelos treinados por meio de uma interface web desenvolvida com
Flask, HTML e CSS.

## 1. Objetivo

Desenvolver e comparar quatro algoritmos de classificação supervisionada
para detecção de phishing em URLs, utilizando validação cruzada,
otimização de hiperparâmetros e métricas de avaliação.

Os classificadores utilizados são:

- K-Nearest Neighbors (KNN)
- Decision Tree
- Gaussian Naive Bayes
- Multilayer Perceptron (MLP)

Após o treinamento e a avaliação, os modelos são exportados e
integrados a uma aplicação web, permitindo realizar previsões
sobre novas URLs.

## 2. Dataset

Foi utilizado o dataset **PhiUSIIL Phishing URL**, disponível no
UCI Machine Learning Repository (Dataset ID: 967).

O conjunto original possui:

- 235.795 registros
- 54 características originais
- Duas classes: phishing e legítimo

Neste projeto, foram utilizadas 16 características lexicais
extraídas diretamente do texto das URLs.

### Classes

| Valor | Classe |
|---|---|
| 0 | Phishing |
| 1 | Legítimo |

Após a remoção de URLs duplicadas, foram mantidos 235.370 registros.

## 3. Extração de características

A aplicação utiliza a função `extrair_features()`, implementada
em Python, para calcular 16 características lexicais:

| Característica | Descrição |
|---|---|
| URLLength | Comprimento total da URL |
| DomainLength | Comprimento do domínio |
| IsDomainIP | Indica se o domínio é um endereço IP |
| TLDLength | Comprimento do sufixo do domínio |
| NoOfSubDomain | Quantidade de subdomínios |
| NoOfLetters | Quantidade de letras |
| LetterRatio | Proporção de letras na URL |
| NoOfDigits | Quantidade de dígitos |
| DigitRatio | Proporção de dígitos na URL |
| NoOfDots | Quantidade de pontos |
| NoOfHyphens | Quantidade de hífens |
| NoOfEquals | Quantidade de sinais de igualdade |
| NoOfQMark | Quantidade de pontos de interrogação |
| NoOfAmpersand | Quantidade de caracteres `&` |
| NoOfAt | Quantidade de caracteres `@` |
| IsHTTPS | Indica a presença do esquema HTTPS |

Essas características são calculadas sem acessar o conteúdo
das páginas web.

## 4. Metodologia

O desenvolvimento foi realizado no Google Colab, utilizando
Python e scikit-learn.

As principais etapas foram:

1. Carregamento e exploração do dataset.
2. Remoção de URLs duplicadas.
3. Separação estratificada entre desenvolvimento e teste.
4. Extração das 16 características lexicais.
5. Seleção de 20.000 registros para otimização de hiperparâmetros.
6. Busca dos melhores hiperparâmetros com GridSearchCV.
7. Comparação dos classificadores utilizando validação cruzada.
8. Treinamento final com os dados de desenvolvimento.
9. Avaliação no conjunto de teste independente.
10. Exportação dos modelos com joblib.
11. Integração dos classificadores à aplicação Flask.

### Divisão dos dados

| Conjunto | Registros |
|---|---:|
| Desenvolvimento | 188.296 |
| Teste | 47.074 |
| Amostra para otimização | 20.000 |

A amostra de otimização foi retirada do conjunto de desenvolvimento.

O conjunto de teste foi mantido separado durante a escolha dos
hiperparâmetros e o treinamento dos modelos.

### Pipelines

Foram utilizados pipelines do scikit-learn para organizar
as etapas de pré-processamento e classificação.

O `StandardScaler` foi aplicado aos modelos KNN, Gaussian Naive
Bayes e MLP. A Decision Tree foi utilizada sem normalização.

### Validação cruzada

A otimização de hiperparâmetros utilizou GridSearchCV com
validação cruzada estratificada de 3 folds.

A comparação posterior dos classificadores utilizou validação
cruzada estratificada de 5 folds, apresentando média e desvio
padrão das métricas.

## 5. Resultados

Os modelos finais foram avaliados em 47.074 URLs do conjunto
de teste.

| Modelo | Acurácia | Precisão macro | Recall macro | F1 macro |
|---|---:|---:|---:|---:|
| MLP | 99,57% | 99,61% | 99,51% | 99,56% |
| Decision Tree | 99,51% | 99,54% | 99,47% | 99,50% |
| KNN | 99,46% | 99,49% | 99,39% | 99,44% |
| Naive Bayes | 90,25% | 92,38% | 88,70% | 89,68% |

O MLP apresentou o melhor desempenho geral considerando
o F1-score macro.

A Decision Tree apresentou recall ligeiramente superior
para a classe phishing.

O Naive Bayes apresentou desempenho inferior aos demais
classificadores, especialmente na identificação de URLs
de phishing.

As métricas de validação cruzada, os desvios padrão e as
matrizes de confusão estão documentados no notebook do projeto.

## 6. Tecnologias utilizadas

- Python
- Google Colab
- scikit-learn
- pandas
- NumPy
- joblib
- tldextract
- Flask
- HTML5
- CSS3

## 7. Estrutura do projeto

```text
phishing-detector/
|
|-- app.py
|-- extrator.py
|-- requirements.txt
|-- README.md
|
|-- models/
|   |-- knn.joblib
|   |-- decision_tree.joblib
|   |-- naive_bayes.joblib
|   |-- mlp.joblib
|   |-- features.joblib
|
|-- templates/
|   |-- index.html
|
|-- static/
|   |-- style.css
```

O notebook do Google Colab contém o processo de treinamento,
otimização e avaliação dos classificadores.

## 8. Como executar

### 8.1. Pré-requisitos

É necessário ter o Python instalado e utilizar um ambiente
compatível com as dependências especificadas no
`requirements.txt`.

O requirements.txt fornecido fixa scikit-learn 1.6.1. Confira a compatibilidade dos artefatos exportados, pois a saída salva do notebook não registra essa versão.

### 8.2. Criar o ambiente virtual

No terminal, a partir da raiz deste repositório, entre na pasta do projeto com `cd phishing-detector`. Em seguida:

```powershell
python -m venv .venv
```

Ativar o ambiente virtual no Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

### 8.3. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

### 8.4. Executar a aplicação

```powershell
python app.py
```

Acesse no navegador:

http://127.0.0.1:5000

O servidor Flask é utilizado localmente para desenvolvimento
e demonstração acadêmica.

## 9. Como utilizar

1. Abra a aplicação no navegador.
2. Informe uma URL completa, começando com `http://` ou `https://`.
3. Selecione um classificador ou **Comparar todos os modelos**.
4. Clique em "Analisar URL".
5. Visualize a classificação individual ou os quatro resultados, com tempos de previsão no modo comparativo.

O MLP é selecionado por padrão na interface.

A aplicação valida a estrutura básica da URL antes de
realizar a extração de características.

## 10. Limitações

A classificação é realizada exclusivamente a partir de
características lexicais da URL.

O sistema não acessa o conteúdo das páginas, não verifica
a existência dos sites e não executa análise de malware.

As previsões não garantem que uma URL classificada como
legítima seja segura.

O desempenho observado no conjunto de teste também não
garante resultados equivalentes em URLs externas ao dataset.

## 11. Considerações finais

O projeto permitiu comparar diferentes algoritmos de
classificação, aplicar técnicas de otimização de
hiperparâmetros e validação cruzada, além de integrar
modelos treinados a uma aplicação web.

O MLP apresentou o melhor desempenho geral no conjunto
de teste, enquanto a aplicação Flask possibilitou
demonstrar o funcionamento prático dos quatro modelos.

O sistema possui finalidade acadêmica e experimental.

## 12. Modos da interface e comparação dos quatro modelos

### Modo individual

Informe uma URL completa, selecione KNN, Decision Tree, Naive Bayes ou MLP e clique em **Analisar URL**. A MLP aparece selecionada por padrão. A resposta individual exibe a URL, o classificador e a classe prevista. O backend também calcula o tempo em milissegundos, mas o HTML atual não o exibe no resultado individual.

### Comparação simultânea na tela

Selecione **Comparar todos os modelos** e clique em **Analisar URL**. O servidor extrai as features uma única vez e envia a mesma entrada aos quatro pipelines. A interface apresenta um cartão por modelo, com a classe e o tempo de previsão em milissegundos.

A comparação é conjunta na interface, mas as chamadas de previsão são **sequenciais**, dentro da mesma requisição. Não há processamento paralelo, votação majoritária ou ensemble. Divergências entre modelos permanecem visíveis.

O tempo mede somente `modelo.predict(entrada)`, usando `time.perf_counter()`, com arredondamento para duas casas decimais. Não inclui extração das features, validação da URL, rede ou renderização. Uma medição isolada não representa um benchmark de latência.

A validação aceita esquemas HTTP/HTTPS, verifica hostname e porta, rejeita espaços e credenciais embutidas. Endereços IP são aceitos. Para domínios, exige ponto e rótulos ASCII válidos. Essa validação verifica estrutura, sem confirmar existência ou segurança.

## 13. Reprodução do treinamento e exportação

Execute as células do notebook `Projeto_Phishing_Detection.ipynb` em ordem no Google Colab. Ele instala `ucimlrepo` e `tldextract`, carrega o dataset com `fetch_ucirepo(id=967)` e recalcula as 16 features a partir das URLs. O carregamento do dataset e a instalação de pacotes exigem acesso à internet.

O notebook exporta os pipelines para a pasta **`modelos/`** e gera `modelos_phishing.zip`. Extraia o conteúdo do ZIP para a pasta **`models/`** ao lado de `app.py`. A aplicação espera diretamente:

```text
models/knn.joblib
models/decision_tree.joblib
models/naive_bayes.joblib
models/mlp.joblib
models/features.joblib
```

`features.joblib` armazena a lista ordenada das colunas. O Flask reorganiza a entrada com essa lista antes da previsão. Preserve os pipelines completos, inclusive o `StandardScaler` dos modelos que o utilizam. A extração no notebook e em `extrator.py` deve permanecer equivalente.

O `requirements.txt` fornecido fixa `scikit-learn==1.6.1`. O README original informa que essa também é a versão de exportação. O notebook não imprime sua versão de execução, portanto essa informação não foi validada pela saída salva. Use versões compatíveis entre treinamento e inferência e carregue somente arquivos joblib de origem confiável.

### Instalação local no Windows sem ativação do ambiente

Na pasta do projeto, com Python instalado:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Abra [a aplicação local](http://127.0.0.1:5000). Essa alternativa usa diretamente o Python do ambiente e dispensa alterar a política de execução do PowerShell. As versões fixadas no arquivo de dependências devem estar disponíveis para a versão do Python e o sistema utilizados. A instalação das dependências não foi executada na preparação desta documentação.

O `app.py` carrega os quatro modelos e a lista de features ao iniciar. Arquivos ausentes, pastas incorretas ou versões incompatíveis impedem a inicialização. O servidor usa `debug=True` e deve permanecer restrito ao desenvolvimento e à demonstração local.

## 14. Hiperparâmetros e validação cruzada detalhada

As duas separações usam estratificação e `random_state=42`. A busca usa `StratifiedKFold(n_splits=3, shuffle=True, random_state=42)`, `scoring="f1_macro"` e `n_jobs=-1` sobre a amostra de 20.000 URLs (11.459 legítimas e 8.541 de phishing).

| Modelo | Grade da busca | Melhor configuração | F1 macro na busca |
|---|---|---|---:|
| KNN | n_neighbors: 3, 5, 7, 9, 11; weights: uniform, distance | n_neighbors=3, weights=distance | 0,9872 |
| Decision Tree | max_depth: 5, 10, 20, None; min_samples_split: 2, 10 | max_depth=20, min_samples_split=2 | 0,9893 |
| Naive Bayes | var_smoothing: 1e-9, 1e-8, 1e-7 | var_smoothing=1e-7 | 0,8961 |
| MLP | hidden_layer_sizes: (32,), (32,16); alpha: 0.0001, 0.01 | hidden_layer_sizes=(32,16), alpha=0.0001 | 0,9935 |

MLP utiliza `max_iter=500`, `early_stopping=True` e `random_state=42`. Decision Tree também fixa `random_state=42`.

A avaliação posterior usa `StratifiedKFold(n_splits=5, shuffle=True, random_state=123)` na mesma amostra. Valores abaixo reproduzem a saída salva com quatro casas decimais, em escala de 0 a 1.

| Modelo | Acurácia (média ± DP) | Precisão macro (média ± DP) | Recall macro (média ± DP) | F1 macro (média ± DP) |
|---|---:|---:|---:|---:|
| KNN | 0,9880 ± 0,0013 | 0,9884 ± 0,0013 | 0,9871 ± 0,0014 | 0,9877 ± 0,0013 |
| Decision Tree | 0,9905 ± 0,0018 | 0,9905 ± 0,0016 | 0,9901 ± 0,0020 | 0,9903 ± 0,0018 |
| Naive Bayes | 0,9020 ± 0,0047 | 0,9232 ± 0,0038 | 0,8865 ± 0,0055 | 0,8963 ± 0,0052 |
| MLP | 0,9944 ± 0,0009 | 0,9947 ± 0,0008 | 0,9937 ± 0,0011 | 0,9942 ± 0,0009 |

DP é o desvio padrão entre os folds, calculado com `valores.std()` do NumPy (ddof=0). Não é intervalo de confiança. A busca e a avaliação posterior reutilizam a mesma amostra, portanto não constituem validação cruzada aninhada. O teste reservado permanece separado desse processo.

## 15. Teste, tempos e matrizes de confusão

Após a seleção, o notebook clona os melhores pipelines e treina novamente com as 188.296 URLs de desenvolvimento. O teste tem 20.104 URLs de phishing e 26.970 legítimas.

| Modelo | Recall phishing | Treino final (s) | Previsão das 47.074 URLs (s) |
|---|---:|---:|---:|
| MLP | 0,9910 | 16,30 | 0,0710 |
| Decision Tree | 0,9916 | 0,39 | 0,0124 |
| KNN | 0,9898 | 0,08 | 77,5121 |
| Naive Bayes | 0,7805 | 0,10 | 0,0206 |

Esses tempos pertencem à execução salva do notebook. Não são médias de repetições e não equivalem ao tempo de uma URL na interface. O notebook não informa hardware suficiente para uma comparação controlada.

Matrizes transcritas dos gráficos originais. Linhas representam a classe real e colunas a previsão, na ordem **[Phishing (0), Legítimo (1)]**:

| Modelo | Phishing → Phishing | Phishing → Legítimo | Legítimo → Phishing | Legítimo → Legítimo |
|---|---:|---:|---:|---:|
| KNN | 19.898 | 206 | 50 | 26.920 |
| Decision Tree | 19.936 | 168 | 61 | 26.909 |
| Naive Bayes | 15.692 | 4.412 | 176 | 26.794 |
| MLP | 19.923 | 181 | 22 | 26.948 |

A MLP apresenta o maior F1 macro no teste, enquanto a árvore deixa passar menos URLs de phishing neste conjunto. Essa diferença não demonstra significância estatística, pois o notebook não realiza esse teste.

## 16. Limitações adicionais e próximos passos

- A separação aleatória controla duplicatas exatas de URL. Não há agrupamento explícito por domínio ou separação temporal, o que limita conclusões sobre domínios inéditos e ataques futuros.
- Padrões do PhiUSIIL podem diferir de URLs reais posteriores. O desempenho no teste não garante o mesmo comportamento fora dessa distribuição.
- HTTPS é somente um dos indicadores lexicais. Sua presença não comprova legitimidade.
- O extrator não consulta DNS, reputação, redirecionamentos, certificados ou conteúdo da página e não analisa malware.
- Os modelos retornam classes. A interface não fornece probabilidade calibrada ou grau de confiança.
- A lista de sufixos depende da versão instalada de `tldextract`. Alterações no extrator ou nas dependências devem ser acompanhadas de nova validação e, quando necessário, novo treinamento.
- Próximos experimentos: validação externa, separação por domínio ou período e medição repetida de latência em ambiente controlado.

## 17. Fontes dos resultados

Dados extraídos de `Projeto_Phishing_Detection.ipynb`: células 1 e 4–5 (base e limpeza), 8 e 14–16 (features e verificações), 12–13 (partições), 18–23 (pipelines, busca, gráfico KNN e CV), 27–32 (treino final, teste, matrizes e relatórios), 34–37 (exportação). Comportamento da aplicação conferido em `app.py`, `extrator.py`, `templates/index.html`, `static/style.css` e `requirements.txt` fornecidos pelo autor.

Os resultados são os da execução salva. Não houve novo treinamento nem preenchimento de valores não registrados. A mensagem “Quantidade de features: 39” na célula 10 usa `len(url_teste)` e mede caracteres da URL de exemplo. O modelo utiliza **16 features**, confirmado pelo dicionário do extrator e por `X_treino.shape == (20000, 16)`.
