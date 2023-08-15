import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno
import seaborn as sns
from  sklearn  import  preprocessing


@pd.api.extensions.register_dataframe_accessor("missing")
class MissingMethods:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj


    def missing_variable_summary(self) -> pd.DataFrame:
        return self._obj.isnull().pipe(
            lambda df_1: (
                df_1.sum()
                .reset_index(name="n_missing")
                .rename(columns={"index": "variable"})
                .assign(
                    n_cases=len(df_1),
                    pct_missing=lambda df_2: df_2.n_missing / df_2.n_cases * 100,
                )
            )
        )
    


def train_scaler(X_train, y_train):
    
    x_scaler = preprocessing.RobustScaler()
    x_train_escalado = x_scaler.fit_transform(X_train)
    
    
    y_train_array = np.array(y_train)
    
    
    y_scaler = preprocessing.RobustScaler()
    y_train_escalado = y_scaler.fit_transform(y_train_array.reshape(-1, 1))
    
    return x_train_escalado, y_train_escalado


def test_scaler(X_test, y_test):
    # Escalar las características (X_test) usando RobustScaler
    x_scaler = preprocessing.RobustScaler()
    x_test_escalado = x_scaler.fit_transform(X_test)
    
    # Convertir y_test a un array de numpy si aún no lo es
    y_test_array = np.array(y_test)
    
    # Escalar las etiquetas (y_test) usando RobustScaler
    y_scaler = preprocessing.RobustScaler()
    y_test_escalado = y_scaler.fit_transform(y_test_array.reshape(-1, 1))
    
    return x_test_escalado, y_test_escalado