import allure
from allure_commons.types import AttachmentType
from selene.support.shared import SharedBrowser


def add_screenshot(browser: SharedBrowser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser: SharedBrowser):
    log = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, extension='.log')


def add_html(browser: SharedBrowser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, extension='.html')
