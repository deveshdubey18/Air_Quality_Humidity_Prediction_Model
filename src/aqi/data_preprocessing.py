from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def processing(df):
    
    # drop duplicates
    df.drop_duplicates(inplace=True)
     
    
    # drop unwanted columns
    df.drop(columns=['Date','Time'],inplace=True)

    X = df.drop(columns='AH')
    y= df['AH']
    
    categorical = X.select_dtypes(include='object').columns
    numerical = X.select_dtypes(exclude='object').columns
    
    numerical_pipeline = Pipeline(steps=[
        ('imputer',SimpleImputer(strategy='mean')),
        ('scaler',MinMaxScaler())
    ])
    
    categorical_pipeline = Pipeline(steps=[
        ('imputer',SimpleImputer(strategy='most_frequent')),    
        ('onehot',OneHotEncoder(handle_unknown='ignore',drop='first'))
    ])
    
    transformer = ColumnTransformer(
        transformers=[
            ('num', numerical_pipeline, numerical),
            ('cat', categorical_pipeline, categorical)
        ]
    )
    
    # Splitting Data into Train and Test
    
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)
    
    X_train = transformer.fit_transform(X_train)
    X_test = transformer.transform(X_test)
    

    return X_train,X_test,y_train,y_test