"""
Helper functions for Bass Diffusion Model estimation and forecasting.
"""
import numpy as np

def estimate_bass_params(sales_series):
    """Estimates p, q, and M from a sales time series using discrete OLS."""
    cum_sales = np.cumsum(sales_series)
    y_lag = np.roll(cum_sales, 1)
    y_lag[0] = 0
    
    X = np.column_stack([np.ones_like(y_lag), y_lag, y_lag**2])
    a, b, c = np.linalg.lstsq(X, sales_series, rcond=None)[0]
    
    M = (-b - np.sqrt(b**2 - 4*a*c)) / (2 * c)
    p = a / M
    q = b + p
    return p, q, M

def bass_forecast(t, p, q, M):
    """Calculates non-cumulative annual adopters n(t)."""
    exp_term = np.exp(-(p + q) * t)
    return M * (((p + q)**2) / p) * exp_term / ((1 + (q / p) * exp_term)**2)

def bass_cumulative(t, p, q, M):
    """Calculates cumulative adopters N(t)."""
    exp_term = np.exp(-(p + q) * t)
    return M * (1 - exp_term) / (1 + (q / p) * exp_term)
