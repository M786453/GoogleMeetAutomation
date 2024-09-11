import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

class GMAutomator:  

    def setup_driver(self):

        options = uc.ChromeOptions()

        profile = {
            "profile.default_content_setting_values.notifications":2,
            "profile.default_content_setting_values.media_stream": 1,
            "profile.content_settings.exceptions.media_stream_camera": {
                "https://meet.google.com,*": {"setting": 1}
            },
            "profile.content_settings.exceptions.media_stream_mic": {
                "https://meet.google.com,*": {"setting": 1}
            }
        }

        options.add_experimental_option("prefs", profile)

        self.driver = uc.Chrome(options=options)

    def join_meeting(self, meeting_link, username):

        try:

            self.setup_driver()
            
            self.driver.get(meeting_link)

            time.sleep(20)

            self.driver.find_element(By.XPATH, "//input[@aria-label='Your name']").send_keys(username)

            time.sleep(5)

            self.driver.find_element(By.XPATH, "//button[@data-promo-anchor-id='w5gBed']").click()

            time.sleep(10)

        except Exception as e:

            print("Error @ join_meeting:", e)

    def leave_meeting(self):

        try:
            
            self.driver.close()

        except Exception as e:

            print("Error @ leave_meeting:", e)