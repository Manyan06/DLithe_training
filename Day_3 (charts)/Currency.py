exchange_rates = {
  "INR": 1.0,
  "USD": 0.0105, # 1 Rs = 1/Exchange rate ===  1 / 94.85 USD = 0.0105 INR
  "EUR": 0.0090, # 1/ 110.79 = 0.0090 Rs
  "GBP": 0.0078, # 1/127.68 = 0.0078
  "JPY": 1.6667  # 1/0.60 = 1.6667
}

def convert_currency(amount, from_currency,to_currency):
  amount_in_inr= amount / exchange_rates[from_currency]
  converted_amount = amount_in_inr * exchange_rates[to_currency]
  return converted_amount

amount = float(input("Enter Amount: "))
from_currency = input("From Currency (USD, EUR, INR, GBP, JPY): ").upper()
to_currency = input("To Currency (USD, EUR, INR, GBP, JPY): ").upper()

if from_currency not in exchange_rates or to_currency not in exchange_rates:
  print("Invalid Currency")
else:
  result = convert_currency(amount, from_currency,to_currency)
  print(f"{amount} {from_currency} = {result:.2f} {to_currency}")