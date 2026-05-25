# DealSniper Pro: Sistema Inteligente de Monitorización de Mercados y Captación de Oportunidades en Tiempo Real

**Desarrollado por:** José Carlos Lobo  
**Stack Principal:** Python | Playwright (Browser Automation) | BeautifulSoup | Telegram Bot API | JSON  

---

## 🎯 ¿Qué es DealSniper Pro? (Perspectiva de Negocio)

En mercados altamente competitivos (desde el e-commerce y el *reselling* hasta el sector inmobiliario o la compraventa de activos), la información oportuna lo es todo. Revisar plataformas de anuncios o marketplaces manualmente para encontrar oportunidades de negocio, subastas o productos por debajo de su precio de mercado es una tarea ineficiente, propensa a errores y que consume cientos de horas hombre. El coste de oportunidad de llegar tarde a una oferta suele significar perder el negocio.

**DealSniper Pro** es un sistema de automatización e inteligencia competitiva desarrollado en Python. Su función es **automatizar por completo la vigilancia del mercado**: rastrea plataformas de forma continua utilizando técnicas avanzadas de navegación robótica, extrae la información, filtra el ruido innecesario mediante lógica de negocio y, si detecta una desviación de precio atractiva, envía una alerta instantánea a los canales de toma de decisiones (Telegram).

### 🏢 Casos de Uso Aplicables a Empresas y Profesionales:
* **Monitoreo de Competencia:** Vigilancia de precios de competidores en tiempo real para ajustar estrategias de pricing dinámico.
* **Captación de Leads y Activos:** Rastreo automático de portales sectoriales para detectar ofertas inmobiliarias, vehículos o maquinaria por debajo de su valor promedio.
* **Inteligencia de Producto:** Alertas tempranas sobre la aparición de inventario crítico o descatalogado en el mercado secundario.

---

## 🚀 Características Clave y Valor Empresarial

* **Extracción Avanzada y Anti-Bot (Scraping de Nivel Industrial):** Integra **Playwright** para emular el comportamiento humano en navegadores (Headless Browser). Esto permite saltar las barreras de protección de los marketplaces modernos y asegurar la continuidad del rastreo sin bloqueos.
* **Filtrado Inteligente de Datos (Ruido Cero):** Cuenta con un motor de reglas de negocio que limpia los datos extraídos, eliminando listados irrelevantes o accesorios no deseados para enviar alertas únicamente cuando existe una oportunidad real.
* **Prevención de Duplicados (Eficiencia Operativa):** Un sistema de persistencia en caché evita el reprocesamiento y el envío duplicado de alertas, optimizando el uso de recursos y el tiempo del equipo de análisis.
* **Canal de Alertas Instantáneas:** Integración nativa con la API de bots de **Telegram**, entregando la información estructurada (`Producto`, `Precio`, `Enlace Directo`) en el móvil del tomador de decisiones en menos de 3 segundos desde su publicación.

---

## 🛠️ Arquitectura Técnica y Estructura del Proyecto

Diseñado bajo una arquitectura modular y escalable que facilita la integración de nuevos marketplaces o reglas de filtrado sin alterar el núcleo del sistema:

deal_sniper/
│
├── app/
│   ├── main.py       # Punto de entrada y orquestador del servicio de monitoreo
│   ├── scraper/      # Módulo de automatización de navegador (Playwright Engine)
│   ├── parser/       # Extracción y estructuración de datos crudos (BeautifulSoup)
│   ├── services/     # Lógica de detección de desviaciones de precio y alertas
│   ├── storage/      # Sistema de caché local para prevención de duplicados (JSON)
│   ├── utils/        # Herramientas de soporte y formateo de datos
│   └── config/       # Gestión segura de credenciales y variables de entorno
│
├── data/             # Historial de registros procesados
├── requirements.txt  # Dependencias del sistema
└── README.md


---

## 📋 Guía de Instalación y Configuración

### Requisitos Previos
* Python 3.10+
* Cuenta de Telegram para la recepción de alertas

### 1. Clonar e Instalar Dependencias
```bash
git clone [https://github.com/JCarlosWolf/deal-sniper-pro.git](https://github.com/JCarlosWolf/deal-sniper-pro.git)
cd deal-sniper-pro
python -m venv .venv
Activar entorno virtual:

Windows: .venv\Scripts\activate

Linux/macOS: source .venv/bin/activate

Bash
pip install -r requirements.txt
# Instalar los navegadores necesarios para Playwright
playwright install
2. Configuración de Credenciales (.env)
Crea un archivo .env en la raíz del proyecto para conectar el sistema con tu canal de alertas:

Fragmento de código
TELEGRAM_TOKEN=tu_token_de_bot_aqui
CHAT_ID=tu_chat_id_de_telegram_aqui
3. Ejecutar el Monitorizador
Bash
python -m app.main
📸 Formato de Alerta Automatizada (Visualización de Datos)
El sistema entrega la información lista para la acción comercial:

Plaintext
🔥 OPORTUNIDAD DETECTADA
🔎 Producto: Fender Jazz Bass Mexico
💰 Precio Objetivo: 450 €
🔗 Enlace Directo: [https://marketplace-url.com/item/12345](https://marketplace-url.com/item/12345)
✉️ Contacto y Consultoría de Automatización
Si tu empresa pierde horas vigilando portales web, necesitas extraer datos masivos de la competencia de manera ética y segura, o buscas automatizar flujos que conecten la web con tus herramientas de comunicación:

Desarrollador: José Carlos Lobo

Especialidad: Automatización de Procesos, Extracción de Datos (Web Scraping) y Arquitecturas Backend con Python.

LinkedIn: www.linkedin.com/in/josé-carlos-lobo-473b458a

Automated marketplace monitoring system that detects underpriced opportunities in real time and sends instant structured alerts.
