Model Training :
"Model training is the process of iteratively adjusting a model's parameters to minimize the difference between its predictions and the actual values in the training data."

=============================================================================================================

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(final_feature_set, labels, test_size = 0.25, random_state = 42)

// from xgboost import XGBClassifier
// import xgboost as xgb
// from xgboost import DMatrix

model = XGBClassifier(learning_rate =0.1, n_estimators=100 , random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test,y_pred ))
print(accuracy_score(y_test, y_pred))
