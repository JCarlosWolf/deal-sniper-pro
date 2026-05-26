# DealSniper Pro: Intelligent Market Monitoring & Real-Time Opportunity Detection System

**Developed by:** José Carlos Lobo  
**Main Stack:** Python | Playwright (Browser Automation) | BeautifulSoup | Telegram Bot API | JSON  

---

## Language / Idioma

* For technical and architectural documentation: 👉 **[Read in English](#english-version)**
* Para el caso de estudio orientado a negocio: 👉 **[Leer en Español](#spanish-version)**

---

<div id="english-version"></div>

# English Version

## 🎯 Executive Summary & Business Value

In hyper-competitive industries—ranging from e-commerce and flipping to real estate and corporate asset acquisition—having information early is everything. Manually checking marketplaces for listings, price drops, or undervalued assets is incredibly inefficient, eats up valuable labor hours, and is prone to human oversight. The cost of arriving late to a market deal means missing out on profits altogether.

DealSniper Pro is a data intelligence and automation system built in Python. Its core purpose is to fully automate market scouting: it runs scheduled checks across platforms using robotic browser emulators, extracts complex listing data, cleans the noise out via custom business logic, and fires instant push alerts to key decision channels (Telegram) the second an opportunity hits the market.

### 🏢 High-Value Corporate Use Cases:
* Competitor Pricing Intelligence: Keeping real-time track of competitor prices to fuel dynamic pricing models.
* Automated Asset & Lead Sourcing: Scouting industry portals to catch undervalue properties, equipment, or machinery ahead of the general public.
* Critical Inventory Alerts: Getting early signals when rare, discontinued, or critical stock becomes available on secondary markets.

---

## 🚀 Key Features & Enterprise Value

* Advanced Industrial Web Scraping: Powers through anti-bot systems by integrating Playwright to run headless browsers that replicate authentic human interactions. This guarantees extraction continuity without dealing with IP blocks.
* Smart Noise Filtering: Backed by an evaluation service layer that handles data cleanup, discarding accessory items or unrelated spam to ensure alerts trigger only on true price mismatches.
* Cache-Driven Duplicate Prevention: An optimized JSON-based tracking cache ensures listings are processed only once, protecting your system metrics and keeping workflows free from repetitive alert spam.
* Instant Notification Flow: Complete integration with the Telegram Bot API, piping structured insights (Product, Target Price, Direct Link) straight to your team's mobile devices within seconds of publication.

---

## 🛠️ Technical Layout & Modular Structure

Engineered using an organized, decoupled layout that allows developers to add new portals or custom filtration services seamlessly:

Layout del Proyecto:
deal_sniper/
│
├── app/
│   ├── main.py       # Main orchestrator and system entry point
│   ├── scraper/      # Browser automation and request handler (Playwright Engine)
│   ├── parser/       # Data extractor and text sanitizer (BeautifulSoup)
│   ├── services/     # Price evaluation and alert logic triggers
│   ├── storage/      # Local caching structure preventing alert duplicates (JSON)
│   ├── utils/        # General formatting helpers
│   └── config/       # Environment secure credential manager
│
├── data/             # Historical file log storage
├── requirements.txt  # Project library dependencies
└── README.md

---

## 📋 Installation & Local Setup

### Prerequisites
* Python 3.10+
* A Telegram Account for alert reception

### 1. Environment Deployment
Comandos para ejecutar en consola:
git clone [https://github.com/JCarlosWolf/deal-sniper-pro.git](https://github.com/JCarlosWolf/deal-sniper-pro.git)
cd deal-sniper-pro
python -m venv .venv

* Activar entorno virtual:
Windows: .venv\Scripts\activate
Linux/macOS: source .venv/bin/activate

Instalar dependencias y navegadores:
pip install -r requirements.txt
playwright install

### 2. Target Configuration (.env)
Crear un archivo .env en la carpeta raíz para apuntar a tus credenciales:
TELEGRAM_TOKEN=your_bot_token_here
CHAT_ID=your_target_chat_id_here

### 3. Execution
Comando para arrancar el sistema:
python -m app.main

---

## ✉️ Contact & Automation Consulting

If your team is wasting hours manually scouting websites, or you need custom software bots to bridge web data directly with your communication apps:

* Developer: José Carlos Lobo
* Specialty: Web Scraping, Core Automation Workflows, & Python Backend Infrastructures.
* LinkedIn: [www.linkedin.com/in/josé-carlos-lobo-473b458a](https://www.linkedin.com/in/josé-carlos-lobo-473b458a)

---
---

<div id="spanish-version"></div>

# Versión en Español: Caso de Estudio de Negocio

## 🎯 ¿Qué es DealSniper Pro? (Perspectiva de Negocio)

En mercados altamente competitivos (desde el e-commerce y el reselling hasta el sector inmobiliario o la compraventa de activos), la información oportuna lo es todo. Revisar plataformas de anuncios o marketplaces manualmente para encontrar oportunidades de negocio, subastas o productos por debajo de su precio de mercado es una tarea ineficiente, propensa a errores y que consume cientos de horas hombre. El coste de oportunidad de llegar tarde a una oferta suele significar perder el negocio.

DealSniper Pro es un sistema de automatización e inteligencia competitiva desarrollado en Python. Su función es automatizar por completo la vigilancia del mercado: rastrea plataformas de forma continua utilizando técnicas avanzadas de navegación robótica, extrae la información, filtra el ruido innecesario mediante lógica de negocio y, si detecta una desviación de precio atractiva, envía una alerta instantánea a los canales de toma de decisiones (Telegram).

### 🏢 Casos de Uso Aplicables a Empresas y Profesionales:
* Monitoreo de Competencia: Vigilancia de precios de competidores en tiempo real para ajustar estrategias de pricing dinámico.
* Captación de Leads y Activos: Rastreo automático de portales sectoriales para detectar ofertas inmobiliarias, vehículos o maquinaria por debajo de su valor promedio.
* Inteligencia de Producto: Alertas tempranas sobre la aparición de inventario crítico o descatalogado en el mercado secundario.

---

## 🚀 Características Clave y Valor Empresarial

* Extracción Avanzada y Anti-Bot (Scraping de Nivel Industrial): Integra Playwright para emular el comportamiento humano en navegadores (Headless Browser). Esto permite saltar las barreras de protección de los marketplaces modernos y asegurar la continuidad del rastreo sin bloqueos.
* Filtrado Inteligente de Datos (Ruido Cero): Cuenta con un motor de reglas de negocio que limpia los datos extraídos, eliminando listados irrelevantes o accesorios no deseados para enviar alertas únicamente cuando existe una oportunidad real.
* Prevención de Duplicados (Eficiencia Operativa): Un sistema de persistencia en caché evita el reprocesamiento y el envío duplicado de alertas, optimizando el uso de recursos y el tiempo del equipo de análisis.
* Canal de Alertas Instantáneas: Integración nativa con la API de bots de Telegram, entregando la información estructurada (Producto, Precio, Enlace Directo) en el móvil del tomador de decisiones en menos de 3 segundos desde su publicación.

---

## ✉️ Contacto y Consultoría de Automatización

* Desarrollador: José Carlos Lobo
* LinkedIn: [www.linkedin.com/in/josé-carlos-lobo-473b458a](https://www.linkedin.com/in/josé-carlos-lobo-473b458a)
