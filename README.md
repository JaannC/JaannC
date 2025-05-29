# 🤖 Xatbot IPOP
## 📖 Descripció
Xatbot intel·ligent que s'integra a un portfoli en WordPress i respon segons la informació de la web personal.

Permet personalitzar el comportament del xatbot, fer web scraping i millorar el model mitjançant API.
## 🎯 Objectius
Desenvolupar un xatbot que respongui segons el contingut d'una web.

Integrar-lo a WordPress com un widget.

Fer servir Google Gemini API per generar respostes.

Aprendre a gestionar API Keys i seguretat bàsica.

Utilitzar web scraping per extreure informació d'una pàgina.

## 📦 Requisits
Abans d’iniciar el projecte, assegura’t de tenir instal·lats:

Python 3.x (python --version)

Google Gemini API Key (Obtenir-la a Google AI Studio)

Google Colab o entorn local amb biblioteques necessàries

Un entorn de proves per al frontend (Google Sites, WordPress, etc.)

## 📂 Estructura del projecte

📦 xatbot-ipop 

  ┣ 📂 src # Codi font del backend ┃ 

    ┣ 📜 main.ipynb # Backend principal del xatbot ┃ 

    ┣ 📜 chatbot.ipynb # Lògica del chatbot (instruccions, API) ┃ 

    ┣ 📜 scraper.ipynb # Web scraping per extreure informació ┃ 

    ┗ 📜 config.ipynb # Configuració de la API i altres paràmetres 

  ┣ 📂 frontend # Widget frontend (HTML, CSS, JS) ┃ 

    ┗ 📜 index.html # Integració al WordPress 

  ┣ 📂 docs # Documentació del projecte 

    ┣ 📜 requirements.txt # Biblioteques necessàries 

    ┣ 📜 README.md # Aquest fitxer 

    ┣ 📜 CHANGELOG.md # Registre de versions i canvis 

    ┗ 📜 CONTRIBUTING.md # Guia per col·laboradors


## 🔧 Instal·lació

1️⃣ Instal·lació de biblioteques i mòduls (Backend)

2️⃣ Configuració de l’API Key

3️⃣ Executar el xatbot


## 🔁 Fluxe de dades

🔽 El backend processa la consulta de l’usuari.

🔽 Recull informació del WordPress (opcional, via web scraping).

🔽 Envia la resposta generada pel model cap al frontend.

🔽 El frontend mostra la resposta a l’usuari en un widget.


## 👨‍💻 Contribució
Si vols contribuir, segueix les normes indicades a CONTRIBUTING.md.
