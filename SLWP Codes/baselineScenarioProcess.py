import glob


path = 'WifiProcessData/'
writeScenarioData = ['']
for i in range(7):
	writeScenarioData.append('')
filenames_for_evaluation=glob.glob(path+"FeatureDataPair_*.txt")
for files in filenames_for_evaluation: 
	print files
	infile=open(files,"r")
	day = (files.split('_')[3]).split('.')[0]
	print day
	for lines in infile:
		time = int(lines.split(',')[0])
		if (day == '02022018' and ((time >= 850 and time <= 864) or (time >= 865 and time <= 879) or (time >= 880 and time <= 894) or (time >= 895 and time <= 909) or (time >= 910 and time <= 924))):
			writeScenarioData[0] += lines #S1
		elif (day == '01312018' and (time >= 744 and time <= 758)):
			writeScenarioData[1] += lines #S2
		elif (day == '02022018' and (time >= 771 and time <= 785)): #or (day == '09062017' and (time >= 1095 and time <= 1154))
			writeScenarioData[2] += lines #S3
		elif ((day == '01302018' and (time >= 687 and time <= 701)) or (day == '02012018' and (time >= 92 and time <= 106))):
			writeScenarioData[3] += lines #S4
		elif ((day == '01302018' and (time >= 1420 and time <= 1434)) or (day == '02022018' and (time >= 1338 and time <= 1352))):
			writeScenarioData[4] += lines #S5
		elif ((day == '01312018' and (time >= 43 and time <= 57)) or (day == '02022018' and (time >= 1380 and time <= 1394))):
			writeScenarioData[5] += lines #S6
		elif (day == '01312018' and (time >= 92 and time <= 106)):
			writeScenarioData[6] += lines  #S7

for i in range(7):
	with open (path + 'FeatureScenario_'+ str(i+1) + '.txt','w') as outfile:
		outfile.write(writeScenarioData[i])
	outfile.close()
