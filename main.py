from src.aqi.data_ingestion import loader
from src.aqi.data_preprocessing import processing
from src.aqi.model_building import model

def main():
    df = loader()
    print(df.shape)
    
    X_train,X_test,y_train,y_test = processing(df)
    
    score_train,score_test = model(X_train,X_test,y_train,y_test)
    
    print('Training accracy : ',score_train)
    print('Testing accuracy : ',score_test)
    
    
    
main()