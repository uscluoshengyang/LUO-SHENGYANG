# Encephalo Investments Coding Pre-Test - main.py
import pandas as pd


def main():
    # main function.
    # Return the top 10 companies with the highest market cap.
    data = pd.read_csv("./data.csv") # read csv using pandas
    data.sort_index(by=u'market_cap')
    
    


if __name__ == "__main__":
    main()
