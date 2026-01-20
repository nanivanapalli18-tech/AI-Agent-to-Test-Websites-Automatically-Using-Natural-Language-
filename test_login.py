from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(r"file:///C:/Users/Nani/OneDrive/Desktop/AI_Agent_Project/login1.html")
    # Wait for the page to be filled/submitted manually in the browser.
    # This waits up to 10 minutes for #message to contain non-empty text.
    page.wait_for_function(
        "() => { const el = document.querySelector('#message'); return el && el.textContent.trim().length > 0; }",
        timeout=600000
    )
    message = page.text_content("#message")
    assert message == "Login Successful", f"Unexpected message: {message}"
    print("✅ Login Successful verified")
    input("Press Enter to close the browser and exit...")
    browser.close()
