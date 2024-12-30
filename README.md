# Arbitrage Opportunity Script

This Python script helps detect arbitrage opportunities using the Call-Put Parity for European options. It enables users to analyze either **call options** or **put options**, calculate synthetic prices, and visualize payoff comparisons.

## Features
- **Synthetic vs. Market Option Prices:** Compares synthetic and market option prices to identify arbitrage opportunities.
- **Arbitrage Detection:** Provides clear recommendations for arbitrage actions.
- **Payoff Visualization:** Graphically represents the payoffs for synthetic and market options.

## Usage
1. Clone this repository or download the `arbitrage_opportunity.py` file.
2. Ensure you have `Python 3.12` installed along with the required libraries (e.g., `matplotlib`, `pandas`, `numpy`).
3. Run the script in your terminal or IDE:
   ```bash
   python arbitrage_opportunity.py
   ```
4. Follow the prompts to:
   - Choose between analyzing **call options** or **put options**.
   - Enter the required parameters, such as option prices, strike price, risk-free rate, and time to maturity.

## Parameters
- **Market Call Price:** The market price of the call option (e.g., `3.00`).
- **Market Put Price:** The market price of the put option (e.g., `2.25`).
- **S_0:** Current stock price (e.g., `31.00`).
- **S_K:** Strike price of the option (e.g., `30.00`).
- **rf:** Risk-free interest rate (as a decimal, e.g., `0.10`).
- **T:** Time to maturity (in years, e.g., `0.25`).
- **D:** Dividend yield (as a decimal, e.g., `0.00`).

## Output
After running the script, you will receive:
- Detailed arbitrage analysis in a tabular format.
- Visual payoff comparison for synthetic and market options.

### Arbitrage Recommendations Example:
For a **put option**, you might see:
```
===== Arbitrage Opportunity Detected =====
- Sell the market put at 2.25
- Buy the synthetic put at 1.75

To buy the synthetic put:
  - Buy the call at 3.00
  - Short the stock at 31.00
  - Invest in a risk-free bond at 29.25
```

For a **call option**, you might see:
```
===== Arbitrage Opportunity Detected =====
- Buy the market call at 3.00
- Sell the synthetic call at 2.85

To sell the synthetic call:
  - Sell the put at 2.25
  - Sell the stock at 31.00
  - Invest in a risk-free bond at 29.25
```

If there is no arbitrage opportunity, you will see:
```
===== No Arbitrage Opportunity =====
Synthetic and market prices are in equilibrium.
No further actions are required.
```
## Requirements
Ensure the following Python libraries are installed:
- `math`
- `numpy`
- `pandas`
- `matplotlib`

Install missing libraries using:
```bash
pip install numpy pandas matplotlib
```

## Contributions
This project is for personal and educational use only. Contributions are not currently open.

## Author
**Sacha**

## Disclaimer
This script is for educational purposes only. It is not financial advice, and the author assumes no responsibility for any actions taken based on the results of this script.
