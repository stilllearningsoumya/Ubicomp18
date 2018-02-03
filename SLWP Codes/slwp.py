import datetime
import os
from collections import defaultdict
import math
import scipy.stats

def writeDataFile(path,day,user1,user2,featureDicData):
	writeData = ''
	for time in range(1440):
		if featureDicData[time][0] == -99999:
			continue
		else:
			data = ''
			for i in range(10):
				if data == '':
					data = str(time) + ',' + str(featureDicData[time][i])
				else:
					data += ',' + str(featureDicData[time][i])

		if day == '01-30-2018':
			if (time >= 687 and time <= 701):
				group1 = ['abhijit','ayan','bidisha','rohit','satadal','snigdha','soumyajit']
				if (user1 in group1 and user2 in group1):
					writeData += data + ',1\n'
				else:
					writeData += data + ',0\n'
			elif (time >= 1420 and time <= 1434):
				group1 = ['ayan','satadal','snigdha']
				group2 = ['abhijit','rohit','soumyajit']
				if ((user1 in group1 and user2 in group1) or (user1 in group2 and user2 in group2)):
					writeData += data + ',1\n'
				else:
					writeData += data + ',0\n'
		elif day == '01-31-2018':
			if (time >= 43 and time <= 57):
				group1 = ['abhijit','ayan','rohit','satadal','snigdha']
				group2 = ['soumyajit']
				if ((user1 in group1 and user2 in group1) or (user1 in group2 and user2 in group2)):
					writeData += data + ',1\n'
				else:
					writeData += data + ',0\n'
			elif (time >= 92 and time <= 106):
				group1 = ['ayan','rohit','satadal','snigdha','soumyajit']
				group2 = ['samsung','bidisha']
				if ((user1 in group1 and user2 in group1) or (user1 in group2 and user2 in group2)):
					writeData += data + ',1\n'
				else:
					writeData += data + ',0\n'
			elif (time >= 744 and time <= 758):
				group1 = ['abhijit','satadal']
				group2 = ['ayan','samsung','snigdha','soumyajit']
				group3 = ['rohit','bidisha']
				if ((user1 in group1 and user2 in group1) or (user1 in group2 and user2 in group2)or (user1 in group3 and user2 in group3)):
					writeData += data + ',1\n'
				else:
					writeData += data + ',0\n'
		elif day == '02-01-2018':
			if ((time >= 1097 and time <= 1111) or (time >= 1112 and time <= 1126) or (time >= 1127 and time <= 1141) or (time >= 1142 and time <= 1156)):
				group1 = ['abhijit','ayan','rohit','satadal','snigdha','soumyajit','samsung']
				if (user1 in group1 and user2 in group1):
					writeData += data + ',1\n'
				else:
					writeData += data + ',0\n'
		elif day == '02-02-2018':
			if (time >= 771 and time <= 785):
				group1 = ['ayan','abhijit','satadal','snigdha']
				group2 = ['samsung','bidisha','rohit']
				if ((user1 in group1 and user2 in group1) or (user1 in group2 and user2 in group2)):
					writeData += data + ',1\n'
				else:
					writeData += data + ',0\n'
			elif ((time >= 850 and time <= 864) or (time >= 865 and time <= 879) or (time >= 880 and time <= 894) or (time >= 895 and time <= 909) or (time >= 910 and time <= 924)):
				group1 = ['ayan','bidisha','soumyajit','snigdha','samsung']
				group2 = ['satadal','rohit']
				if ((user1 in group1 and user2 in group1) or (user1 in group2 and user2 in group2)):
					writeData += data + ',1\n'
				else:
					writeData += data + ',0\n'
			elif (time >= 1338 and time <= 1352):
				group1 = ['ayan','abhijit','rohit','snigdha']
				group2 = ['samsung','bidisha','satadal']
				if ((user1 in group1 and user2 in group1) or (user1 in group2 and user2 in group2)):
					writeData += data + ',1\n'
				else:
					writeData += data + ',0\n'
			elif (time >= 1380 and time <= 1394):
				group1 = ['ayan','abhijit','rohit','snigdha','samsung','bidisha','satadal','soumyajit']
				if (user1 in group1 and user2 in group1):
					writeData += data + ',1\n'
				else:
					writeData += data + ',0\n'
	# print writeData
	dayStr = datetime.datetime.strptime(day,'%m-%d-%Y').strftime('%m%d%Y')
	with open ('wifiSLWP/FeatureDataPair_'+ user1 + '_' + user2 + '_' + dayStr + '.txt','a') as outfile:
		outfile.write(writeData)
	outfile.close()

