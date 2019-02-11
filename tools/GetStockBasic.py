import tushare as ts

ts.set_token('519ade7742d87ada41e0aba865dbecfadeed0a4443f6f88ff6a300a2')
pro = ts.pro_api()

def get_stock_basic():
    data = pro.query('stock_basic', exchange='', list_status='L',
                    fields='ts_code,symbol,exchange,name,market,area,industry,is_hs')

    data.rename(columns={'symbol': 'code'}, inplace=True)

    return data


if __name__ == '__main__':
    data = get_stock_basic()
    print(data)


