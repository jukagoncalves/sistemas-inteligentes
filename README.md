# Sistemas Inteligentes

Repositório das atividades e do projeto final da disciplina de Sistemas Inteligentes.

**Autor:** Juka Francis Pereira Gonçalves

## Organização

- [Atividades](atividades/): espaço para os notebooks e exercícios desenvolvidos ao longo da disciplina.
- [Phishing Detector](phishing-detector/): projeto final de classificação de URLs com KNN, Decision Tree, Naive Bayes e MLP, integrado a uma interface web com Flask.

```text
sistemas-inteligentes/
├── README.md
├── atividades/
│   └── README.md
└── phishing-detector/
    ├── README.md
    ├── Projeto_Phishing_Detection.ipynb
    ├── app.py
    ├── extrator.py
    ├── requirements.txt
    ├── models/
    ├── static/
    └── templates/
```

## Projeto final

O Phishing Detector utiliza o dataset PhiUSIIL e 16 características extraídas das URLs. Inclui treinamento e avaliação no Colab, modelos exportados e interface para classificação individual ou comparação dos quatro classificadores.

Consulte o [README do projeto](phishing-detector/README.md) para instalação, resultados e limitações. Execute os comandos de instalação e inicialização dentro de `phishing-detector/`.

## Atividades no Colab

Os notebooks das atividades poderão ser adicionados à pasta `atividades/`. Consulte as [orientações de envio](atividades/README.md).