def nonOverlapBssidGenerate(bssid1,bssid2):
	bssidNonOverlap = []
	for i in range(len(bssid2)):
		if bssid2[i] not in bssid1:
			bssidNonOverlap.append(bssid2[i])
	#print bssidIntersect
	return bssidNonOverlap

def unionBssidGenerate(bssid1,bssid2):
	bssidUnion = list(bssid1)
	for i in range(len(bssid2)):
		if bssid2[i] not in bssidUnion:
			bssidUnion.append(bssid2[i])
	return bssidUnion

def intersectBssidGenerate(bssid1,bssid2):
	bssidIntersect = []
	for i in range(len(bssid2)):
		if bssid2[i] in bssid1:
			bssidIntersect.append(bssid2[i])
	#print bssidIntersect
	return bssidIntersect


def featureGeneration(dicData):
	featureDicData = defaultdict(dict)
	for time in range(1440):
		featureDicData[time][0] = -99999 #overlap
		featureDicData[time][1] = -99999 #union
		featureDicData[time][2] = -99999 #jaccard
		featureDicData[time][3] = -99999 #nonOverlap
		featureDicData[time][4] = -99999 #spearman
		featureDicData[time][5] = -99999 #pearson
		featureDicData[time][6] = -99999 #manhattan
		featureDicData[time][7] = -99999 #euclidean
		featureDicData[time][8] = -99999 #topAP
		featureDicData[time][9] = -99999 #topAP+6dB
		


	for time in range(1440):
		wifiInfoUser1 = dicData[time][0][2]
		wifiInfoUser2 = dicData[time][1][2]
		
		if wifiInfoUser1 == '' or wifiInfoUser2 == '':
			overlapFeature = -99999
			unionFeature = -99999
			jcFeature = -99999
			nonoverlapFeature = -99999
			spearmanFeature = -99999
			pearsonFeature = -99999
			manhattanFeature = -99999
			euclideanFeature = -99999
			topAPFeature = -99999
			topAPplussixFeature = -99999
		else :
			#print wifiInfoUser1
			#print wifiInfoUser2
			
			wifiSplitInfoUser1 = wifiInfoUser1.split(';')
			bssidInfoUser1 = []
			signalStrengthUser1 = []
			for i in range(len(wifiSplitInfoUser1)):
				bssidPlusSSInfo = wifiSplitInfoUser1[i].split(',')
				bssidInfoUser1.append(bssidPlusSSInfo[0])
				signalStrengthUser1.append(bssidPlusSSInfo[1])

			wifiSplitInfoUser2 = wifiInfoUser2.split(';')
			bssidInfoUser2 = []
			signalStrengthUser2 = []
			for i in range(len(wifiSplitInfoUser2)):
				bssidPlusSSInfo = wifiSplitInfoUser2[i].split(',')
				bssidInfoUser2.append(bssidPlusSSInfo[0])
				signalStrengthUser2.append(bssidPlusSSInfo[1])
			
			if len(wifiSplitInfoUser1) > len(wifiSplitInfoUser2):
				unionBssidList = unionBssidGenerate(bssidInfoUser1,bssidInfoUser2)
				intersectBssidList = intersectBssidGenerate(bssidInfoUser1,bssidInfoUser2)
			else :
				unionBssidList = unionBssidGenerate(bssidInfoUser2,bssidInfoUser1)
				intersectBssidList = intersectBssidGenerate(bssidInfoUser2,bssidInfoUser1)

			nonOverlapBssidList = nonOverlapBssidGenerate(intersectBssidList,unionBssidList)

			overlapFeature = len(intersectBssidList)
			unionFeature = len(unionBssidList)
			nonoverlapFeature = len(nonOverlapBssidList)

			#print signalStrengthUser1
			#print signalStrengthUser2

			top_ap1_SS = -100
			top_ap2_SS = -100

			for i in range(len(signalStrengthUser1)):
				if float(signalStrengthUser1[i]) > top_ap1_SS:
					top_ap1_SS = float(signalStrengthUser1[i])
					top_ap1 = bssidInfoUser1[i] 
			for i in range(len(signalStrengthUser2)):
				if float(signalStrengthUser2[i]) > top_ap2_SS:
					top_ap2_SS = float(signalStrengthUser2[i])
					top_ap2 = bssidInfoUser2[i] 

			#print top_ap1_SS
			#print top_ap2_SS

			if top_ap1 == top_ap2:
				topAPFeature = 1
			else:
				topAPFeature = 0
			
			if not intersectBssidList: 
				jcFeature = 0.0
				spearmanFeature = 0.0
				pearsonFeature = 0.0
				manhattanFeature = 99999.0
				euclideanFeature = 99999.0
				topAPplussixFeature = 0
			else :
				jcFeature = len(intersectBssidList)*1.0/len(unionBssidList)

				intersectSignal1List = []
				intersectSignal2List = []
				for i in range(len(intersectBssidList)):
					for j in range(len(bssidInfoUser1)):
						if intersectBssidList[i] == bssidInfoUser1[j]:
							intersectSignal1List.append(float(signalStrengthUser1[j]))
					for k in range(len(bssidInfoUser2)):
						if intersectBssidList[i] == bssidInfoUser2[k]:
							intersectSignal2List.append(float(signalStrengthUser2[k]))

				if len(intersectBssidList) < 3:
					spearmanFeature = 99999.0
					pearsonFeature = 99999.0
				else: 

					try:
						spearmanFeature = scipy.stats.spearmanr(intersectSignal1List, intersectSignal2List)[0]

						pearsonFeature = 0.0
						meanWifiUser1 = 0.0
						for i in range(len(intersectSignal1List)):
							meanWifiUser1 += float(intersectSignal1List[i])
						meanWifiUser1 /= len(intersectSignal1List)

						meanWifiUser2 = 0.0
						for i in range(len(intersectSignal2List)):
							meanWifiUser2 += float(intersectSignal2List[i])
						meanWifiUser2 /= len(intersectSignal2List)

						varWifiUser1 = 0.0
						for i in range(len(intersectSignal1List)):
							varWifiUser1 += pow((intersectSignal1List[i] - meanWifiUser1),2)
						varWifiUser1 = math.sqrt(varWifiUser1)

						varWifiUser2 = 0.0
						for i in range(len(intersectSignal2List)):
							varWifiUser2 += pow((intersectSignal2List[i] - meanWifiUser2),2)
						varWifiUser2 = math.sqrt(varWifiUser2)
					
						for i in range(len(intersectSignal1List)):
							pearsonFeature += ((intersectSignal1List[i] - meanWifiUser1)*(intersectSignal2List[i] - meanWifiUser2))
						if varWifiUser1*varWifiUser2 == 0.0:
							pearsonFeature = 0.0
						else:
							pearsonFeature /= (varWifiUser1*varWifiUser2)
					except Exception as e:
						print e
						pass

				manhattanFeature = 0.0
				for i in range(len(intersectBssidList)):
					manhattanFeature += abs(intersectSignal1List[i] - intersectSignal2List[i])
				manhattanFeature /= len(intersectBssidList)

				euclideanFeature = 0.0
				for i in range(len(intersectBssidList)):
					euclideanFeature += pow((intersectSignal1List[i] - intersectSignal2List[i]),2)
				euclideanFeature = math.sqrt(euclideanFeature)
				euclideanFeature /= len(intersectBssidList)

				topAPplussixFeature = 0
				top_ap_SS = max(top_ap1_SS, top_ap2_SS)
				#print top_ap_SS
				#print intersectSignal1List
				for i in range(len(intersectSignal1List)):
					if abs(intersectSignal1List[i] - top_ap_SS) <= 6.0:
						topAPplussixFeature = 1
						break
				if topAPplussixFeature == 0:
					for i in range(len(intersectSignal2List)):
						if abs(intersectSignal2List[i] -top_ap_SS) <= 6.0:
							topAPplussixFeature = 1
							break

		featureDicData[time].update({0:overlapFeature}) #overlap
		featureDicData[time].update({1:unionFeature}) #union
		featureDicData[time].update({2:jcFeature}) #jaccard
		featureDicData[time].update({3:nonoverlapFeature}) #nonOverlap
		featureDicData[time].update({4:spearmanFeature}) #spearman
		featureDicData[time].update({5:pearsonFeature}) #pearson
		featureDicData[time].update({6:manhattanFeature}) #manhattan
		featureDicData[time].update({7:euclideanFeature}) #euclidean
		featureDicData[time].update({8:topAPFeature}) #topAP 
		featureDicData[time].update({9:topAPplussixFeature}) #topAPplussix
		
	#print featureDicData
	return featureDicData


