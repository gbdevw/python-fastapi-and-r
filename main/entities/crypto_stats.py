class CryptoStats:
    """POJO which contains trading stats for a currency pair"""
    def __init__ (self, open: float = 0.0, high: float = 0.0, low: float = 0.0, volume: float = 0.0, last: float = 0.0, volume30d: float = 0.0):
        self.open = open
        self.high = high
        self.low = low
        self.volume = volume
        self.last = last
        self.volume30d = volume30d