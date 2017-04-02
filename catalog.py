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
