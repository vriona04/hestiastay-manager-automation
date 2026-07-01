from pages.base_page import BasePage
from utils.navigation_helper import open_owner_menu
from utils.waits import medium_wait


class BillsPage(BasePage):

    def open(self):
        open_owner_menu(self.driver)

        if not self.page_contains("Bills"):
            return False

        self.click_by_accessibility_id("Bills")
        medium_wait()
        return True

    def is_loaded(self):
        page = self.current_page()

        return (
            "Bills" in page
            or "Filter Bills" in page
            or "Current" in page
            or "No bills found" in page
            or "Add Bill" in page
        )