# 🗄️ MySQL Operations Dashboard

> A Python-powered web application built with Streamlit that enables non-technical users to perform advanced database operations on a MySQL backend — no SQL knowledge required.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

---
<div style="display: flex; gap: 20px; ">
  <div style="flex: 1; min-width: 45%;">
    <img src="dash-1.png" alt="MySQL Operations Dashboard - View 1" style="width: 40%; border-radius: 8px;">
    
  </div>
  <div style="flex: 1; min-width: 45%;">
    <img src="dash-2.png" alt="MySQL Operations Dashboard - View 2" style="width: 40%; border-radius: 8px;">
  </div>
</div>

<p align="center">
  <img src="dash-1.png" alt="Main Dashboard" width="48%" style="border-radius: 8px;">
  <img src="dash-2.png" alt="Another View" width="48%" style="border-radius: 8px; margin-left: 15px;">
</p>



## 📌 Overview

This project simulates a **real-world business operations system** where managers, team leads, and non-technical staff can interact with a MySQL database through a clean, intuitive web interface.

It combines **advanced SQL concepts** (stored procedures, views, functions, triggers) with a **Python Streamlit frontend** — demonstrating full-stack thinking and enterprise-level database design.

---

## 🚀 Features

- 📊 **View & Filter Data** — Browse tables and database views (product lists, order history, inventory levels)
- ⚙️ **Run Stored Procedures** — Execute business operations like *"Mark order as received"* or *"Update stock"* with a single button click
- ➕ **Add / Update Records** — Insert new products, prices, or orders via forms — no SQL needed
- 🧮 **Business Calculations** — Use database functions to check restocking needs, calculate totals, and more
- 📈 **Live Results** — All changes reflect instantly on screen

---

## 🏗️ Project Structure

```
MySQL-Operations-Dashboard-Streamlit/
│
├── app.py                  # Main Streamlit application
├── db_connection.py        # MySQL connection handler
├── requirements.txt        # Python dependencies
│
├── sql/
│   ├── schema.sql          # Database tables & relationships
│   ├── views.sql           # SQL Views for reports
│   ├── procedures.sql      # Stored Procedures
│   └── functions.sql       # SQL Functions
│
└── README.md
```

---

## 🗃️ Database Design

The MySQL database is structured to reflect a real business backend:

| Object | Purpose |
|---|---|
| **Tables** | Products, Orders, Shipments, Inventory |
| **Views** | Product history, Sales summaries, Stock reports |
| **Stored Procedures** | Receive orders, Update inventory, Process shipments |
| **Functions** | Check restock thresholds, Calculate totals |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Python, Streamlit |
| Backend | MySQL, MySQL Workbench |
| Connector | mysql-connector-python |
| Language | Python 3.10+ |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- MySQL Server + MySQL Workbench
- pip

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/your-username/MySQL-Operations-Dashboard-Streamlit.git
cd MySQL-Operations-Dashboard-Streamlit
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up the database**

Open MySQL Workbench and run the SQL files in order:
```
sql/schema.sql
sql/views.sql
sql/procedures.sql
sql/functions.sql
```

**4. Configure connection**

In `db_connection.py`, update your credentials:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="operations_db"
)
```

**5. Run the app**
```bash
streamlit run app.py
```

---

## 📚 Skills Demonstrated

- ✅ Advanced SQL — Stored Procedures, Views, Functions
- ✅ MySQL database design and normalization
- ✅ Python + MySQL integration using `mysql-connector-python`
- ✅ Real-time web UI development with Streamlit
- ✅ End-to-end full-stack application architecture
- ✅ Simulating real-world business operations systems

---

## 🙋‍♂️ Mohd Farhan Abbas 
      - Currently Interning as Developer Relations (DevRel) @ Y Combinator (YC)
      - Passionate about building real-world applications that bridge the gap
      between complex backend systems and simple, usable interfaces.
      - This project reflects my interest in database engineering, Python
      development, and creating tools that non-technical users can actually use.

- GitHub: [@mohdabbasfarhan](https://github.com/URBANHUNTER107)
- LinkedIn: [Mohd Farhan Abbas](www.linkedin.com/in/mohd-farhan-abbas-704a2b2a8)

---

