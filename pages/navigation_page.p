from utils.logger import log
from utils.waits import medium_wait


class NavigationPage:

    def __init__(self, driver):
        self.driver = driver

    def go_home(self):

        for _ in range(5):
            page = self.driver.page_source

            if (
                "Hestia PG" in page
                or "Good Morning" in page
                or "Today's Overview" in page
                or "Announcements" in page
                or "Home" in page
                or "Vacancies" in page
                or "Rooms" in page
            ):
                log("Dashboard detected")
                return True

            try:
                self.driver.back()
                medium_wait(2)
            except Exception:
                pass

        log("Could not confirm dashboard")
        return False

    def click_if_available(self, text, success_message, failure_message):

        if not self.go_home():
            log(failure_message)
            return False

        try:
            self.driver.find_element(
                "xpath",
                f"//*[contains(@content-desc,'{text}')]"
            ).click()

            medium_wait(3)
            log(success_message)
            return True

        except Exception:
            log(failure_message)
            return False

    def open_vacancies(self):
        return self.click_if_available(
            "Vacancies",
            "VACANCIES OPENED",
            "Vacancies button not found"
        )

    def open_rooms(self):
        return self.click_if_available(
            "Rooms",
            "ROOMS OPENED",
            "Rooms button not found"
        )

    def open_booked(self):
        return self.click_if_available(
            "Booked",
            "BOOKED OPENED",
            "Booked button not found"
        )

    def open_notifications(self):
        return self.click_if_available(
            "Notifications",
            "NOTIFICATIONS OPENED",
            "Notifications button not found"
        )

    def open_menu(self):
        return self.click_if_available(
            "Menu",
            "MENU OPENED",
            "Menu button not found"
        )

    def refresh_dashboard(self):
        return self.click_if_available(
            "Refresh",
            "DASHBOARD REFRESHED",
            "Refresh button not found"
        )