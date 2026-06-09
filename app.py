import pandas as pd
import streamlit as st
from db_functions import connect_to_db, get_basic_info, get_operational_data    

# Sidebar
st.sidebar.title("Inventory Management Dashboard")

option = st.sidebar.radio(
    "Select Option",
    ["Basic Information", "Operational Tasks"]
)


# Main Space
st.title("Inventory and Supply Chain Dashboard")

db = connect_to_db()
cursor = db.cursor(dictionary=True)

# ---------------- BASIC INFORMATION PAGE ----------------

if option == "Basic Information":

    st.header("Basic Metrics")

    # Get data from database
    basic_info = get_basic_info(cursor)

    # Display metrics
    cols = st.columns(3)

    keys = list(basic_info.keys())

    for i in range(len(keys)):
        cols[i % 3].metric(
            label=keys[i],
            value=basic_info[keys[i]]
        )

    st.divider()

    operational_data = get_operational_data(cursor)

    for title, data in operational_data.items():

        st.subheader(title)

        df = pd.DataFrame(data)

        st.dataframe(df, use_container_width=True)



#py -m streamlit run app.py

