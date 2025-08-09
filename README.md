# Indian-Startup-Funding-Analysis
Here’s a README file based on your `main.py` script:

---

# Startup Funding Analysis

This project analyzes a dataset of startup funding to uncover trends, top sectors, cities, and startups receiving investments. It also visualizes the results for better insights.

## 📂 Dataset

The script uses a CSV file named `startup_funding.csv` that contains the following relevant columns:

* **Date dd/mm/yyyy** – Date of funding
* **Amount in USD** – Funding amount (USD)
* **Industry Vertical** – Sector of the startup
* **City  Location** – Location of the startup
* **Startup Name** – Name of the startup
* **Investment Type** – Type of investment (e.g., Seed, Series A, etc.)

## ⚙️ Requirements

Install the required Python packages before running the script:

```bash
pip install pandas matplotlib seaborn
```

## ▶️ How to Run

1. Place the `startup_funding.csv` file in the correct path (default: `/content/startup_funding.csv`).
2. Run the Python script:

```bash
python main.py
```

## 📊 Features & Visualizations

The script performs:

1. **Data Cleaning**

   * Converts date strings to datetime format.
   * Cleans and converts funding amounts to numeric values.
2. **Analysis**

   * Calculates total funding trends over time.
   * Finds top 5 sectors by number of startups.
   * Finds top 5 cities by funding amount.
   * Finds top 5 startups by funding amount.
3. **Visualizations**

   * Funding trend over time (Line chart)
   * Top 5 sectors (Bar chart)
   * Top 5 cities (Bar chart)
   * Top 5 startups (Bar chart)
   * Distribution of investment types (Bar chart)

## 📌 Note

* The variable `investment_type_distribution` is referenced but **not defined** in the script. You will need to calculate it, for example:

```python
investment_type_distribution = df['Investment Type'].value_counts()
```

before plotting.

## 📷 Example Output

* **Line chart**: Shows funding trend over time.
* **Bar charts**: Display top sectors, cities, startups, and investment types.

-
