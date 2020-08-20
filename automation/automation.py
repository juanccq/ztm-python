from selenium import webdriver

chrome_browser = webdriver.Chrome( './chromedriver' )

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
button = chrome_browser.find_element_by_class_name( 'btn-default' )

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id( 'user-message' )

# another option 
user_message2 = chrome_browser.find_element_by_css_selector('#user-message')
print(user_message2)

user_message.clear()
user_message.send_keys( 'my name is juan' )

button.click()

output_message = chrome_browser.find_element_by_id('display')

assert 'my name is juan' in output_message.text

chrome_browser.quit()