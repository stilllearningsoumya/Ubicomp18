import glob
from operator import itemgetter
import numpy as np
from collections import Counter
#from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.metrics import f1_score


###################Creating the dataset from the files#################################
filenames=glob.glob("/home/snigdhad/BaselineSLWP/WifiProcessData/total.txt")
temp_dataset=[]
classes=[]
chosenFeatures = [1,2,3,4,5,6,7,8,9,10]
count_0=0
count_1=0
for files in filenames:
	file_handle=open(files,"r")
	print(files)
	for lines in file_handle:
		#print(lines)
		feature_vector=itemgetter(*chosenFeatures)(lines.strip("\r\n").split(","))
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
instances,features=dataset.shape
#print(class_data)
print("No. of instances: "+str(instances)+", No. of features: "+str(features))
print("Class count 0: "+str(count_0)+" 1:"+ str(count_1))
#print(np.isnan(dataset).any())
#sm = SMOTE(random_state=42)
#dataset_new, class_data_new = sm.fit_sample(dataset, class_data)
#print('Resampled dataset shape {}'.format(Counter(class_data_new)))
###################Applying stratified sampling########################################
X_train, X_test, y_train, y_test = train_test_split(dataset, class_data, test_size=.50,
		                                                    random_state=0)
#clf_1 = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(X_train, y_train)
clf_2 = RandomForestClassifier(max_depth=2, random_state=0).fit(X_train, y_train)
'''acc_1=clf_1.score(X_test, y_test)
acc_2=clf_2.score(X_test, y_test)
print("Accuracy with Gradient Boost: "+str(acc_1)+" Accuracy with Random Forest: "+str(acc_2))#'''

#roc_1=clf_1.predict(X_test)
roc_2=clf_2.predict(X_test)
#print(f1_score(y_test, roc_1))
print(f1_score(y_test, roc_2)) 
'''print(roc_2)
fpr_1, tpr_1, thresholds_1 = metrics.roc_curve(y_test, roc_1)
print(metrics.auc(fpr_1, tpr_1))
fpr_2, tpr_2, thresholds_2 = metrics.roc_curve(y_test, roc_2)
print(metrics.auc(fpr_2, tpr_2))'''
