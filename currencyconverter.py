#Currency Converter
from forex_python.converter import CurrencyRates
c = CurrencyRates()
print(c.convert('USD','INR',1))
