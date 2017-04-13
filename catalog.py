<<<<<<< HEAD
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
=======
import cognitive_face as CF
import time

KEY = '70d05f71a4ca436d83949d3458497c6e'
CF.Key.set(KEY)

#while True:
	img_url = 'C:\Users\mayur_000\Desktop\Random C++\CannyStill1\images\img.jpg'
	detectResult = CF.face.detect(img_url)

	faceIds = []

	if len(detectResult) != 0:
		for detected in detectResult:
			faceIds.append(detected['faceId'])
			#print detected

		identifyResult = CF.face.identify(faceIds,1)
		
		if len(identifyResult) != 0:
			for identified in identifyResult:
				if len(identified['candidates']) != 0:
					confirmed = CF.person.get(1, identified['candidates'][0]['personId'])
					print confirmed['userData']
					print confirmed['name']
					
	time.sleep(5)
>>>>>>> 09bd5112a17f3f24be0a2b7f2c308281dffd79bb
