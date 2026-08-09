
from sklearn.ensemble import RandomForestRegressor

import os
import pickle

def model(X_train,X_test,y_train,y_test):
    
    model = RandomForestRegressor(n_estimators=300)
    model.fit(X_train,y_train)
    
    y_pred = model.predict(X_test)
    score_test = model.score(X_test,y_test)
    score_train = model.score(X_train,y_train)
    
    
    os.makedirs('models',exist_ok=True)
        
    with open('models/model.pkl','wb') as f:
        pickle.dump(model,f)
    


    return score_train,score_test