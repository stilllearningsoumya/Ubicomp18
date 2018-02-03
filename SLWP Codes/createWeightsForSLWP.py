import glob
import glob
from operator import itemgetter
import numpy as np
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.metrics import f1_score
#from memory_profiler import profile

#@profile
def createWeights():
###################Creating the dataset from the files#################################
	filenames=glob.glob("wifiSLWP/FeatureDataPair_*.txt")
	temp_dataset=[]
	classes=[]
	chosenFeatures = [1,2,3,4,5,6,7,8,9,10]
	count_0=0
	count_1=0
	releaseDate="01302018"
	for files in filenames:
		if(files.find(releaseDate,0,len(files))==-1):
			file_handle=open(files,"r")
			print(files)
			for lines in file_handle:
				#print(lines)
				lines=lines.strip("\r\n")
				if(lines.find("nan",0,len(lines))==-1):
					feature_vector=itemgetter(*chosenFeatures)(lines.split(","))
					#feature_vector=lines.strip("\r\n").split(",")[7:8]
					class_label=int(lines.strip("\r\n").split(",")[11])
					if(class_label==0):
						count_0+=1
					else:
						count_1+=1
					#print class_label
					data=[]
					for val in feature_vector:
					    #print(val)
					    data.append(float(val))
					temp_dataset.append(data)
					classes.append(class_label)
			file_handle.close()
	dataset=np.asanyarray(temp_dataset) 
	class_data=np.asarray(classes)
	#print(dataset)
	#print(dataset.shape)
	#print(class_data)
	#print("No. of instances: "+str(instances)+", No. of features: "+str(features))
	print("Class count 0: "+str(count_0)+" 1:"+ str(count_1))
#########################################################################################
################################Create Test Set##########################################
#########################################################################################
	filenames=glob.glob("wifiSLWP/FeatureDataPair_*"+releaseDate+"*.txt")
	for files in filenames:
		print(files)
		file_handle_test=open(files,"r")
		temp_dataset=[]
		classes=[]
		for lines in file_handle_test:
			lines=lines.strip("\r\n")
			if(lines.find("nan",0,len(lines))==-1):
				feature_vector=itemgetter(*chosenFeatures)(lines.strip("\r\n").split(","))
				class_label=int(lines.strip("\r\n").split(",")[11])
				data=[]
				for val in feature_vector:
				    #print(val)
				    data.append(float(val))
				temp_dataset.append(data)
				classes.append(class_label)
		file_handle_test.close()
		testdata=np.asanyarray(temp_dataset) 
		testClass=np.asarray(classes)
#########################################################################################
		clf_2 = RandomForestClassifier(max_depth=2, random_state=0).fit(dataset, class_data)
		weights=clf_2.predict_proba(testdata)
		#print weights
		lineNumber=0
		file_handle_test=open(files,"r")
		outFile="wifiSLWP/"+"Predicted_"+files.split("/")[1]
		file_handle_out=open(outFile,"w+")
		for lines in file_handle_test:
			if(lineNumber<len(weights)):
				#print lines.strip("\r\n").split(",")[0]+","+str(weights[lineNumber][1])
				file_handle_out.write(lines.strip("\r\n").split(",")[0]+","+str(weights[lineNumber][1])+"\n")
			lineNumber+=1
		file_handle_out.flush()
		file_handle_out.close()
		file_handle_test.close()
if __name__ == '__main__':
    createWeights()
