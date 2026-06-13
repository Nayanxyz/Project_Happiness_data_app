# 🌍 Happiness Data Explorer

An interactive web application built with Streamlit and Plotly that allows users to visualize and analyze the correlations between a country's GDP, Generosity, and overall Happiness score.

## ✨ Features

- **Dynamic Data Visualization:** Instantly generate scatter plots based on user-selected metrics.
- **Interactive Controls:** Toggle between GDP, Happiness, and Generosity for both X and Y axes to discover hidden trends.
- **Clean UI:** A minimalist, fast-loading interface powered by Streamlit.

## 🛠️ Tech Stack

- **Python 3.10+** (Required for `match-case` syntax)
- **Streamlit:** For the frontend web framework.
- **Pandas:** For data manipulation and CSV parsing.
- **Plotly Express:** For rendering interactive charts.

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nayanxyz/Project_Happiness_data_app.git
   cd Project_Happiness_data_app
   ```
2. **Install dependencies:**
Ensure you have the required libraries installed. You can install them via pip:

```Bash
pip install streamlit pandas plotly
```

3. **Add the dataset:**
Ensure the data file happy.csv is located in the root directory of the project. (Note: The dataset must contain columns exactly named gdp, happiness, and generosity.)

4. **Run the application:**

```Bash
streamlit run main.py
```
