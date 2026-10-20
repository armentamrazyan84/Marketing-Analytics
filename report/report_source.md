# Innovation Diffusion Analysis: TIME 2025 Robotics

**Author:** Homework Submission  
**Course Assignment:** Bass Diffusion Model Analysis  

---

## 1. Selected Innovation
* **Innovation:** Figure 03 Household Humanoid Robot (Robotics Category)[cite: 5]
* **TIME 2025 Link:** https://time.com/collections/best-inventions-2025/7318507/figure-03/[cite: 5]

## 2. Historical Look-Alike Innovation & Justification
* **Look-Alike Innovation:** Consumer Robotic Vacuum Cleaners (iRobot Roomba)[cite: 5]

### Comparison & Justification
The adoption trajectory of modern household humanoids (such as Figure 03) closely mirrors early consumer robotic vacuums[cite: 5]. Functionally, both categories shift households from manual human labor to autonomous physical task execution[cite: 5]. Technologically, both depend on onboard spatial sensors (LiDAR, computer vision) and hardware unit-cost reductions before achieving broad market adoption[cite: 5]. Economically, both faced early high hardware costs and consumer skepticism regarding daily utility[cite: 5].

## 3. Data Source
* **Historical Reference:** Statista Research / iRobot Historical Unit Sales Data (2005–2020)[cite: 5].

## 4. Estimated Bass Model Parameters
Using discrete OLS regression on historical time series data[cite: 5]:
* **Coefficient of Innovation ($p$):** 0.006426[cite: 5]
* **Coefficient of Imitation ($q$):** 0.323217[cite: 5]
* **Historical Market Capacity ($M_{hist}$):** 147.08 Million units[cite: 5]

## 5. Scope Selection & Justification
* **Selected Scope:** Global Market[cite: 5]
* **Justification:** Humanoid robotics platforms require substantial R&D and capital expenditures, making international markets essential from launch[cite: 5].

## 6. Fermi Estimation for Target Market Potential ($M$)
To derive the global market capacity ($M$) for household humanoids[cite: 5]:
1. Total middle/high-income global households = $500,000,000$[cite: 5]
2. Addressable target adoption tier ($20\%$) = $100,000,000$ households[cite: 5]
3. Estimated 15-year penetration limit ($50\%$) = $100,000,000 \times 0.50 = \mathbf{50,000,000\text{ units}}$ ($M$)[cite: 5].

## 7. Diffusion Predictions
The predicted 15-year adoption path is plotted below and exported to `data/predicted_diffusion.csv`[cite: 5].
