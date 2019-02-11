import pandas as pd
from tools.GetDailyData import get_daily_data
from config import conf

stock_code_file = conf.stock_code_file
start = conf.start
end = conf.end

stkPool = pd.read_csv(stock_code_file, encoding='utf-8');

for index, row in stkPool.iterrows():
    length = len(stkPool['ts_code']);
    ts_code = row["ts_code"]
    xc = row["code"]
    code = "%06d" % xc
    print("\n", index, "/", length, "code,", ts_code)
    df = get_daily_data(ts_code,start,end)
    df['code'] = code
    save_file = './data/daily/{}.csv'.format(ts_code)
    df.to_csv(save_file,index=0,encoding='utf-8')