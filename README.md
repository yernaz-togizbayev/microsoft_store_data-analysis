# 📊 Microsoft Store Data Analysis

This project explores and analyzes a dataset of applications from the **Microsoft Windows Store**.  
Using Python and data analysis libraries, the project focuses on **data cleaning, exploratory analysis, visualization, and answering business-related questions**.

The dataset includes app categories, prices, ratings, number of downloads (people rated), and release dates.

---

## 🧠 Project Goals

- Clean and preprocess raw dataset
- Convert string-based prices to numeric values
- Perform exploratory data analysis (EDA)
- Visualize trends in downloads and pricing
- Answer analytical questions about popularity and revenue patterns

---

## 📂 Files Included

microsoft-store-project.ipynb   # Full Jupyter Notebook  
microsoft_store_project.py      # Script version of the notebook  
msft.csv                        # Dataset (required to run the project)

---

## 🛠 Technologies Used

- Python 3
- pandas
- numpy
- matplotlib
- seaborn
- Jupyter Notebook

---

## 🔎 Data Preparation & Cleaning

Key preprocessing steps:

- Removed empty/NaN rows
- Converted "Free" prices to 0
- Converted price strings (INR) to numeric values (EUR conversion)
- Renamed columns for easier access
- Converted `Price` column to numeric type
- Extracted:
  - year
  - month
  - day
  - weekday

---

## 📈 Exploratory Data Analysis

### 📌 Most Popular Category
Bar chart analysis shows which category appears most frequently.

Result: **Music** is the most frequent category in the dataset.

---

### 💰 Most Expensive Category
Pie chart of total category prices.

Result: **Developer Tools** accounts for the highest total price share.

---

### 📆 Most Active Download Year
Line plot analysis of downloads per year.

Result: Downloads peaked in **2016**, followed by a decline.

---

### 📅 Most Active Download Day
Bar plot of downloads by weekday.

Result: **Monday** has the highest download activity.

---

## ❓ Questions Answered

### 1️⃣ Most Popular & Unpopular Apps
Sorted by:
- Rating (primary)
- Number of people rated (secondary)

---

### 2️⃣ Top 10 Most Expensive Apps
Identified using both:
- `sort_values()`
- `groupby()` + sorting

---

### 3️⃣ When Did the Most Downloads Occur?
Grouped by:
- Year
- Month
- Day
- Weekday

Highest single-day download: **30 January 2018**

---

### 4️⃣ Most Downloaded Category
Grouped by category and summed total ratings.

Music category dominates downloads.

---

### 5️⃣ Total & Average Downloads

- Total downloads: ~2.9 million
- Average downloads per day: ~731

---

## 🚀 How to Run

### Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn
```

### Run notebook:

```bash
jupyter notebook microsoft-store-project.ipynb
```

or run script:

```bash
python microsoft_store_project.py
```

---

## 🎯 Learning Outcomes

- Data cleaning & preprocessing
- Handling mixed-type columns
- Exploratory Data Analysis (EDA)
- Grouping & aggregation with pandas
- Data visualization best practices
- Business-oriented data questioning

---

## 📚 Acknowledgements

This project was completed as part of the online course "Data Analysis with Python: Zero to Pandas" by Jovian.

- Dataset: Kaggle (Windows Store dataset)


