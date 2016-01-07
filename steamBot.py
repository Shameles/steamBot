
#kev's steam script for auto buy and sell

#pistols
'''
import json

#24 hour list, max 100 elements
#importList = "http://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name=StatTrak%E2%84%A2%20P250%20%7C%20Steel%20Disruption%20%28Factory%20New%29"
importList = '{"fruits":["apple", "banana", "orange"]}'
priceArray = json.loads(importList);

print (priceArray['fruits'])
'''
import constants
#
print("steamBot v1")

lowestPrice = float(input("Lowest item price = "))
averagePrice = float(input("Average item price = "))

if lowestPrice <= averagePrice - (averagePrice*constants.BUY_MARGIN):

	print("Bought for ", lowestPrice)
	fees = float(averagePrice * (constants.CSGO_FEE + constants.STEAM_FEE))
	profit = (averagePrice - fees - lowestPrice)
	profitPercentile = float(profit/averagePrice)
	print("Profit ", profit)
	print("Profit Percentile ", profitPercentile)

	profitMargin = constants.PROFIT_MARGIN

	profitLimit = constants.PROFIT_PERCENTILE_HIGH

	if averagePrice > constants.PROFIT_CASH_MARGIN:
		profitLimit = constants.PROFIT_PERCENTILE_LOW

	print("Profit Limit ", profitLimit)

	if profitPercentile >= profitLimit:
		print("BUY")

else:
	print("DO NOT BUY")
