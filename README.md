# Arbitrage Opportunity Script

This Python script provides solutions for detecting arbitrage opportunities using the **Call-Put Parity** for European options. It allows users to analyze **call options** and **put options**, calculate synthetic prices, visualize payoff comparisons, and detect arbitrage opportunities.

## Features
- **Synthetic vs. Market Option Prices**: Computes synthetic call and put prices based on the Call-Put Parity formula and compares them to market prices.
- **Arbitrage Detection**: Identifies arbitrage opportunities and provides actionable recommendations with step-by-step instructions.
- **Payoff and Component Visualization**: Graphically represents payoff comparisons and synthetic option components for better understanding.

## Usage
1. Clone this repository or download the `arbitrage_opportunity.py` file.
2. Ensure you have Python 3.12+ installed along with the required libraries (`matplotlib`, `pandas`, `numpy`).
3. Run the script in your terminal or IDE:
   ```bash
   python arbitrage_opportunity.py
   ```
4. Follow the prompts to:
   - Enter the required parameters.

## Parameters
You will be prompted to input the following parameters:
- **Market Call Price**: The market price of the call option (e.g., `3.00`).
- **Market Put Price**: The market price of the put option (e.g., `2.25`).
- **S_0**: Current stock price (e.g., `31.00`).
- **K**: Strike price of the option (e.g., `30.00`).
- **rf**: Risk-free interest rate (as a decimal, e.g., `0.10` for 10%).
- **T**: Time to maturity (in years, e.g., `0.25`).
- **D**: Dividend yield (as a decimal, e.g., `0.00` for no dividends).

### Input Example:
```
Please enter the following parameters (use ',' or '.' as separator & don't include thousands separator):
Enter the market call price: 3.00
Enter the market put price: 2.25
Enter the current stock price (S_0): 31.00
Enter the strike price (K): 30.00
Enter the risk-free rate (e.g., 0.10 for 10%): 0.10
Enter the time to maturity (T, in years): 0.25
Enter the dividend yield (e.g. '0' for no dividends): 0.00
```

## Output
After running the script, you will receive:
- A **table of input parameters** for clarity.
- Detailed **arbitrage analysis** for both call and put options, with actionable recommendations.
- **Payoff comparisons** for synthetic and market options, plotted for visualization.
- **Synthetic option components** plotted to illustrate their value contributions.

### Arbitrage Recommendations Example:
For a **call option**, you might see:
```
=== Arbitrage Opportunity Detected for Calls ===
- Short the market call at 3.00
- Long the synthetic call at 2.85

To do so:
  - Buy the put at 2.25
  - Buy the stock at 31.00
  - Borrow at a risk-free rate such that pv_K = 29.25
```

For a **put option**, you might see:
```
=== Arbitrage Opportunity Detected for Puts ===
- Buy the market put at 2.25
- Short the synthetic put at 2.85

To do so:
  - Sell the call at 3.00
  - Buy the stock at 31.00
  - Borrow at a risk-free rate such that pv_K = 29.25
```

If there is no arbitrage opportunity, the output will state:
```
No Arbitrage Opportunity for Calls: Synthetic and market option prices are in equilibrium.
No Arbitrage Opportunity for Puts: Synthetic and market put prices are in equilibrium.
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
Contributions are not currently open.

## Author
**Sacha D.**

## Disclaimer
This script is for educational purposes only. It is not financial advice, and the author assumes no responsibility for any actions taken based on the results of this script.
