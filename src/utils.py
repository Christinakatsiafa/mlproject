import os
import sys
from src.exception import CustomException
from src.logger import logging

import numpy as np
import pandas as pd
import pickle 
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        logging.info("Create the report")
        for i in range(len(list(models))):
            model = list(models.values())[i]
            
            model.fit(X_train,y_train)
            
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            
            report[list(models.keys())[i]] = test_model_score
        
        logging.info("Report has be created successfully")
        return report
    
    except Exception as e:
        CustomException(e,sys)
    
