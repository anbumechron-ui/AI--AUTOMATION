from playwright.sync_api import sync_playwright

HEADLESS = False  # Change to True after testing


with sync_playwright() as p:

    # Launch installed Google Chrome
    browser = p.chromium.launch(
        channel="chrome",
        headless=HEADLESS
    )

    page = browser.new_page(
        viewport={"width": 1366, "height": 768}
    )

    try:
        # Open Cricbuzz
        print("Opening Cricbuzz...")
        page.goto(
            "https://www.cricbuzz.com/",
            wait_until="domcontentloaded"
        )

        # Wait until cricket score text appears
        page.wait_for_function(
            """() => {
                const text = document.body.innerText;
                return /\\b\\d{1,3}\\s*[/\\-]\\s*\\d{1,2}\\b/.test(text);
            }""",
            timeout=60000
        )

        # Inspect the page and discover a matching element
        element_info = page.evaluate("""() => {
            const scorePattern =
                /\\b\\d{1,3}\\s*[/\\-]\\s*\\d{1,2}\\b/;

            const elements = [...document.querySelectorAll("body *")];

            const candidates = elements.filter(el => {
                const text = (el.innerText || "").trim();
                const rect = el.getBoundingClientRect();
                const style = getComputedStyle(el);

                return text.length > 0
                    && text.length < 150
                    && scorePattern.test(text)
                    && rect.width > 0
                    && rect.height > 0
                    && style.display !== "none"
                    && style.visibility !== "hidden";
            });

            candidates.sort((a, b) =>
                a.innerText.trim().length -
                b.innerText.trim().length
            );

            if (!candidates.length) return null;

            const el = candidates[0];
            const parts = [];

            let current = el;

            while (current && current !== document.body) {
                let part = current.tagName.toLowerCase();

                if (current.id) {
                    part += "#" + CSS.escape(current.id);
                    parts.unshift(part);
                    break;
                }

                const parent = current.parentElement;

                if (parent) {
                    const siblings = [...parent.children].filter(
                        child => child.tagName === current.tagName
                    );

                    if (siblings.length > 1) {
                        part += ":nth-of-type(" +
                            (siblings.indexOf(current) + 1) + ")";
                    }
                }

                parts.unshift(part);
                current = parent;
            }

            return {
                selector: parts.join(" > "),
                text: el.innerText.trim()
            };
        }""")

        if not element_info:
            raise Exception("Could not find a score element.")

        # Locate the element discovered from the live page
        score_element = page.locator(
            element_info["selector"]
        )

        # Wait for the discovered element
        score_element.wait_for(
            state="visible",
            timeout=30000
        )

        # Print the score
        score = score_element.inner_text().strip()

        print("\nDiscovered selector:")
        print(element_info["selector"])

        print("\nCricbuzz score:")
        print(score)

        # Save screenshot
        page.screenshot(
            path="score.png",
            full_page=True
        )

        print("\nScreenshot saved as score.png")

    finally:
        browser.close()
