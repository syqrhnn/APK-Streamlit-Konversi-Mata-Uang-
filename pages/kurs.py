import streamlit as st
import requests

# Function to get currency exchange rates
def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # API untuk kurs mata uang biasa
    response = requests.get(url)
    data = response.json()
    return data['rates']

# Function to get cryptocurrency rates
def get_crypto_rates():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data

# Function for currency conversion
def convert_currency(amount, from_currency, to_currencies, rates):
    converted_amounts = {}
    for currency in to_currencies:
        converted_amounts[currency] = amount * rates[currency]
    return converted_amounts

# Function for cryptocurrency conversion
def convert_crypto(amount, from_crypto, to_crypto, rates):
    from_to_usd = rates[from_crypto]
    to_amount = amount * from_to_usd / rates[to_crypto]
    return to_amount

# Streamlit UI
def main():
    st.title("Aplikasi Konversi Mata Uang dengan Kurs Mata Uang Kripto")

    # Input fields
    amount = st.number_input("Masukkan jumlah yang ingin dikonversi:", min_value=0.01, step=0.01)
    from_currency = st.selectbox("Dari mata uang:", ["USD", "EUR", "JPY", "IDR", "GBP", "AUD", "CAD", "CHF", "BTC", "ETH"])  # Tambahkan mata uang kripto
    to_currencies = st.multiselect("Kepada mata uang:", ["EUR", "JPY", "IDR", "GBP", "AUD", "CAD", "CHF", "BTC", "ETH"])  # Bisa lebih dari satu mata uang

    # Get exchange rates
    rates = get_exchange_rates()

    # Get cryptocurrency rates
    crypto_rates = get_crypto_rates()

    # Convert and display results
    if st.button("Konversi"):
        if from_currency in ["BTC", "ETH"]:
            # Convert from crypto to other crypto or fiat currencies
            converted_amounts = convert_crypto(amount, from_currency.lower(), to_currencies, crypto_rates)
        else:
            # Convert from fiat to other fiat currencies
            converted_amounts = convert_currency(amount, from_currency, to_currencies, rates)

        for currency, converted_amount in converted_amounts.items():
            st.write(f"{amount} {from_currency} = {converted_amount:.2f} {currency}")

if __name__ == "__main__":
    main()

