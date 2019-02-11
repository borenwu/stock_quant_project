import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from tools.GetDailyData import get_daily_data


class MonteCarlo:
    def __init__(self, ts_code, start, end, t_intervals, iterations):
        self.ts_code = ts_code
        self.start = start
        self.end = end
        self.t_intervals = t_intervals
        self.iterations = iterations

    def run_algo(self):
        stock = get_daily_data(self.ts_code, self.start, self.end)[['trade_date', 'close']]
        log_returns = np.log(1 + stock['close'].pct_change())

        u = log_returns.mean()
        var = log_returns.var()
        drift = u - (0.5 * var)
        stdev = log_returns.std()

        daily_returns = np.exp(drift + stdev * norm.ppf(np.random.rand(self.t_intervals, self.iterations)))
        S0 = stock.iloc[-1]

        price_list = np.zeros_like(daily_returns)
        price_list[0] = S0[1]

        for t in range(1, self.t_intervals):
            price_list[t] = price_list[t - 1] * daily_returns[t]

        print(price_list.min())
        print(price_list.max())

        plt.figure(figsize=(10, 6))
        plt.plot(price_list)
        plt.show()
