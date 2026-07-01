from pages.base_page import BasePage
from utils.navigation_helper import open_owner_menu
from utils.waits import medium_wait


class DashboardPage(BasePage):

    def is_loaded(self):
        page = self.current_page()

        return (
            "Hestia PG" in page
            or "Good Morning" in page
            or "Today's Overview" in page
            or "Announcements" in page
            or "Home" in page
        )

    def open_menu(self):
        return open_owner_menu(self.driver)

    def refresh(self):
        if self.page_contains("Refresh"):
            self.click_by_accessibility_id("Refresh")
            medium_wait()
            return True

        return False