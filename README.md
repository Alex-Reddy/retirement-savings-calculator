# Retirement Savings Calculator

This is a Python-based interactive retirement calculator built with **Streamlit**. It estimates how your savings grow over time and tests your strategy using **real historical stock market data** via `yfinance`. Designed for finance students, analysts, and anyone interested in understanding long-term investment behavior.
Python interactive savings calculator with Streamlit, Numpy, Matplotlib, and YFinance

## Features

### Ideal Scenario Calculator
- Input user input for starting age, balance, interest, future contributions, and retirement age
- Outputs:
  - Final balance at retirement
  - Total interest earned
  - Years your money will last in retirement
  - Interactive growth graph

### Historical Strategy Backtester
- Test your strategy against the S&P 500 in past years
- Outputs:
  - Realistic savings growth graph
  - Actual average return
  - Historical total interest earned

---

##  Download and Set Up Locally

   ```bash
   #clone repository
   git clone https://github.com/Alex-Reddy/retirement-calculator.git
   cd retirement-savings-calculator

   #install dependencies
   pip install -r requirements.txt
   
   #run the app
   streamlit run app.py
```
## Purpose

This project was designed to familiarize me with Python and popular libraries in finance, namely NumPy, Matplotlib, and yfinance. This calculator is fairly minimalist, and I do plan on working with more in-depth financial modeling in the future, but such features would not make sense to put in a simple retirement calculator.
