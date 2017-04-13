from selenium import webdriver
from selenium.webdriver.support.ui import Select
import cognitive_face as CF
import time

driver = webdriver.Chrome('./chromedriver')

KEY = '70d05f71a4ca436d83949d3458497c6e'
CF.Key.set(KEY)

driver.get("https://www.fbi.gov/wanted/fugitives")

count = 0
while count < 5:
	time.sleep(5)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	count += 1

for item in driver.find_elements_by_class_name('portal-type-person'):
	name = item.find_element_by_class_name('name').find_element_by_tag_name('a').text
	print(name)

	img = item.find_element_by_tag_name('a').find_element_by_class_name('focuspoint').find_element_by_tag_name('img').get_attribute("src")
	print(img)

	bio = item.find_element_by_tag_name('h3').find_element_by_tag_name('a').text
	print(bio)

	personID = CF.person.create(2, name, bio) #create a new person with name and bio
	unwrappedPersonID = personID['personId']
	print(unwrappedPersonID)
	try:
		CF.person.add_face(img, 2, unwrappedPersonID) #give the new person a face
	except Exception:
		pass

	print('new dude added')

	time.sleep(10)

driver.quit()
