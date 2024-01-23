name = "大逛逛"
stock_price = 19.99
stock_code = 123456
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_price = stock_price_daily_growth_factor ** growth_days * stock_price

print(f"公司{name},股票代码:{stock_code},股票价格:{stock_price}")
print("每日增长系数: %.1f,经过%d天增长后，价格达到%.2f" % (stock_price_daily_growth_factor,growth_days,finally_price))