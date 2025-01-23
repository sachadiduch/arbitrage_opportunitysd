#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 12:21:52 2024

@author: sacha
"""

''' This script s intended to provide solutions in dectecting arbitrage opportunity 
using the Call-Put parity for European Options'''
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#dictionary that will contain user inputs

def parametersinputs():
    print("Please enter the following parameters (use ',' or '.' as separator & don't include thousands seperator'):")
    
    def getinputs(prompt): #allows the use of "," and "."
        return float(input(prompt).replace(',','.'))
    
    market_call_price = getinputs("Enter the market call price: ")
    market_put_price = getinputs("Enter the market put price: ")
    S_O = getinputs("Enter the current stock price (S_0): ")
    S_K = getinputs("Enter the strike price (K): ")
    rf = getinputs("Enter the risk-free rate (e.g., 0.10 for 10%): ")
    T = getinputs("Enter the time to maturity (T, in years): ")
    D = getinputs("Enter the dividend yield (e.g. '0' for no dividends): ")

    #dictionary containing inputs ready for computations
    return {
        'market_call_price': market_call_price,
        'market_put_price': market_put_price,
        'S_O': S_O,
        'S_K': S_K,
        'rf': rf,
        'T': T,
        'D': D
    }
# Function to calculate the syntethic call price
def calculate_synthetic_call(parameters):
    # adjusted spot price with dividend
    S_0_adjusted = parameters['S_O'] * math.exp(-parameters['D'] * parameters['T'])
    # PV of K value (K * exp^(-rT))
    pv_K = parameters['S_K'] * math.exp(-parameters['rf'] * parameters['T'])
    # compute the syntethic put
    synthetic_call = parameters['market_put_price'] + S_0_adjusted - pv_K
    return synthetic_call

# Function to calculate the syntethic put price
def calculate_synthetic_put(parameters):
    # adjusted spot price with dividend
    S_0_adjusted = parameters['S_O'] * math.exp(-parameters['D'] * parameters['T'])
    # PV of K value (K * exp^(-rT))
    pv_K = parameters['S_K'] * math.exp(-parameters['rf'] * parameters['T'])
    # compute the syntethic put
    synthetic_put = parameters['market_call_price'] - S_0_adjusted + pv_K
    return synthetic_put

# funtion to compute difference between market and synthetic call
def calldiff(synthetic_call, market_call):
    pricediffc = synthetic_call - market_call
    print(f' The calculated price difference is : {pricediffc}')
    return pricediffc

# funtion to compute difference between market and synthetic put
def putdiff(synthetic_put, market_put):
    pricediffp = synthetic_put - market_put
    print(f' The calculated price difference is : {pricediffp}')
    return pricediffp



#plot components of synthetic call
def plot_synthetic_call_components(parameters, synthetic_call):
    S_0_adjusted = parameters['S_O'] * math.exp(-parameters['D'] * parameters['T'])
    pv_K = parameters['S_K'] * math.exp(-parameters['rf'] * parameters['T'])

    components = ['Market Put Price', 'Adjusted Spot Price', 'PV of Strike']
    values = [parameters['market_put_price'], -S_0_adjusted, pv_K]

    plt.barh(components, values, color=['green', 'red', 'purple'])
    plt.title('Synthetic Call Price Components')
    plt.xlabel('Value Contribution')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.show()
    
#plot components of synthetic put
def plot_synthetic_put_components(parameters, synthetic_put):
    S_0_adjusted = parameters['S_O'] * math.exp(-parameters['D'] * parameters['T'])
    pv_K = parameters['S_K'] * math.exp(-parameters['rf'] * parameters['T'])

    components = ['Market Call Price', 'Adjusted Spot Price', 'PV of Strike']
    values = [parameters['market_call_price'], -S_0_adjusted, pv_K]

    plt.barh(components, values, color=['green', 'red', 'purple'])
    plt.title('Synthetic Put Price Components')
    plt.xlabel('Value Contribution')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.show()


#plot payoff call
def plot_payoffc(parameters):
    import numpy as np

    # Parameters
    K = parameters['S_K']  # Strike price
    rf = parameters['rf']  # Risk-free rate
    T = parameters['T']    # Time to maturity
    S_T = np.linspace(0, 2 * K, 500)  # Range of stock prices at maturity

    # Market call payoff
    market_call_payoff = np.maximum(S_T - K, 0)

    # Synthetic call payoff components
    long_stock = S_T
    short_bond = -K * math.exp(-rf * T)
    long_put = np.maximum(K - S_T, 0)

    # Synthetic call payoff
    synthetic_call_payoff = long_stock + long_put + short_bond

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(S_T, market_call_payoff, label='Market Call Payoff', linestyle='-', color='blue')
    plt.plot(S_T, synthetic_call_payoff, label='Synthetic Call Payoff', linestyle='--', color='orange')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.title('Synthetic vs. Market Call Payoffs')
    plt.xlabel('Stock Price at Maturity (S_T)')
    plt.ylabel('Payoff')
    plt.legend()
    plt.grid(True)
    plt.show()


#plot payoff put
def plot_payoffp(parameters):

    # Parameters
    K = parameters['S_K']  # Strike price
    rf = parameters['rf']  # Risk-free rate
    T = parameters['T']    # Time to maturity
    S_T = np.linspace(0, 2 * K, 500)  # Range of stock prices at maturity

    # Market put payoff
    market_put_payoff = np.maximum(K - S_T, 0)

    # Synthetic put payoff components
    long_call = np.maximum(S_T - K, 0)
    short_stock = -S_T
    long_bond = K * math.exp(-rf * T)

    # Synthetic put payoff
    synthetic_put_payoff = long_call + short_stock + long_bond

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(S_T, market_put_payoff, label='Market Put Payoff', linestyle='-', color='blue')
    plt.plot(S_T, synthetic_put_payoff, label='Synthetic Put Payoff', linestyle='--', color='orange')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.title('Synthetic vs. Market Put Payoffs')
    plt.xlabel('Stock Price at Maturity (S_T)')
    plt.ylabel('Payoff')
    plt.legend()
    plt.grid(True)
    plt.show()



#function to detect opportunity and provide recommendations
def recommend(parameters):
    #Compute synthetic call by calling function
    synthetic_call = calculate_synthetic_call(parameters)
    # Get the market call price
    market_call = parameters['market_call_price']
    # Calculate call price difference by calling function
    call_price_diff = calldiff(synthetic_call, market_call)
    
    #Compute synthetic put by calling function
    synthetic_put = calculate_synthetic_put(parameters)
   
    # Get the market put price
    market_put = parameters['market_put_price']
    # Calculate put price difference by calling function
    put_price_diff = putdiff(synthetic_put, market_put)
   

   #==========Data Frames creation==========
   # Create a DataFrame for input parameters
    input_df = pd.DataFrame.from_dict(parameters, orient='index', columns=['Value'])
    print("\n===== Input Parameters =====")
    print(input_df)
    print()
   
    #data frame for the elements computed
    data = {
        'Synthetic Put Price': [synthetic_put],
        'Market Put Price': [market_put],
        'Put Price Difference': [put_price_diff],
        'Synthetic Call Price': [synthetic_call],
        'Market Call Price': [market_call],
        'Call Price Difference': [call_price_diff]}
    details_df = pd.DataFrame(data)

    print("\n===== Arbitrage Details =====")
    print(details_df)
    print()

#========== Arbitrage Analysis for Calls ==========
    print("==================== Arbitrage Analysis ====================")
    print()
   
    if call_price_diff < 0:
        print("=== Arbitrage Opportunity Detected for Calls ===")
        print(f"- Short the market call at {market_call}")
        print(f"- Long the synthetic call at {synthetic_call}")
        print()
        print(f"  To do so:")
        print(f"  - Buy the put at {parameters['market_put_price']}")
        print(f"  - Buy the stock at {parameters['S_O']}")
        print(f"  - Borrow at a risk-free rate such that pv_K = {parameters['S_K'] * math.exp(-parameters['rf'] * parameters['T'])}")
        print()
        print()
    elif call_price_diff > 0:
        print("=== Arbitrage Opportunity Detected for Calls ===")
        print(f"- Long the market call at {market_call}")
        print(f"- Short the synthetic call at {synthetic_call}")
        print()
        print(f"  To do so:")
        print(f"  - Sell the market put at {parameters['market_put_price']}")
        print(f"  - Short the stock at {parameters['S_O']}")
        print(f"  - Invest in a risk-free bond such that pv_K = {parameters['S_K'] * math.exp(-parameters['rf'] * parameters['T'])}")
        print()
        print()

    else:
       print("No Arbitrage Opportunity for Calls: Synthetic and market option prices are in equilibrium.")
       print()
       print()

#========= Arbitrage Analysis For Puts =========
    if put_price_diff < 0:
        print("====Arbitrage Opportunity Detected for Puts===")
        print(f"- Short the market put at {market_put}")
        print(f"- Long the synthetic put at {synthetic_put}") 
        print()
        print(f"  To do so :")
        print(f"  - Buy the call at {parameters['market_call_price']}")
        print(f"  - Short the stock at {parameters['S_O']}")
        print(f"  - Invest in a risk-free bond such that pv_K = {parameters['S_K'] * math.exp(-parameters['rf'] * parameters['T'])}")
    elif put_price_diff > 0:
        print("===Arbitrage Opportunity Detected for Puts===")
        print(f"- Buy the market put at {market_put}")
        print(f"- Short the synthetic put at {synthetic_put}")
        print()
        print(f"  To do so :")
        print(f"  - Sell the market call at {parameters['market_call_price']}")
        print(f"  - Buy the stock at {parameters['S_O']}")
        print(f"  - Borrow at a risk-free rate such that pv_K = {parameters['S_K'] * math.exp(-parameters['rf'] * parameters['T'])}")
    else:
        print("No Arbitrage Opportunity for Puts: Synthetic and market put prices are in equilibrium.")



def main():
    #Ask_for_parameters_to_user 
    parameters = parametersinputs()
    #detects arbitrage and provides rcommndation
    recommend(parameters)

    # Plot payoff comparison
    plot_payoffc(parameters)
    plot_payoffp(parameters)
    # Plot synthetic option components
    synthetic_call = calculate_synthetic_call(parameters)
    synthetic_put = calculate_synthetic_put(parameters)
    plot_synthetic_call_components(parameters, synthetic_call)
    plot_synthetic_put_components(parameters, synthetic_put)

    
if __name__ == "__main__":
    main()
