import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
        self.rates = self.get_rates()

    def get_rates(self):
        response = requests.get(self.api_url)
        if response.status_code != 200:
            raise Exception("Failed to fetch exchange rates.")
        return response.json()["rates"]

    def convert(self, amount, from_currency, to_currency):
        if from_currency != "USD":
            amount /= self.rates[from_currency]
        converted_amount = amount * self.rates[to_currency]
        return converted_amount

def main():
    api_key = "3af215ae945a2dc9f3fe0fc7"  
    converter = CurrencyConverter(api_key)

    print("Добро пожаловать в Конвертер Валют!")
    amount = float(input("Введите сумму для конвертации: "))
    from_currency = input("Из какой валюты (например, USD): ").upper()
    to_currency = input("В какую валюту (например, EUR): ").upper()

    try:
        result = converter.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except KeyError:
        print("Ошибка: Неверный код валюты.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()