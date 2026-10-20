import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helper_functions import estimate_bass_params, bass_forecast, bass_cumulative

# 1. Load historical look-alike sales data
df = pd.read_csv('data/lookalike_sales_data.csv')

# 2. Estimate Bass parameters
p_est, q_est, M_hist = estimate_bass_params(df['Sales'].values)

print("--- Bass Model Parameters ---")
print(f"p (Innovation Coefficient): {p_est:.6f}")
print(f"q (Imitation Coefficient):  {q_est:.6f}")
print(f"M (Historical Ceiling):     {M_hist:.2f}M units")

# 3. Forecast Figure 03 Household Robotics (Global Scope: M_target = 50M units via Fermi estimation)
M_target = 50.0  
periods = np.arange(1, 16)

annual_adopters = bass_forecast(periods, p_est, q_est, M_target)
cum_adopters = bass_cumulative(periods, p_est, q_est, M_target)

# Export adoption table
forecast_df = pd.DataFrame({
    'Period_Year': periods,
    'Annual_Adopters_Millions': annual_adopters,
    'Cumulative_Adopters_Millions': cum_adopters
})
forecast_df.to_csv('data/predicted_diffusion.csv', index=False)

# 4. Generate Plot
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Years Since Commercial Launch')
ax1.set_ylabel('Annual New Adopters n(t) [Millions]', color=color)
ax1.bar(periods, annual_adopters, color=color, alpha=0.6, label='Annual Adopters')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Cumulative Adopters N(t) [Millions]', color=color)
ax2.plot(periods, cum_adopters, color=color, linewidth=2.5, label='Cumulative Adopters')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Bass Diffusion Forecast: Figure 03 Household Robotics')
fig.tight_layout()
plt.savefig('img/image1.png', dpi=300)
print("Execution complete. Output saved to data/predicted_diffusion.csv and img/image1.png")
