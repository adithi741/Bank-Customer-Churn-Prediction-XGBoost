Evaluating a model :
"Model evaluation is the process of assessing a trained model's performance on unseen data."

================================================================================================

import numpy as np
feat_importances = pd.Series(model.feature_importances_, index=final_feature_set.columns)
colors=['lightcoral','lightgreen','lightsteelblue','cornflowerblue','teal']
feat_importances.nlargest(5).plot(kind='bar',color=colors)

