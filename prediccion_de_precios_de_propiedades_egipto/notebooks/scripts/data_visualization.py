import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno
import seaborn as sns


@pd.api.extensions.register_dataframe_accessor("missing")
class MissingMethods:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj


    def missing_variable_plot(self):
        df = self._obj.missing.missing_variable_summary().sort_values("n_missing")

        plot_range = range(1, len(df.index) + 1)

        plt.hlines(y=plot_range, xmin=0, xmax=df.n_missing, color="black")

        plt.plot(df.n_missing, plot_range, "o", color="black")

        plt.yticks(plot_range, df.variable)

        plt.grid(axis="y")

        plt.xlabel("Number missing")
        plt.ylabel("Variable")


    def sort_variables_by_missingness(self, ascending = False):

        return (
            self._obj
            .pipe(
                lambda df: (
                    df[df.isna().sum().sort_values(ascending = ascending).index]
                )
            )
        )
    

    def visualizar_patrones_faltantes(df, order_by):
       data_missing = df.missing
       
       grafico = data_missing.sort_variables_by_missingness().sort_values(by=order_by).pipe(missingno.matrix)
       
       return grafico
    

    def matriz_correlacion(datos):
       
       correlacion = datos.corr()
       
       sns.heatmap(correlacion, cmap='Reds', annot=True, fmt='.2f')
       
       plt.show()

    
    def visualizar_outliers(datos):
    
       summary = datos.describe()
       Q1 = summary.loc['25%']
       Q3 = summary.loc['75%']
       IQR = Q3 - Q1

    
       lower_bound = Q1 - 1.5 * IQR
       upper_bound = Q3 + 1.5 * IQR

    
       outliers_count = (datos < lower_bound) | (datos > upper_bound)
       outliers_count = outliers_count.sum()

    
       plt.figure(figsize=(10, 6))
       sns.barplot(x=outliers_count.index, y=outliers_count.values)
       plt.xticks(rotation=90)
       plt.title("Número de Datos Atípicos por Variable")
       plt.xlabel("Variables")
       plt.ylabel("Número de Datos Atípicos")
       plt.show()