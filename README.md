# 🍔 Food Delivery Data Analysis & Machine Learning

This repository contains a **real-world data integration and analytics project** simulating a food delivery system.  
It demonstrates data preprocessing, merging multiple sources, exploratory analysis, and machine learning for business insights.

---

## 📂 Project Files

| File | Description |
|------|-------------|
| `orders.csv` | Transactional order data (order ID, user ID, restaurant ID, date, amount, city) |
| `users.json` | User master data (user ID, name, membership type, signup date) |
| `restaurants.sql` | Restaurant master data (restaurant ID, name, cuisine, rating) |
| `final_food_delivery_dataset.csv` | Merged dataset containing orders, user, and restaurant information |
| `analysis.ipynb` | Python notebook for data analysis, visualizations, and ML models |

---

## 🚀 Project Steps

### 1️⃣ Load Data
- Load `orders.csv` using Pandas
- Load `users.json` using Pandas
- Load `restaurants.sql` into SQLite

### 2️⃣ Merge Data
- Perform **Left Joins**:
  - `orders.user_id → users.user_id`
  - `orders.restaurant_id → restaurants.restaurant_id`
- Result: `final_food_delivery_dataset.csv`

### 3️⃣ Data Analysis
- Order trends over time
- User behavior patterns
- City-wise and cuisine-wise performance
- Membership impact (Gold vs Regular)
- Revenue distribution and seasonality

### 4️⃣ Machine Learning
- **Regression:** Predict order amount
- **Classification:** Predict Gold vs Regular members
- Models used: Random Forest, XGBoost (optional)
- Features include: `membership_type`, `cuisine`, `city`, `rating`, `order_month`

---

## 📊 Example Insights

- Identify **highest revenue cities**
- Analyze **cuisine popularity and average order values**
- Detect **high-value users**
- Evaluate **restaurant performance by rating**
- Determine **seasonal revenue trends**

---

## 🛠 Technology Stack

- **Python**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **SQL**: SQLite (for restaurant master data)
- **CSV / JSON**: For transactional and user data
- **Google colab /Jupyter Notebook**: For analysis and ML


