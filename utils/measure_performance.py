from sklearn.metrics import mean_squared_error, mean_absolute_error
import pandas as pd
from pandas import DataFrame
import os

data = list(filter(lambda x: x.endswith('.csv'), os.listdir('./groups')))
DATA_DICT = {i[:-4]: pd.read_csv(f'./groups/{i}') for i in data}
TRUE_TARGETS = pd.read_csv('./test/target.csv')


class RankGroups:

    def __init__(self,
                 true_target: DataFrame,
                 results: dict,
                 target_col: str = 'target',
                 pred_col: str = 'prediccion'
                 ):
        self.true_target: DataFrame = true_target
        self.results: dict = results
        self.target_col = target_col
        self.pred_col = pred_col

    def calculate_metrics(self) -> dict:
        rmse = {}
        mae = {}
        for group in self.results.keys():
            merged = pd.merge(self.true_target, self.results.get(group), how='inner', on='identificador')
            rmse[group] = mean_squared_error(
                y_true=merged[self.target_col],
                y_pred=merged[self.pred_col]
            )
            mae[group] = mean_absolute_error(
                y_true=merged[self.target_col],
                y_pred=merged[self.pred_col]
            )
        return rmse, mae

    def rank_groups(self) -> DataFrame:
        rmse, mae = self.calculate_metrics()
        df_groups: DataFrame = pd.concat(
            [
            pd.DataFrame.from_dict(rmse, orient="index", columns=["RMSE"]),
            pd.DataFrame.from_dict(mae, orient="index", columns=["MAE"])
            ],
            axis=1
        ).sort_values(by='RMSE', ascending=True)
        df_groups['RANKING'] = list(range(1, df_groups.shape[0]+1))
        return df_groups


df = RankGroups(true_target=TRUE_TARGETS, results=DATA_DICT).rank_groups()
