# Mike Wooldridge
# SWDV 600 2W 21/FA1
# Week 1 Review Programming Exercise 2
# Bitcoin Converter
#   Convert bit coin to US dollars
# Sample output:
#   As of 8/1/17 at 11:13 am, bitcoin is currently trading at $2086 per bitcoin.
#   Enter the bitcoin amount: .5
#   That is worth 1043 us dollars.
# 8/26/21 at 2:20pm $46,953.29 per bitcoin
bitcoinPricePerUnit = 47953
print("As of 8/26/21 at 2:20pm, bitcoin is currently trading at $47953 per bitcoin")
bitcoinInput = input("Enter the bitcoin amount:  ")
bitcoins = float(bitcoinInput)
bitcoinValue = round(bitcoins * bitcoinPricePerUnit)
print("That is worth " + str(bitcoinValue) + " US dollars.")
print()
