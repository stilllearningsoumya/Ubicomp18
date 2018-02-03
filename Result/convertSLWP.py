import os 

def map (path,filename):
	filename=filename.replace('parsed_clustered_','').replace('.txt','')#.replace('sData.txt','')
	day = filename.split('_')[0]
	time = int(filename.split('_')[1])
	name_to_integer_mapping = {'abhijit':'0','ayan':'1','bidisha':'2','rohit':'3','satadal':'4','snigdha':'5','soumyajit':'6','samsung':'7'} 
	group1 = []
	group2 = []
	group3 = []
	groupTime = 15
	if day == '01302018':
		if (time >= 687 and time <= 701):
			expNo = 'exp1'+ str((time -687)/groupTime + 1)			
			group1 = ['abhijit','ayan','bidisha','rohit','satadal','snigdha','soumyajit']
		elif (time >= 1420 and time <= 1434):
			expNo = 'exp2'+ str((time -1420)/groupTime + 1)	
			group1 = ['ayan','satadal','snigdha']
			group2 = ['abhijit','rohit','soumyajit']
	elif day == '01312018':
		if (time >= 43 and time <= 57):
			expNo = 'exp3'+ str((time -43)/groupTime + 1)	
			group1 = ['abhijit','ayan','rohit','satadal','snigdha']
			group2 = ['soumyajit']
		elif (time >= 92 and time <= 106):
			expNo = 'exp4'+ str((time -92)/groupTime + 1)	
			group1 = ['ayan','rohit','satadal','snigdha','soumyajit']
			group2 = ['samsung','bidisha']
		elif (time >= 744 and time <= 758):
			expNo = 'exp5'+ str((time -744)/groupTime + 1)	
			group1 = ['abhijit','satadal']
			group2 = ['ayan','samsung','snigdha','soumyajit']
			group3 = ['rohit','bidisha']
	elif day == '02012018':
		if ((time >= 1097 and time <= 1111) or (time >= 1112 and time <= 1126) or (time >= 1127 and time <= 1141) or (time >= 1142 and time <= 1156)):
			expNo = 'exp6'+ str((time -1097)/groupTime + 1)	
			group1 = ['abhijit','ayan','rohit','satadal','snigdha','soumyajit','samsung']
	elif day == '02022018':
		if (time >= 771 and time <= 785):
			expNo = 'exp7'+ str((time -771)/groupTime + 1)	
			group1 = ['ayan','abhijit','satadal','snigdha']
			group2 = ['samsung','bidisha','rohit']
		elif ((time >= 850 and time <= 864) or (time >= 865 and time <= 879) or (time >= 880 and time <= 894) or (time >= 895 and time <= 909) or (time >= 910 and time <= 924)):
			expNo = 'exp8'+ str((time -850)/groupTime + 1)	
			group1 = ['ayan','bidisha','soumyajit','snigdha','samsung']
			group2 = ['satadal','rohit']
		elif (time >= 1338 and time <= 1352):
			expNo = 'exp9'+ str((time -1338)/groupTime + 1)	
			group1 = ['ayan','abhijit','rohit','snigdha']
			group2 = ['samsung','bidisha','satadal']
		elif (time >= 1380 and time <= 1394):
			expNo = 'exp10'+ str((time -1380)/groupTime + 1)	
			group1 = ['ayan','abhijit','rohit','snigdha','samsung','bidisha','satadal','soumyajit']
	print filename, expNo

	writeData = ''
	if group1:
		val = ''
		for key in group1:
			if val == '':
				val = name_to_integer_mapping[key] 
			else :
				val += ',' + name_to_integer_mapping[key]
		#val = ','.join(group1)
		if writeData == '':
			writeData = val
		else :
			writeData += '|' + val
	if group2:
		val = ''
		for key in group2:
			if val == '':
				val = name_to_integer_mapping[key] 
			else :
				val += ',' + name_to_integer_mapping[key]
		# val = ','.join(group2)
		if writeData == '':
			writeData = val
		else :
			writeData += '|' + val
	if group3:
		val = ''
		for key in group3:
			if val == '':
				val = name_to_integer_mapping[key] 
			else :
				val += ',' + name_to_integer_mapping[key]
		# val = ','.join(group3)
		if writeData == '':
			writeData = val
		else :
			writeData += '|' + val
	print writeData
	#with open ('groundtruth/groundtruth_' + expNo + '.txt','w') as outfile:
		#outfile.write(writeData)
	#outfile.close()
	expName = 'parsed_clustered_' + expNo + 'sData.txt'
	return expName

def list_files(path):
	# returns a list of names (with extension, without full path) of all files
	# in folder path
	files = []
	for name in os.listdir(path):
		if os.path.isfile(os.path.join(path, name)) and os.stat(os.path.join(path, name)).st_size > 0:
			if name.startswith('parsed_clustered_') and name.endswith('.txt'):
				files.append(name)
	return files

def main():
	path = 'slwp/'
	filenameList = list_files(path)
	# print filenameList
	for filename in filenameList:
		expName = map(path,filename)
		os.rename(path+filename,path+expName)

if __name__=='__main__':
	main()
