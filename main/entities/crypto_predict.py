class CryptoPredict:
    """Class which represents a forecast of the value of a crypto asset"""
    def __init__ (self, product: str, current_price: float, forecasted_price: float):
        self.product = product
        self.current_price = current_price
        self.forecasted_price = forecasted_price

