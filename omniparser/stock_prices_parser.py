
# omniparser/gradebook_parser.py

import os
import statistics
import json
import pandas


def calculate_average_stock_from_json(x):
    

    with open(x, "r") as f:
        #print(type(f))
        file_contents = f.read()
        #print(type(file_contents))

    stock_list = json.loads(file_contents)
    #print(type(gradebook))
    #print(gradebook)
    stocks = stock_list ["stock_prices"]
    stock_prices = [s["4. close"] for s in stocks]
    avg_stock_price = statistics.mean(stock_prices)
    
    return avg_stock_price

if __name__ == "__main__":   

    print("PARSING SOME JSON STOCK FILES HERE...")
    app_stock_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices_aapl.json")
    print(app_stock_filepath)
    print(os.path.isfile(app_stock_filepath))
    avg = calculate_average_stock_from_json(app_stock_filepath)
    print(avg)
