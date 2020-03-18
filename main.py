# Encephalo Investments Coding Pre-Test - main.py
import pandas as pd


def main():
    # main function.
    # Return the top 10 companies with the highest market cap.
    data = pd.read_csv("./data.csv") # read csv using pandas
    data['market_cap'] = data['market_cap'].str.replace('$','')

    def to_float(x):
        if type(x) == float or type(x) == int:
            return x
        if 'M' in x:
            return float(x.replace('M', '')) * 1000000

        if 'B' in x:
            return float(x.replace('B', '')) * 1000000000

    data.market_cap = data.market_cap.apply(to_float)

    market_cap = data.sort_values(by = 'market_cap',ascending = False).head(10)
    return market_cap['ticker']
if __name__ == "__main__":
    main()
