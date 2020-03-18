# Encephalo Investments Coding Pre-Test - main.py
import pandas as pd


def main():
    # main function.
    # Return the top 10 companies with the highest market cap.
    data = pd.read_csv("./data.csv") # read csv using pandas
    
    data_market_cap = data.sort_values(by = 'market_cap', ascending = False)
    
    return data_market_cap.iloc[0:10,0]
    


if __name__ == "__main__":
    main()
