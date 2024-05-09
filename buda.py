from trading_api_wrappers import Buda
from datetime import datetime, timezone
import numpy as np
import pandas as pd
client = Buda.Public()
pd.set_option('display.float_format', '{:.2f}'.format)

# DATA NECESARIA
marketId = 'btc-clp'
firstDate = datetime(2024,3,1,12,0,0,0,timezone.utc)
lastDate = datetime(2024,3,1,13,0,0,0,timezone.utc)
fee = 0.008

def getTimestamp(date):
    return int(date.replace(tzinfo=timezone.utc).timestamp()* 1e3) # en milisegundos!

def getTransactions(marketId,timestamp,firstTimestamp):
    flag = True
    transactions = []
    while flag:
        trades = client.trades(marketId,timestamp=timestamp, limit=50)
        entries = list(trades[2])
        for entry in entries:
            actualTimestamp = entry[0]
            if actualTimestamp < firstTimestamp:
                flag = False
                break;
            else:
                transactions.append(np.array(entry))
                timestamp = actualTimestamp
    return transactions

def createDataFrame(transactions):
    df = pd.DataFrame(transactions, columns=['timestamp', 'amount', 'price', 'type'])
    df['value [CLP]'] = df['amount'].astype(float) * df['price'].astype(float)
    df['value [CLP]'] = df['value [CLP]'].astype(float)
    return df

def calculateTotalValueTraded(df):
    return round(df['value [CLP]'].sum(),2)

def calculateTotalBTCTraded(df):
    return df['amount'].astype(float).sum()

def calculatePercentageIncrease(initialValue, newValue):
    if initialValue == 0:
        raise ValueError("¡Initial value cannot be zero!")
    percentageIncrease = ((newValue - initialValue) / initialValue) * 100
    return round(percentageIncrease,2)

def calculateFeeAmount(totalTraded, fee):
    return round(totalTraded * fee,2)


firstTimestamp = getTimestamp(firstDate)
lastTimestamp = getTimestamp(lastDate)

transactions = getTransactions(marketId,lastTimestamp,firstTimestamp)
df = createDataFrame(transactions)

totalTraded = calculateTotalValueTraded(df)
print("totalTraded at black buda:",totalTraded)


#Año pasado
firstDate2023 = datetime(2023,3,1,12,0,0,0,timezone.utc)
lastDate2023 = datetime(2023,3,1,13,0,0,0,timezone.utc)
firstTimestamp2023 = getTimestamp(firstDate2023)
lastTimestamp2023 = getTimestamp(lastDate2023)

transactions2023 = getTransactions(marketId,lastTimestamp2023,firstTimestamp2023)
df2023 = createDataFrame(transactions2023)

#Total tradeado en 2023 misma fecha y hora
totalTraded2023 = calculateTotalValueTraded(df2023)
print("totalTraded at black buda 2023:",totalTraded2023,"\n")

#Cuánto creció porcentualmente entre 2023 y 2024? [BTC]
totalBTCTraded = calculateTotalBTCTraded(df)
totalBTCTraded2023 = calculateTotalBTCTraded(df2023)
percentageIncreaseByBTC = calculatePercentageIncrease(totalBTCTraded2023,totalBTCTraded)
print("percentageIncreaseByBTC:",percentageIncreaseByBTC,"%","\n")

#Cuanto dinero se dejó de ganar por el evento
moneyLost = calculateFeeAmount(totalTraded,fee)
print("moneyLost:",moneyLost,"\n")