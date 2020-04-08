from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import os


class COGBrowser:
    def __init__(self):
        self.cog_username = 'MikeB'
        self.cog_password = 'Pasteur123'
        # self.cog_username = os.environ.get('cogUsername')
        # self.cog_password = os.environ.get('cogPassword')
        self.options = Options()
        # self.options.headless = True
        self.browser = Chrome()


    def browse(self):
        self.browser.get('https://lookup.coghq.org/report/minister/login.php')


    def login(self):
        self.browser.find_element_by_name('usr').send_keys(self.cog_username)
        self.browser.find_element_by_name('psw').send_keys(self.cog_password)
        self.browser.find_element_by_name('submit').click()


    def report(self):
        # report link
        self.browser.get('https://lookup.coghq.org/report/minister/report.php')

        # [0] is spanish button is top-right corner
        # [1] starts report button
        # handle for possibility of more than 1 report button
        # browser.find_elements_by_tag_name('input')[1].click()
        self.browser.find_elements_by_xpath("//input[@type='button']")[1].click()

        # reporting to New Jersey
        self.browser.find_element_by_name('ans').click()
        self.browser.find_element_by_name('ans').is_selected() # True if selected

        # continue
        self.browser.find_elements_by_tag_name('input')[-1].click()


    def fill_in_form(self):
        # no to 'Has marital status changed since last report?'
        # [0] is yes
        self.browser.find_elements_by_name('marital_status_change')[1].click()

        # no to 'Do you have a supplemental vocation to your ministry?'
        # [0] is yes
        self.browser.find_elements_by_name('supplemental_vocation')[1].click()

        self.browser.find_element_by_name('revivals').send_keys(5)
        self.browser.find_element_by_name('past_visit').send_keys(3)
        self.browser.find_element_by_name('spec_serv').send_keys(1)
        self.browser.find_element_by_name('sermons').send_keys(4)
        self.browser.find_element_by_name('personal_evangelism_mtgs').send_keys(5)
        self.browser.find_element_by_name('lectures').send_keys(5)
        self.browser.find_element_by_name('worker_classes').send_keys(5)
        self.browser.find_element_by_name('counseling').send_keys(5)
        self.browser.find_element_by_name('choir_training_mtgs').send_keys(5)
        self.browser.find_element_by_name('tithes').click()
        self.browser.find_element_by_name('tithes_where').send_keys('East Orange Church of God')


    def submit(self):
        # submit edit
        self.browser.find_element_by_xpath('/html/body/center[3]/input')


    def quit_browser(self):
        self.browser.quit()


if __name__ == '__main__':
    cog = COGBrowser()
    cog.browse()
    cog.login()
    cog.report()
    cog.fill_in_form()
    # cog.quit_browser()