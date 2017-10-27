def ticker():
    antw = input("Give a company name: ")
    ticker_symbol = {'YAHOO':"YHOO", "GOOGLE INC":"GOOG", "Harley-Davidson":"HOG", "Yamana Gold":"AUY","Sotheby's":"BID", "inBev":"BUD"}
    print("Ticker symbol:", ticker_symbol[antw])

ticker()