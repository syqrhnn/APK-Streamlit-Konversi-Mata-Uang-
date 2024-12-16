import streamlit as st
import requests

# Function to get currency exchange rates
def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # Replace 'USD' with your base currency if needed
    response = requests.get(url)
    data = response.json()
    return data['rates']

# Function for currency conversion
def convert_currency(amount, from_currency, to_currencies, rates):
    converted_amounts = {}
    for currency in to_currencies:
        converted_amounts[currency] = amount * rates[currency]
    return converted_amounts

# Streamlit UI
def main():
    st.title("Konversi Mata Uang")

    # Input fields
    amount = st.number_input("Masukkan jumlah yang ingin dikonversi:", min_value=0.01, step=0.01)
    from_currency = st.selectbox("Dari mata uang:", ["USD", "EUR", "JPY", "IDR", "GBP", "AUD", "CAD", "CHF"])  # Tambahkan mata uang lain sesuai kebutuhan
    to_currencies = st.multiselect("Kepada mata uang:", ["EUR", "JPY", "IDR", "GBP", "AUD", "CAD", "CHF"])  # Bisa lebih dari satu mata uang

    # Get exchange rates
    rates = get_exchange_rates()

    # Convert and display results
    if st.button("Konversi"):
        converted_amounts = convert_currency(amount, from_currency, to_currencies, rates)
        for currency, converted_amount in converted_amounts.items():
            st.write(f"{amount} {from_currency} = {converted_amount:.2f} {currency}")

if __name__ == "__main__":
    main()
