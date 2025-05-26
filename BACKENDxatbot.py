# Instal·lació de les biblioteques necessàries
!pip install -U flask flask-cors pyngrok google-genai requests beautifulsoup4

from flask import Flask, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from google import genai
import os


########### CONFIGURACIÓ DE L'API ###########

GOOGLE_API_KEY = "AIzaSyAa0FfHe2VLs8GueXZo16ajdQCEGC5TCzE"
if not GOOGLE_API_KEY:
    raise ValueError("⚠️ No s'ha trobat la clau API. Configura-la abans d'executar el programa.")

# Crear el client de GenAI amb la clau API
client = genai.Client(api_key=GOOGLE_API_KEY)


########### WEB SCRAPING DE TOT EL DOMINI ###########

BASE_URL = "https://jcanet.inscastellbisbal.net/"

def es_intern(url, base):
    """Retorna True si l'URL és interna al domini base."""
    parsed_base = urlparse(base)
    parsed_url = urlparse(url)
    return parsed_url.netloc == "" or parsed_url.netloc == parsed_base.netloc

def obtenir_contingut_pagina(url):
    """Extreu els paràgrafs d'una pàgina donada."""
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            soup = BeautifulSoup(resposta.text, 'html.parser')
            paragrafs = soup.find_all('p')
            text = "\n".join([p.get_text().strip() for p in paragrafs if p.get_text().strip()])
            return text
        else:
            return ""
    except Exception as e:
        return ""

def obtenir_contingut_domain(base_url, max_pagines=50):
    """Recorre totes les subpàgines internes del domini i retorna el contingut combinat."""
    visited = set()
    to_visit = [base_url]
    contingut_total = ""
    count = 0

    while to_visit and count < max_pagines:
        url_actual = to_visit.pop(0)
        if url_actual in visited:
            continue
        visited.add(url_actual)
        print(f"Visitant: {url_actual}")
        text = obtenir_contingut_pagina(url_actual)
        if text:
            contingut_total += text + "\n"
        count += 1

        # Trobar enllaços interns
        try:
            resposta = requests.get(url_actual)
            if resposta.status_code == 200:
                soup = BeautifulSoup(resposta.text, 'html.parser')
                enllacos = soup.find_all("a", href=True)
                for a in enllacos:
                    href = a["href"]
                    url_completa = urljoin(base_url, href)
                    if es_intern(url_completa, base_url) and url_completa not in visited:
                        to_visit.append(url_completa)
        except Exception as e:
            continue

    return contingut_total

# Obtenir el contingut de tot el domini (subpàgines incloses)
contingut_web = obtenir_contingut_domain(BASE_URL)
print("Contingut extret (primeres 500 lletres):\n", contingut_web[:500], "...\n")


########### CONFIGURACIÓ DE FLASK ###########

app = Flask(__name__)
CORS(app)  # Permet sol·licituds des de qualsevol origen (necessari per JavaScript)

# Ruta per gestionar les sol·licituds del xatbot
@app.route("/chat", methods=["POST"])
def chat():
    try:
        dades = request.get_json()
        missatge_usuari = dades.get("message", "")

        if not missatge_usuari:
            return jsonify({"response": "Si us plau, escriu alguna cosa!"})

        # El xatbot només respon consultes relacionades amb el domini (reptes, institut, etc.)
        prompt_complet = f"Només respon preguntes sobre els reptes, els projectes i la informació de l'institut. {missatge_usuari}"
        resposta = client.chats.create(
            model="gemini-2.0-flash",
            config=genai.types.GenerateContentConfig(
                system_instruction=contingut_web[:1000],
                temperature=0.7,
                max_output_tokens=200
            )
        ).send_message(prompt_complet)

        return jsonify({"response": resposta.text.strip()})
    except Exception as e:
        return jsonify({"response": f"⚠️ Error en la comunicació amb Gemini: {e}"})

########### EXPOSAR EL SERVIDOR AMB NGROK ###########

NGROK_AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

port = 5000
public_url = ngrok.connect(port).public_url
print(f"🌍 Servidor exposat a: {public_url}")

if __name__ == "__main__":
    app.run(port=port)
