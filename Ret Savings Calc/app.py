#import necessary folders
import numpy as np 
import streamlit as st
import matplotlib.pyplot as plt
import yfinance as yf

#years until money runs out calculation
def years_after(balance, rate, withdrawal):
    for i in range(1, 150):  
        interest = balance * rate / 100
        if withdrawal <= interest:
            return "You can live off interest forever!"
        balance = balance + interest - withdrawal
        if balance < 0:
            return i
    return "150+ years"

st.title("Retirement Calculator")
st.header("Calculate Your Retirement Savings and Strategy in Ideal Conditions")

#take necessary input with streamlit
age = st.slider("Current Age", 18, 100)
ret_age = st.slider("Retirement Age", 19, 100)
bal = st.number_input("Starting Balance", 0, None)
temp_bal = ret_bal = bal 
int_rate = st.number_input("Interest Rate (%)", 0, 100)
contr = st.number_input("Annual Contribution", 0, None)
spending = st.number_input("Annual Withdrawal During Retirement", 0, None)

#basic number crunching
years = ret_age - age
for i in range(years):
    ret_bal = (ret_bal + contr)*(1+int_rate/100)
total_interest = ret_bal - bal - contr*years
zero_age = years_after(ret_bal, int_rate/100, spending)

#display results numerically
st.subheader(f"Savings at Retirement: ${ret_bal:,.2f}")
st.subheader(f"Total Interest Gained: ${total_interest:,.2f}")
st.subheader(f"Years Living Off Interest: {zero_age}") 

#plot results in numpy
st.subheader("Graph of Retirement Savings Over Time")
x = np.arange(0, years + 1) 
y = []
current = bal
for _ in range(years + 1):
    y.append(current)
    current = (current + contr) * (1 + int_rate / 100)
plt.figure(figsize=(10, 5))
plt.grid(True)
plt.plot(x, y)
plt.xlabel("Years")
plt.ylabel("Balance")
plt.title("Retirement Savings Over Time")
st.pyplot(plt)
#plot market average returns on top of the graph
market_returns = [0.08] * (years + 1)  # Assuming a constant 8% market return
plt.plot(x, [bal * (1 + r) ** x for r in market_returns], label='Market Average Returns', linestyle='--')
plt.legend()

# Strategy Testing
#Test strategy against historical market data from yahoo finance
st.header("Calculate Your Strategy in Previous Market Conditions")
st.subheader("This section allows you to test your retirement strategy against historical S&P 500 data to see how it would have performed in the past with the starting balance and contributions as above.")

# Get user input for start year and end year (annual for the sake of simplicity)
start_year = st.number_input("Start Year for Historical Data", 1958, 2023, value=2007) # Default to 2007
end_year = st.number_input("End Year for Historical Data", 1900, 2023, value=2023) # Default to 2023

# Get historical data for S&P 500
start_date = f"{start_year}-01-01"
end_date = f"{end_year}-12-31"  
data = yf.download("SPY", start=start_date, end=end_date)
close = data['Close'] 
annual_close = close.resample('YE').last() # Close price of the year
annual_returns = annual_close.pct_change().dropna() #drop 0s and calculate annual returns
annual_balances = []
adjusted_balance = bal

# Balance with interest and contributions
for i in range(len(annual_returns)):
    adjusted_balance = adjusted_balance * (1 + annual_returns.iloc[i]) + contr
    annual_balances.append(adjusted_balance)
adjusted_balance = (float(adjusted_balance))

plt.figure(figsize=(10, 5))
plt.grid(True)
yrs = np.arange(start_year, start_year + len(annual_balances))
plt.plot(yrs, annual_balances, label='Your Strategy', color='blue')
plt.xlabel("Years")
plt.ylabel("Balance")
plt.title("Retirement Savings Over Time with Historical Market Data")
plt.legend()
st.pyplot(plt)

average_return = 100*(float)(annual_returns.mean())
int_gained = adjusted_balance - bal - contr * (end_year - start_year)

st.subheader(f"Savings at Retirement with Historical Data: ${adjusted_balance:,.2f}")
st.subheader(f"Total Interest Gained with Historical Data: ${int_gained:,.2f}")
st.subheader(f"Average Annual Return During This Period: {average_return:.2f}%")