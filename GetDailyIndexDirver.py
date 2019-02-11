import pandas as pd
from tools.GetDailyData import get_daily_index
from config import conf

index_codes = conf.index_codes
start = conf.start
end = conf.end

for code in index_codes:
    result = get_daily_index(code,start,end)
    file_name = './data/index/{}.csv'.format(code)
    result.to_csv(file_name,index=0,encoding='utf-8')

