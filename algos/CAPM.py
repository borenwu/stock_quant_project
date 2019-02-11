import pandas as pd
import numpy as np


class CAPM:
    def __init__(self, stock_file, index_daily_path, stock_daily_path, trade_day):
        self.stock_file = stock_file
        self.index_daily_path = index_daily_path
        self.stock_daily_path = stock_daily_path
        self.trade_day = trade_day

    def go_beta(self):
        SH_data = self.index_daily_path + '000001.SH.csv'
        SZ_data = self.index_daily_path + '399300.SZ.csv'
        sz = pd.read_csv(SZ_data)
        sh = pd.read_csv(SH_data)

        ts_code_list = []
        stock_name_list = []
        industry_list = []
        market_list = []
        stock_beta_list = []

        stock_pool = pd.read_csv(self.stock_file)
        for index, row in stock_pool.iterrows():
            ts_code = row['ts_code']
            stock_name = row['name']
            industry = row['industry']
            market = row['market']
            exchange = row['exchange']
            stock_data_path = self.stock_daily_path + ts_code + '.csv'
            stock_data = pd.read_csv(stock_data_path)
            if len(stock_data) == self.trade_day:
                data = {
                    'trade_date': sz['trade_date'],
                    'index': sz['close'] if exchange == 'SZSE' else sh['close'],
                    'stock_data': stock_data['close']
                }

                df = pd.DataFrame(data=data, columns=['trade_date', 'index', 'stock_data'])
                df.set_index(["trade_date"], inplace=True)
                sec_returns = np.log(df / df.shift(1))
                cov = sec_returns.cov() * self.trade_day
                cov_with_market = cov.iloc[0, 1]
                market_var = sec_returns['index'].var() * self.trade_day
                stock_beta = cov_with_market / market_var

                ts_code_list.append(ts_code)
                stock_name_list.append(stock_name)
                industry_list.append(industry)
                market_list.append(market)
                stock_beta_list.append(stock_beta)

        betas = {
            'ts_code': ts_code_list,
            'stock_name': stock_name_list,
            'industry': industry_list,
            'market': market_list,
            'stock_beta': stock_beta_list
        }
        stock_bate_data_frame = pd.DataFrame(data=betas,
                                             columns=['ts_code', 'stock_name', 'industry', 'market', 'stock_beta'])
        stock_bate_data_frame.to_csv('./data/output/beta_list.csv', encoding='utf-8')
