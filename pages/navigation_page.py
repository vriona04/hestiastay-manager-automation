import time


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
            ):
                print("Dashboard detected")
                return

            try:
                self.driver.back()
                time.sleep(2)

            except Exception:
                pass

        print("Could not confirm dashboard")

    def open_vacancies(self):

        self.go_home()

        try:
            self.driver.find_element(
                "xpath",
                "//*[contains(@content-desc,'Vacancies')]"
            ).click()

            time.sleep(3)

            print("VACANCIES OPENED")

        except Exception:
            print("Vacancies button not found")

    def open_rooms(self):

        self.go_home()

        try:
            self.driver.find_element(
                "xpath",
                "//*[contains(@content-desc,'Rooms')]"
            ).click()

            time.sleep(3)

            print("ROOMS OPENED")

        except Exception:
            print("Rooms button not found")

    def open_booked(self):

        self.go_home()

        try:
            self.driver.find_element(
                "xpath",
                "//*[contains(@content-desc,'Booked')]"
            ).click()

            time.sleep(3)

            print("BOOKED OPENED")

        except Exception:
            print("Booked button not found")

    def open_notifications(self):

        self.go_home()

        try:
            self.driver.find_element(
                "xpath",
                "//*[contains(@content-desc,'Notifications')]"
            ).click()

            time.sleep(3)

            print("NOTIFICATIONS OPENED")

        except Exception:
            print("Notifications button not found")

    def open_menu(self):

        self.go_home()

        try:
            self.driver.find_element(
                "xpath",
                "//*[contains(@content-desc,'Menu')]"
            ).click()

            time.sleep(3)

            print("MENU OPENED")

        except Exception:
            print("Menu button not found")

    def refresh_dashboard(self):

        self.go_home()

        try:
            self.driver.find_element(
                "xpath",
                "//*[contains(@content-desc,'Refresh')]"
            ).click()

            time.sleep(3)

            print("DASHBOARD REFRESHED")

        except Exception:
            print("Refresh button not found")