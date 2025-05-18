
# Physics Data Analysis Challenge

This project is a complete data analysis workflow based on real-world physics experiment data (motion of a cart).  
It showcases essential skills in data wrangling, visualization, and scientific reasoning using Python.

---

## 🔍 Dataset

The dataset `cart_flat.csv` includes readings from a physics lab experiment:
- Time (s)
- Velocity (m/s)
- Acceleration (m/s²)
- Force (N)
- Angular velocity components
- Position (m)

---

## ✅ What I Did

### 1. Data Cleaning
- Handled missing values using mean imputation.
- Detected and interpreted anomalies in physical readings (outliers like negative force).
- Removed irrelevant or zeroed-out columns (e.g., constant angular velocity).

### 2. Feature Engineering
- Calculated **Kinetic Energy** using the formula:  
  \( E_k = \frac{1}{2}mv^2 \), assuming mass = 1 kg.

### 3. Visualization & Interpretation
- **Force vs Acceleration** → clear linear relation reflecting Newton's second law (F = ma).
- **Velocity vs Time** → revealed changes in direction and motion phases.
- **Kinetic Energy vs Time/Velocity** → explored motion energy dynamics.

---

## 📊 Sample Visualizations

- Scatter plots, line charts, and energy curves were generated using `matplotlib` and `seaborn`.
- Heatmap and correlation matrix can be added to extend the analysis.

---

## 🧠 Key Insights

- Physics laws like Newton's 2nd law appear clearly in the data.
- Acceleration patterns matched expected motion behavior.
- Cleaned data helped uncover precise physical interpretations.

---

## ⚙️ Tools Used

- Python
- Pandas
- Seaborn
- Matplotlib

---

## ▶️ How to Run

1. Clone the repository
2. Add the file `cart_flat.csv` to the working directory.
3. Run `physics_analysis_project.py` using Python 3.

---

## 🧾 License

This project is open for learning purposes and experimentation.

---

Made with curiosity and science!
