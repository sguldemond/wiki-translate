from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options, executable_path='/usr/local/bin/geckodriver')


def page_title(url, driver):
    driver.get(url)
    first_heading_element = driver.find_element_by_css_selector('#firstHeading')
    return first_heading_element.text


url = "https://nl.wikipedia.org/wiki/Computer"
driver.get(url)
print(page_title(url, driver))


languages = []
language_elements = driver.find_elements_by_class_name('interlanguage-link-target')
for language_element in language_elements:
    language = {'name': language_element.text, 'url': language_element.get_attribute('href')}
    languages.append(language)
    i = len(languages)

    print(str(i) + ': ' + language['name'] + ' // ' + language['url'])


active = True

while active:
    user_input = input('Select language (id): ')

    if user_input == '/quit':
        active = False
        break

    selected_lang = languages[int(user_input) - 1]
    print(page_title(selected_lang['url'], driver) + ' (' + selected_lang['name'] + ')')

driver.quit()