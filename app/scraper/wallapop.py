import logging
from playwright.sync_api import sync_playwright


def fetch_wallapop_results(query: str) -> list:
    """
    Scraper de Wallapop usando Playwright + extracción robusta del DOM.
    """

    url = f"https://es.wallapop.com/app/search?keywords={query.replace(' ', '%20')}"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(url, timeout=30000)

            # Esperar a que haya resultados visibles
            page.wait_for_selector("a[href*='/item/']", timeout=15000)

            items = page.evaluate("""
                () => {
                    const results = [];
                    const elements = document.querySelectorAll("a[href*='/item/']");

                    elements.forEach(el => {

                        const link = el.href;
                        const rawText = el.innerText || "";

                        if (!rawText) return;

                        // 🔥 LIMPIEZA DE TEXTO
                        const lines = rawText
                            .split("\\n")
                            .map(l => l.trim())
                            .filter(l => l.length > 0);

                        // ❌ eliminar basura típica
                        const cleanLines = lines.filter(l =>
                            !l.includes("/") && 
                            !l.toLowerCase().includes("destacado")
                        );

                        // 💰 buscar precio
                        let price = 0;

                        cleanLines.forEach(line => {
                            const match = line.match(/\\d+[,.]?\\d*/);
                            if (match) {
                                const val = parseFloat(match[0].replace(",", "."));
                                if (val > price) price = val;
                            }
                        });

                        // 🧠 título = línea más larga sin número
                        let title = "";

                        cleanLines.forEach(line => {
                            if (!line.match(/\\d/)) {
                                if (line.length > title.length) {
                                    title = line;
                                }
                            }
                        });

                        if (title && price > 0 && link) {
                            results.push({
                                title: title,
                                price: price,
                                link: link
                            });
                        }
                    });

                    return results;
                }
            """)

            browser.close()

            logging.info(f"[SCRAPER DOM FIXED] {len(items)} items capturados → {query}")

            return items

    except Exception as e:
        logging.error(f"[SCRAPER ERROR] {query} → {e}")
        return []