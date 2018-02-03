from sklearn.cluster import KMeans
import numpy as np
import glob
import scipy.stats as stats

def performClustering(X):
	kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
	#print kmeans.labels_
	return kmeans.labels_

def performWindowing(listVals):
	X=[]
	for elem in listVals:
		temp=[]
		temp.append(elem)
		X.append(temp)
	clusterLabels=performClustering(X)
	group0=[]
	group1=[]
	i=0
	for labels in clusterLabels:
		if(labels==0):
			group0.append(X[i][0])
		else:
			group1.append(X[i][0])
		i+=1
	#print group0
	#print group1
	finalVal=0.0
	p_value=stats.f_oneway(group0,group1)[1]
	#print "Level of significance: "+str(p_value)
	if(p_value>=0.05 or np.isnan(p_value)):
		finalVal=float(sum(listVals))/float(len(listVals))
	else:
		if(len(group0)>len(group1)):
			finalVal=float(sum(group0))/float(len(group0))
		else:
			finalVal=float(sum(group1))/float(len(group1))
	#print "Final return value: "+str(finalVal)
	return finalVal
		
window_size=15
filenames=glob.glob("wifiSLWP/Predicted_*")#GainData
for files in filenames:
	try:
		out_file="Splitted"
		for i in range(1,len(files.split("_"))):
			out_file+="_"
			out_file+=files.split("_")[i]
		print out_file
		in_file_handle=open(files,"r")
		out_file_handle=open("wifiSLWP/"+out_file,"w+")
		tempTime=0
		listVals=[]
		for lines in in_file_handle:
			data=lines.strip("\r\n").split(",")
			time=int(data[0])
			inverted_gain=float(data[1])#JC 2, gain 3, both 1
			if((time-tempTime)<window_size):
				listVals.append(inverted_gain)			
			else:
				if(len(listVals)!=0):
					finalVal=performWindowing(listVals)
					#finalVal_1=oldPerformWindowing(listVals)
					#print str(finalVal)+" "+str(finalVal_1)
					out_file_handle.write(str(tempTime)+","+str(finalVal)+"\n")
					tempTime=time
					listVals=[]
					countVal=0
				else:
					tempTime=time
		in_file_handle.close()
		if(len(listVals)!=0):
			finalVal=performWindowing(listVals)
			#finalVal_1=oldPerformWindowing(listVals)
			#print str(finalVal)+" "+str(finalVal_1)
			out_file_handle.write(str(tempTime)+","+str(finalVal)+"\n")
			tempTime=time
			listVals=[]
			countVal=0
		out_file_handle.flush()
		out_file_handle.close()
	except Exception as e:
		print e
		pass
