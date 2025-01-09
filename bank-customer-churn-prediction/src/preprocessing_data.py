Data Pre-processing :

"Data preprocessing is defined as transforming raw data into a suitable format for training models.
This involves cleaning, transforming, and splitting the data to improve model accuracy and efficiency."

============================================================================================================

data = data.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

features =  data.drop(['Exited'], axis=1)

labels = data['Exited']

temp_data =  features.drop(['Geography', 'Gender'], axis=1)

Geography = pd.get_dummies(features .Geography).iloc[:,1:]

Gender = pd.get_dummies(features.Gender).iloc[:,1:]

final_feature_set = pd.concat([temp_data,Geography,Gender], axis=1)
