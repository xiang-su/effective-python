import matplotlib
import matplotlib.pyplot as plt
import tushare as ts
from matplotlib.pylab import datestr2num

# 设置中文字体
font = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

# 获取实时行情数据
hq = ts.get_today_all()
# 节选出股票代码code、名称name、涨跌幅changepercent、股价trade
hq = hq[['code', 'name', 'changepercent', 'trade']]

# 筛选出当前股价高于0元低于3元的股票信息
mins = hq.trade > 0.00
maxs = hq.trade <= 2.99
allselect = mins & maxs
# data = hq[allselect].sort('trade')
data = hq[allselect]

# 提取低价股股票代码,并剔除深圳成指股票
code_list = []
for c in data.code:
    if c[0] != "0":
        code_list.append(c)
code_list

sh_hist_data = ts.get_hist_data(code='sh', start='2014-12-01', end='2016-12-01')
sh_hist_data = sh_hist_data[['open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change']].sort_index()

sh_hist_data.head(10)
dates = [datestr2num(i) for i in sh_hist_data.index]
plt.figure(figsize=(40, 30))
# 新建一个子图，绘制上证指数走势
plt.subplot(311)
plt.title("2014年12月1日至2016年12月1日上证指数最低价走势", fontsize=30)
plt.xticks(rotation=20, fontsize=26)
plt.yticks(fontsize=26)
plt.plot_date(dates, sh_hist_data.low, '-', linewidth=2.5)
plt.grid(True)
# 遍历低价股代码列表，绘制股价走势
for i in code_list[0:4]:
    hist_data = ts.get_hist_data(code=i, start='2014-12-01', end='2016-12-01')
    code_data = hist_data[['open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change']].sort_index()
    dates = [datestr2num(t) for t in code_data.index]
    plt.subplot(312)
    plt.title("2014年12月1日至2016年12月1日各低价股最低价走势", fontsize=30)
    plt.xticks(rotation=20, fontsize=26)
    plt.yticks(fontsize=26)
    plt.plot_date(dates, code_data['low'], '-', linewidth=2.5, label=i)
    plt.legend(loc=1, fontsize=22)
    plt.grid(True)
for i in code_list[4:]:
    hist_data = ts.get_hist_data(code=i, start='2014-12-01', end='2016-12-01')
    code_data = hist_data[['open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change']].sort_index()
    dates = [datestr2num(t) for t in code_data.index]
    plt.subplot(313)
    plt.title("2014年12月1日至2016年12月1日各低价股最低价价走势", fontsize=30)
    plt.xticks(rotation=20, fontsize=26)
    plt.yticks(fontsize=26)
    plt.plot_date(dates, code_data['low'], '-', linewidth=2.5, label=i)
    plt.legend(loc=1, fontsize=22)
    plt.grid(True)
