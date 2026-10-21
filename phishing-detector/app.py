from flask import Flask, render_template, request
import pandas as pd
import joblib
from pathlib import Path
from extrator import extrair_features
from urllib.parse import urlsplit
import ipaddress
import time

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
PASTA_MODELOS = BASE_DIR / "models"

arquivos_modelos = {
    "KNN": "knn.joblib",
    "Decision Tree": "decision_tree.joblib",
    "Naive Bayes": "naive_bayes.joblib",
    "MLP": "mlp.joblib"
}

modelos = {
    nome: joblib.load(PASTA_MODELOS / arquivo)
    for nome, arquivo in arquivos_modelos.items()
}

colunas = joblib.load(PASTA_MODELOS / "features.joblib")

def classificar_url(entrada, nome_modelo):
    """
    Executa a previsão de um classificador
    e mede o tempo de inferência.
    """
    modelo = modelos[nome_modelo]

    inicio = time.perf_counter()
    previsao = int(modelo.predict(entrada)[0])
    tempo_ms = (time.perf_counter() - inicio) * 1000

    return {
        "modelo": nome_modelo,
        "classe": "Phishing" if previsao == 0 else "Legítimo",
        "tempo_ms": round(tempo_ms, 2)
    }

def validar_url(url):
    if not url or any(c.isspace() for c in url):
        return False

    try:
        partes = urlsplit(url)

        if partes.scheme.lower() not in ("http", "https"):
            return False

        if not partes.netloc or not partes.hostname:
            return False

        # Acessar a porta também verifica se ela é válida.
        porta = partes.porta if False else partes.port
        dominio = partes.hostname

        if partes.username is not None or partes.password is not None:
            return False

        try:
            ipaddress.ip_address(dominio)
            return True
        except ValueError:
            pass

        if "." not in dominio:
            return False

        rotulos = dominio.split(".")

        if any(
            not rotulo
            or len(rotulo) > 63
            or rotulo.startswith("-")
            or rotulo.endswith("-")
            or not all(c.isascii() and (c.isalnum() or c == "-") for c in rotulo)
            for rotulo in rotulos
        ):
            return False

        return True

    except ValueError:
        return False

@app.route("/", methods=["GET", "POST"])
def index():

    resultado = None
    erro = None
    resultados_comparacao = None

    if request.method == "POST":

        url = request.form.get("url", "").strip()
        nome_modelo = request.form.get("modelo", "MLP")

        if not url:
            erro = "Informe uma URL."

        elif not validar_url(url):
            erro = (
                "URL inválida. Informe um endereço completo, "
                "como https://www.exemplo.com."
            )

        elif nome_modelo != "Todos" and nome_modelo not in modelos:
            erro = "Modelo inválido."

        else:
            try:
                features = extrair_features(url)

                entrada = pd.DataFrame([features])
                entrada = entrada[colunas]

                if nome_modelo == "Todos":

                    resultados_comparacao = []

                    for nome in modelos:
                        resultado_modelo = classificar_url(
                            entrada,
                            nome
                        )

                        resultados_comparacao.append(resultado_modelo)

                else:

                    resultado_modelo = classificar_url(
                        entrada,
                        nome_modelo
                    )

                    resultado = {
                        "url": url,
                        "modelo": nome_modelo,
                        "classe": resultado_modelo["classe"],
                        "tempo_ms": resultado_modelo["tempo_ms"]
                    }


            except (ValueError, TypeError):
                erro = "Não foi possível processar a URL."

    return render_template(
        "index.html",
        resultado=resultado,
        resultados_comparacao=resultados_comparacao,
        erro=erro,
        modelos=list(modelos.keys())
    )


if __name__ == "__main__":
    app.run(debug=True)