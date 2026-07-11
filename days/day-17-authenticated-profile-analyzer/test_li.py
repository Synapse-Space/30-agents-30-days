from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(storage_state="storage_state.json")
    page = context.new_page()
    page.goto("https://www.linkedin.com/in/yuvraj3905/", wait_until="networkidle")
    print(page.title())
    print(page.locator("body").inner_text()[:500])
    browser.close()
