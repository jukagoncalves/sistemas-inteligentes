from urllib.parse import urlsplit
import ipaddress
import tldextract # identifica corretamente as partes de um dominio

# Utiliza a lista de sufixos incluída no pacote, sem precisar consultar a internet.
extrator_tld = tldextract.TLDExtract(
    suffix_list_urls=()
)

def extrair_features(url):

    url = str(url).strip() # strip remove espaços em branco e quebras de linha

    # Separar os componentes da URL
    partes = urlsplit(url)

    dominio = partes.hostname or ""

    # Identificar domínio, sufixo e subdomínios
    info_dominio = extrator_tld(dominio)

    # Verificar se o domínio é um endereço IP
    try:
        ipaddress.ip_address(dominio) # interpreta texto como ipv4 ou ipv6
        is_domain_ip = 1
    except ValueError:
        is_domain_ip = 0

    # Contar subdomínios
    subdominios = (
        info_dominio.subdomain.split(".")
        if info_dominio.subdomain
        else []
    )

    # Contar letras e dígitos
    num_letras = sum(c.isalpha() for c in url)
    num_digitos = sum(c.isdigit() for c in url)

    tamanho_url = len(url)

    # Evitar divisão por zero
    if tamanho_url > 0:
        proporcao_letras = num_letras / tamanho_url
        proporcao_digitos = num_digitos / tamanho_url
    else:
        proporcao_letras = 0
        proporcao_digitos = 0

    features = {
        "URLLength": tamanho_url,
        "DomainLength": len(dominio),
        "IsDomainIP": is_domain_ip,
        "TLDLength": len(info_dominio.suffix),
        "NoOfSubDomain": len(subdominios),
        "NoOfLetters": num_letras,
        "LetterRatio": proporcao_letras,
        "NoOfDigits": num_digitos,
        "DigitRatio": proporcao_digitos,
        "NoOfDots": url.count("."),
        "NoOfHyphens": url.count("-"),
        "NoOfEquals": url.count("="),
        "NoOfQMark": url.count("?"),
        "NoOfAmpersand": url.count("&"),
        "NoOfAt": url.count("@"),
        "IsHTTPS": int(partes.scheme.lower() == "https")
    }

    return features