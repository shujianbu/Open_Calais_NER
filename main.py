import sys
from calais import Calais


file = ["Bloomberg_Philippine_Peso_Set_for_Worst_Week_in_Two_Months", "Bloomberg_Korea_Won_Falls_Most_in_Two_Months_on_US_Budget_Concern", "Bloomberg_China_Next_Step_in_Yuan_Overhaul_Is_Convertibility_Zhou_Says", "NYTimes_A_Test_for_Obama_Light_Footprint", "NYTimes_Suit_Contests_Limits_on_Online_Activities_of_Sex_Offenders"]
for filename in file:
	fout = open(("results/" + filename + ".html"), "w") 
	fout.write('<html>')
	fout.write('\r\n')
	fout.write('<head><title>' + filename + '</title></head>')
	fout.write('\r\n')
	fout.write('<body>')

	with open(("articles/" + filename + ".txt"), "r") as myfile:
		sys.stdin = myfile
		content = ""
		for line in sys.stdin: 
			content += line 
	  
		API_KEY = "f7vhuv2kt4fxufuvv6eznwpe"
		calais = Calais(API_KEY, submitter="python-calais newsparser")
		result = calais.analyze(content)
		
		print "Summary of the Calais Analysis"
		result.print_summary()
		
		print "Entity of the Calais Analysis"
		result.print_entities()
		
		i = 0
		temp = []
		entityList = []
		html = []
		for entity in result.entities: 
			if result.entities[i]["_type"] in ["City","Company", "Country", "Movie", "Organization", "Person"]:
				temp.append(result.entities[i]["name"])  
				if 'resolutions' in result.entities[i]:
					temp.append(result.entities[i]['resolutions'][0]['id'])
				else:
					temp.append("null")
				entityList.append(temp)
				temp = []
			i += 1
		# print entityList  
 
		j = 0
		for j in range(len(entityList)):
			if entityList[j][1] != "null": 
				html.append('<a href= \"'+ entityList[j][1] + '\">' + entityList[j][0] + '</a>')
			else:
				html.append('<a href= "http://en.wikipedia.org/wiki/'+ entityList[j][0] + '\">' + entityList[j][0] + '</a>')
			j += 1
	
		# for link in html:
		# 	fout.write(link)	
		# 	fout.write('\r\n')
		# 	fout.write('</br>')	

		k = 0 
		for k in range(len(entityList)):
			content = content.replace(entityList[k][0],html[k]) 
			print entityList[k][0]
			print html[k] 
			k +=1
			print k
		print content
		fout.write(content)
		fout.write('\r\n')		
		fout.write('</body>')
		fout.write('\r\n')
		fout.write('</html>')