def returnDateAsString(string):
	changedDate=None
	if(len(string.split("-"))>1):
		changedDate=datetime.datetime.strptime(string, '%d-%b-%Y %H:%M:%S').strftime('%m-%d-%Y %H:%M')
	else:
		if((string.find(",", 0, len(string)))!=-1):
			changedDate=datetime.datetime.strptime(string, '%b %d, %Y %H:%M:%S').strftime('%m-%d-%Y %H:%M')
		else:
			timeSchedule=string[len(string)-4:len(string)]
			# print timeSchedule
			if(timeSchedule=='a.m.'):
				string=string[:len(string)-5]+' AM'
				changedDate=datetime.datetime.strptime(string, '%d %b %Y %I:%M:%S %p').strftime('%m-%d-%Y %H:%M')
			elif(timeSchedule=='p.m.'):
				string=string[:len(string)-5]+' PM'
				changedDate=datetime.datetime.strptime(string, '%d %b %Y %I:%M:%S %p').strftime('%m-%d-%Y %H:%M')
			else:
				# print timeSchedule
				changedDate=datetime.datetime.strptime(string, '%d %b %Y %H:%M:%S').strftime('%m-%d-%Y %H:%M')
	return changedDate

def dataprocess(path,day,user1,user2):
	dicData = defaultdict(lambda: defaultdict(dict))
	for time in range(1440):
		for user in range(2):
			dicData[time][user][0] = '' #lumiData
			dicData[time][user][1] = '' #magFluxMagnitude
			dicData[time][user][2] = '' #wifi
			dicData[time][user][3] = [] #audio
	users = {0:user1,1:user2}
	for i in range(2):
		with open (path + '/' + users[i] + '/V2_' + day + '.txt','r') as infile:
			prevTime = -1
			for line in infile:
				#print line
				line = line.strip('\r\n')
				words = line.split('|')
				audioData = words[0] 
				audioFilterData = []#getAudioLevel(audioData)
				lumiData = words[1]
				#print lumiData
				magData = words[2].strip('[]')
				#print magData
				accelerometerData = words[3].strip('[]')
				#print accelerometerData
				wifiData = words[4].split('>')
				#print wifiData
				dateData = words[5]
				#print dateData

				dateInfo = returnDateAsString(dateData)
				dateTimeInfo = dateInfo.split(' ')
				dayCompare = dateTimeInfo[0]

				if dayCompare == day:
					timeInfo = dateTimeInfo[1].split(':')
					timeHour = timeInfo[0]
					timeMinute = timeInfo[1]
					time = (int(timeHour) * 60) + int(timeMinute)

					if magData != '':
						magInfo = magData.split(',')
						magFluxMagnitude = str(pow(float(magInfo[0]),2) + pow(float(magInfo[1]),2) + pow(float(magInfo[2]),2))
					else :
						magFluxMagnitude = ''

					accelerometerInfo = accelerometerData.split(',')

					wifiFilteredInfo = ''


					if time - prevTime > 0:
						prevTime = time
						#print dateInfo
						if wifiData[2] != '':
							wifiInfo = wifiData[2].split(';')
							for val in wifiInfo:
								val = val.split(',')
								bssid = val[0]
								signalStrength = val[2]
								if wifiFilteredInfo == '':
									wifiFilteredInfo = bssid + ',' + signalStrength
								else :
									wifiFilteredInfo += ';' + bssid + ',' + signalStrength
						else :
							wifiFilteredInfo = ''
						#userInfo = lumiData + '#' + magFluxMagnitude + '#' + wifiFilteredInfo
						#print str(time) + '|' + userInfo
						#print audioFilterData
						dicData[time][i].update({0:lumiData})
						dicData[time][i].update({1:magFluxMagnitude})
						dicData[time][i].update({2:wifiFilteredInfo})
						dicData[time][i].update({3:audioFilterData})
		infile.close()
	#print dicData
	return dicData


def list_users(path):
	users = []
	with open (path + '/users.txt','r') as infile:
		for line in infile:
			line = line.strip('\r\n')
			users.append(line)
	return users


def main():
	path = '/home/snigdhad/Data2018'
	day = '02-02-2018'
	userList = list_users(path)
	for i in range(len(userList)-1):
		for j in range(i+1,len(userList)):
			if not ((os.path.isfile(path + '/' + userList[i] + '/V2_' + day + '.txt')) and ((os.path.isfile(path + '/' + userList[j] + '/V2_' + day + '.txt')))):
				continue
			print '  started: ', day, userList[i], userList[j]
			dicData = dataprocess(path,day,userList[i], userList[j]) # 08-28-2017 onwards
			featureDicData = featureGeneration(dicData)
			writeDataFile(path,day,userList[i], userList[j],featureDicData)
			print 'completed: ', day, userList[i], userList[j]

	'''dicData = dataprocess(path,day,'Satadal','Bidisha')
	featureDicData = featureGeneration(dicData)
	writeDataFile(path,day,'Satadal','Bidisha',featureDicData)'''


if __name__=='__main__':
	main()
