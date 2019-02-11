from algos.MonteCarlo import MonteCarlo

ts_code = '000001.SZ'
start = '20150101'
end = '20190207'
t_intervals = 30
iterations = 5

mc = MonteCarlo(ts_code=ts_code, start=start, end=end, t_intervals=t_intervals, iterations=iterations)
mc.run_algo()
