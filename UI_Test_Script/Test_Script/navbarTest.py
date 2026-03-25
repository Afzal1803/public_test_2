# Generated Playwright Tests for navbar
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from navbar_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0001
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Global URLs dictionary (update with actual URLs as needed)
urls: dict[str, str] = {
    "home": os.environ.get("TEST_HOME_URL", "https://your-website-homepage.com")
}
def test_logo_click_returns_user_to_home_page() -> None:
    """
    TC-0001: Logo Click Returns User to Home Page
    This test verifies that clicking the logo in the navigation bar always returns the user to the home page,
    regardless of their current location on the site.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        test_result: str = "FAILED"
        test_details: str = ""
        home_url: str = Utility.validate_and_convert_data(urls.get("home"), str)
        if not home_url:
            print("[ERROR] Home URL is not defined or invalid.")
            return
        # --- Enhanced dialog and console handling ---
        def handle_console_message(msg):
            Utility.log_console_message(msg)
        page.on("console", handle_console_message)
        try:
            # --- Given: Setup and navigation to initial state ---
            Utility.log_test_step("Navigate to the main page of the website.")
            navigation_success: bool = Utility.navigate_to_page(page, home_url, timeout=15000)
            if not navigation_success:
                raise Exception("Navigation to home page failed.")
            Utility.log_test_step("Wait for the main page to load and essential elements to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            # --- Accept cookies/pop-ups if present ---
            # (Assume a cookie banner with a button labeled 'Accept' may exist)
            cookie_accept_xpath: str = "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]"
            Utility.safe_wait_and_interact(page, f"xpath={cookie_accept_xpath}", action="click", timeout=5000, retries=1)
            # --- Step 1: The logo is visible in the top left corner of the navigation bar. ---
            Utility.log_test_step("Verify the logo is visible in the navigation bar.")
            logo_xpath: str = "//nav//a[contains(@class, 'logo') or contains(@href, '/') or contains(@aria-label, 'logo') or contains(@aria-label, 'home')]"
            logo_locator = page.locator(f"xpath={logo_xpath}")
            Utility.log_element_state("Logo", logo_locator, timeout=15000)
            Utility.retry_assertion(
                lambda: expect(logo_locator).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            # --- Step 2: Scroll down or navigate to another section (simulate navigation) ---
            Utility.log_test_step("Scroll down the page to ensure logo remains visible.")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            Utility.log_element_state("Logo after scroll", logo_locator, timeout=15000)
            Utility.retry_assertion(
                lambda: expect(logo_locator).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            # --- Step 3: Hover the mouse pointer over the logo. ---
            Utility.log_test_step("Hover over the logo and verify pointer changes to clickable.")
            logo_locator.hover()
            pointer_style: str = page.evaluate(
                """el => window.getComputedStyle(el).cursor""",
                logo_locator.element_handle(timeout=15000)
            )
            if pointer_style not in ["pointer", "hand"]:
                raise AssertionError(f"Logo cursor style is '{pointer_style}', expected 'pointer' or 'hand'.")
            # --- Step 4: Click on the logo. ---
            Utility.log_test_step("Click the logo to navigate to the home page.")
            Utility.retry_assertion(
                lambda: logo_locator.click(timeout=15000),
                retries=3,
                delay=2000
            )
            # --- Step 5: Observe the page content after redirection. ---
            Utility.log_test_step("Wait for redirection and verify main page content is displayed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            # --- Step 6: Confirm that the URL corresponds to the home page. ---
            Utility.log_test_step("Verify the browser URL reflects the main page address.")
            current_url: str = Utility.validate_and_convert_data(page.url, str)
            if not current_url.startswith(home_url):
                raise AssertionError(f"After logo click, URL is '{current_url}', expected to start with '{home_url}'.")
            test_result = "PASSED"
            test_details = "Logo click successfully returned user to the home page and all verifications passed."
        except AssertionError as ae:
            test_details = f"Assertion failed: {ae}"
            Utility.log_error(test_details)
            raise
        except Exception as e:
            test_details = f"Test failed due to unexpected error: {e}"
            Utility.log_error(test_details)
            raise
        finally:
            Utility.log_test_result(test_result, test_details)
            browser.close()
#---#

# Generated Playwright Tests for navbar
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from navbar_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0001
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Global URLs dictionary (update with actual URLs as needed)
urls: dict[str, str] = {
    "home": os.environ.get("TEST_HOME_URL", "https://your-website-homepage.com")
}
def test_logo_click_returns_user_to_home_page() -> None:
    """
    TC-0001: Logo Click Returns User to Home Page
    This test verifies that clicking the logo in the navigation bar always returns the user to the home page,
    regardless of their current location on the site.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        test_result: str = "FAILED"
        test_details: str = ""
        home_url: str = Utility.validate_and_convert_data(urls.get("home"), str)
        if not home_url:
            print("[ERROR] Home URL is not defined or invalid.")
            return
        # --- Enhanced dialog and console handling ---
        def handle_console_message(msg):
            Utility.log_console_message(msg)
        page.on("console", handle_console_message)
        try:
            # --- Given: Setup and navigation to initial state ---
            Utility.log_test_step("Navigate to the main page of the website.")
            navigation_success: bool = Utility.navigate_to_page(page, home_url, timeout=15000)
            if not navigation_success:
                raise Exception("Navigation to home page failed.")
            Utility.log_test_step("Wait for the main page to load and essential elements to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            # --- Accept cookies/pop-ups if present ---
            # (Assume a cookie banner with a button labeled 'Accept' may exist)
            cookie_accept_xpath: str = "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]"
            Utility.safe_wait_and_interact(page, f"xpath={cookie_accept_xpath}", action="click", timeout=5000, retries=1)
            # --- Step 1: The logo is visible in the top left corner of the navigation bar. ---
            Utility.log_test_step("Verify the logo is visible in the navigation bar.")
            logo_xpath: str = "//nav//a[contains(@class, 'logo') or contains(@href, '/') or contains(@aria-label, 'logo') or contains(@aria-label, 'home')]"
            logo_locator = page.locator(f"xpath={logo_xpath}")
            Utility.log_element_state("Logo", logo_locator, timeout=15000)
            Utility.retry_assertion(
                lambda: expect(logo_locator).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            # --- Step 2: Scroll down or navigate to another section (simulate navigation) ---
            Utility.log_test_step("Scroll down the page to ensure logo remains visible.")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            Utility.log_element_state("Logo after scroll", logo_locator, timeout=15000)
            Utility.retry_assertion(
                lambda: expect(logo_locator).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            # --- Step 3: Hover the mouse pointer over the logo. ---
            Utility.log_test_step("Hover over the logo and verify pointer changes to clickable.")
            logo_locator.hover()
            pointer_style: str = page.evaluate(
                """el => window.getComputedStyle(el).cursor""",
                logo_locator.element_handle(timeout=15000)
            )
            if pointer_style not in ["pointer", "hand"]:
                raise AssertionError(f"Logo cursor style is '{pointer_style}', expected 'pointer' or 'hand'.")
            # --- Step 4: Click on the logo. ---
            Utility.log_test_step("Click the logo to navigate to the home page.")
            Utility.retry_assertion(
                lambda: logo_locator.click(timeout=15000),
                retries=3,
                delay=2000
            )
            # --- Step 5: Observe the page content after redirection. ---
            Utility.log_test_step("Wait for redirection and verify main page content is displayed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            # --- Step 6: Confirm that the URL corresponds to the home page. ---
            Utility.log_test_step("Verify the browser URL reflects the main page address.")
            current_url: str = Utility.validate_and_convert_data(page.url, str)
            if not current_url.startswith(home_url):
                raise AssertionError(f"After logo click, URL is '{current_url}', expected to start with '{home_url}'.")
            test_result = "PASSED"
            test_details = "Logo click successfully returned user to the home page and all verifications passed."
        except AssertionError as ae:
            test_details = f"Assertion failed: {ae}"
            Utility.log_error(test_details)
            raise
        except Exception as e:
            test_details = f"Test failed due to unexpected error: {e}"
            Utility.log_error(test_details)
            raise
        finally:
            Utility.log_test_result(test_result, test_details)
            browser.close()
#---#

# Test Case 1 - TC-0018
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Global URLs dictionary (update as needed)
def test_products_page_category_first_last_selection() -> None:
    """
    TC-0018: Navigation and selection of first and last category items on Products Page Category List.
    Scenario: Ensures correct handling of selection for the first and last items in the category list.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", lambda msg: Utility.log_console_message(msg))
        test_passed: bool = False
        # XPaths for categories (must match the actual DOM structure)
        categories_xpath = [
            "//nav//ul/li[1]",  # BATMAN
            "//nav//ul/li[2]",  # WONDER WOMEN
            "//nav//ul/li[3]",  # SPIDY KIDS
            "//nav//ul/li[4]"   # HOMELANDER
        ]
        category_names = ["BATMAN", "WONDER WOMEN", "SPIDY KIDS", "HOMELANDER"]
        try:
            # --- GIVEN: Setup and navigation to initial state ---
            Utility.log_test_step("Navigating to the Products Page.")
            navigation_success = Utility.navigate_to_page(page, urls["products_page"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to the Products Page.")
                raise Exception("Navigation failed.")
            Utility.log_test_step("Waiting for page body to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.log_test_step("Validating essential elements using POM.")
            generated_page.validate_essential_elements()
            # --- WHEN: Ensure all categories are visible in order ---
            Utility.log_test_step("Verifying all four categories are displayed in order.")
            for idx, xpath in enumerate(categories_xpath):
                locator = page.locator(f"xpath={xpath}")
                Utility.log_element_state(f"Category '{category_names[idx]}'", locator, timeout=15000)
                expect(locator).to_be_visible(timeout=15000)
                actual_text = Utility.get_element_text(page, f"xpath={xpath}", timeout=15000)
                expected_text = Utility.validate_and_convert_data(category_names[idx], str)
                if actual_text.strip() != expected_text:
                    Utility.log_error(f"Category text mismatch: expected '{expected_text}', got '{actual_text.strip()}'")
                    raise AssertionError(f"Category order or label incorrect at position {idx+1}")
            # --- THEN: Identify and select first and last categories ---
            # First category: BATMAN
            first_category_xpath = categories_xpath[0]
            last_category_xpath = categories_xpath[-1]
            first_category_name = category_names[0]
            last_category_name = category_names[-1]
            Utility.log_test_step(f"Ensuring first category '{first_category_name}' is visible and selectable.")
            locator_first = page.locator(f"xpath={first_category_xpath}")
            Utility.log_element_state(f"First Category '{first_category_name}'", locator_first, timeout=15000)
            expect(locator_first).to_be_visible(timeout=15000)
            Utility.log_test_step(f"Ensuring last category '{last_category_name}' is visible and selectable.")
            locator_last = page.locator(f"xpath={last_category_xpath}")
            Utility.log_element_state(f"Last Category '{last_category_name}'", locator_last, timeout=15000)
            expect(locator_last).to_be_visible(timeout=15000)
            # --- WHEN: Click on the first category (BATMAN) ---
            Utility.log_test_step(f"Clicking on the first category '{first_category_name}'.")
            Utility.safe_wait_and_interact(page, f"xpath={first_category_xpath}", action="click", timeout=15000)
            # --- THEN: Verify BATMAN category is selected/highlighted ---
            Utility.log_test_step(f"Verifying '{first_category_name}' category is selected/highlighted.")
            def assert_first_selected():
                selected_class = locator_first.get_attribute("class")
                if not selected_class or "active" not in selected_class:
                    raise AssertionError(f"'{first_category_name}' category is not highlighted as selected.")
            Utility.retry_assertion(assert_first_selected, retries=3, delay=1000)
            # --- WHEN: Click on the last category (HOMELANDER) ---
            Utility.log_test_step(f"Clicking on the last category '{last_category_name}'.")
            Utility.safe_wait_and_interact(page, f"xpath={last_category_xpath}", action="click", timeout=15000)
            # --- THEN: Verify HOMELANDER category is selected/highlighted ---
            Utility.log_test_step(f"Verifying '{last_category_name}' category is selected/highlighted.")
            def assert_last_selected():
                selected_class = locator_last.get_attribute("class")
                if not selected_class or "active" not in selected_class:
                    raise AssertionError(f"'{last_category_name}' category is not highlighted as selected.")
            Utility.retry_assertion(assert_last_selected, retries=3, delay=1000)
            # --- Optionally: Simulate only one category present (hide others via dev tools) ---
            # This step is optional and would require DOM manipulation, which is not covered by POM.
            # If implemented, add logic here to hide other categories and verify single category behavior.
            test_passed = True
            Utility.log_test_result("PASS", "First and last category selection and highlighting verified successfully.")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Test failed due to unexpected error: {e}")
            raise
        finally:
            if not test_passed:
                Utility.log_error("Test did not complete successfully. See logs above for details.")
            browser.close()
            Utility.log_test_step("Browser closed. Test execution complete.")
#---#
