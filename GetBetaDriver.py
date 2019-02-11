from algos.CAPM import CAPM
from config import conf

stock_file = conf.stock_code_file
index_daily_path = conf.index_daily_path
stock_daily_path = conf.stock_daily_path
trade_day = conf.trade_day

capm = CAPM(stock_file=stock_file, index_daily_path=index_daily_path, stock_daily_path=stock_daily_path,
            trade_day=trade_day)
capm.go_beta()
