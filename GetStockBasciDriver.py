import pandas as pd
from tools.GetStockBasic import get_stock_basic

df = get_stock_basic()
df.to_csv('./data/basic/stk_code_full.csv',index=0,encoding='utf-8')