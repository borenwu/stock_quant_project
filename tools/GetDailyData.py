import tushare as ts

ts.set_token('519ade7742d87ada41e0aba865dbecfadeed0a4443f6f88ff6a300a2')
pro = ts.pro_api()


def get_daily_index(ts_code, start, end):
    data = pro.index_daily(ts_code=ts_code, start_date=start, end_date=end)
    result = data.sort_values(by="trade_date", ascending=True)
    return result

def get_daily_data(ts_code, start, end):
    data = pro.daily(ts_code=ts_code, start_date=start, end_date=end)
    result = data.sort_values(by="trade_date", ascending=True)
    return result


if __name__ == '__main__':
    result = get_daily_data('000002.SZ', '20180101', '20181231')
    print(result)
