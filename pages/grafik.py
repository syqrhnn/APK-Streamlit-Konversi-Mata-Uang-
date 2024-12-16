import streamlit as st
import requests
import matplotlib.pyplot as plt
import datetime

# Function to get historical exchange rates
def get_historical_rates(from_currency, to_currency, start_date, end_date):
    url = f"https://api.exchangerate-api.com/v4/history/{from_currency}/{to_currency}?start={start_date}&end={end_date}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()['rates']
        return data
    else:
        st.error(f"Error: Unable to fetch data (status code {response.status_code})")
        return None

# Function to plot exchange rate trend
def plot_exchange_rate_trend(rates, title):
    if not rates:
        st.error("Tidak ada data yang ditemukan untuk grafik.")
        return
    
    dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in rates.keys()]
    values = [rate for rate in rates.values()]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o')
    plt.title(title)
    plt.xlabel("Tanggal")
    plt.ylabel("Nilai Tukar")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot()

# Streamlit UI
def main():
    st.title("Aplikasi Konversi Mata Uang dengan Grafik Nilai Tukar")

    # Input fields
    from_currency = st.selectbox("Dari mata uang:", ["USD", "EUR", "JPY", "IDR", "GBP", "AUD", "CAD", "CHF"])  # Tambahkan mata uang lain sesuai kebutuhan
    to_currency = st.selectbox("Kepada mata uang:", ["EUR", "JPY", "IDR", "GBP", "AUD", "CAD", "CHF"])  # Bisa lebih dari satu mata uang
    start_date = st.date_input("Mulai tanggal:", value=datetime.date.today() - datetime.timedelta(days=30))
    end_date = st.date_input("Sampai tanggal:", value=datetime.date.today())
    
    # Get historical rates
    if start_date and end_date and st.button("Tampilkan Grafik"):
        rates = get_historical_rates(from_currency, to_currency, start_date, end_date)
        if rates:
            plot_exchange_rate_trend(rates, f"Fluktuasi Nilai Tukar {from_currency} ke {to_currency} dari {start_date} hingga {end_date}")

if __name__ == "__main__":
    main()
