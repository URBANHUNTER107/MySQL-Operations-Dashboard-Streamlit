import pandas as pd
import streamlit as st
from db_functions import (
    connect_to_db,
    get_basic_info,
    get_operational_data,
    get_suppliers,
    get_categories,
    add_new_manual_id,
    get_all_products,
    get_product_history,
    place_reorder,
    get_pending_reorders,
    mark_reorder_as_received
)

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


elif option == "Operational Tasks":
    st.header("Operational Tasks")

    selected_task = st.selectbox(
        "Choose a Task",
        [
            "Add New Product",
            "Product History",
            "Place Reorder",
            "Receive Reorder"
        ]
    )
    if selected_task == "Add New Product":
        categories = get_categories(cursor)
        suppliers = get_suppliers(cursor)
        with st.form("Add_Product_Form"):
                
                product_name = st.text_input("Product Name")

                product_category = st.selectbox(
                    "Category",
                    categories
                )

                product_price = st.number_input(
                    "Price",
                    min_value=0.0
                )

                product_stock = st.number_input(
                    "Stock Quantity",
                    min_value=0,
                    step=1
                )

                product_level = st.number_input(
                    "Reorder Level",
                    min_value=0,
                    step=1
                )

                supplier_ids = [s["supplier_id"] for s in suppliers]
                supplier_names = [s["supplier_name"] for s in suppliers]

                supplier_id = st.selectbox(
                    "Supplier",
                    options=supplier_ids,
                    format_func=lambda x: supplier_names[supplier_ids.index(x)]
                )

                submitted = st.form_submit_button("Add Product")
                
                
                if submitted:

                    if not product_name:
                        st.error("Please Enter the Product Name.")

                    else:
                        try:

                            add_new_manual_id(
                                cursor,
                                db,
                                product_name,
                                product_category,
                                product_price,
                                product_stock,
                                product_level,
                                supplier_id
                            )

                            st.success(f"Product {product_name} added successfully!")

                        except Exception as e:
                            st.error(f"Error adding the Product {e}")


    if selected_task == "Product History":

            st.header("Product Inventory History")

            products = get_all_products(cursor)

            product_names = [p["product_name"] for p in products]
            product_ids = [p["product_id"] for p in products]

            selected_product_name = st.selectbox(
                "Select a Product",
                options=product_names
            )

            if selected_product_name:

                selected_product_id = product_ids[
                    product_names.index(selected_product_name)
                ]

                history_data = get_product_history(
                    cursor,
                    selected_product_id
                )

                if history_data:

                    df = pd.DataFrame(history_data)
                    st.dataframe(df)

                else:

                    st.info(
                        "No History found for the product selected"
                    )  
    

    if selected_task == "Place Reorder":
        products = get_all_products(cursor)

        product_names = [p["product_name"] for p in products]
        product_ids = [p["product_id"] for p in products]

        selected_product_name = st.selectbox(
            "Select a Product",
            options=product_names
        )

        reorder_qty = st.number_input(
            "Reorder Quantity",
            min_value=1,
            step=1
        )

        
        if st.button("Place Reorder"):

            if not selected_product_name:
                st.error("Please Select a Product")

            elif reorder_qty <= 0:
                st.error("Reorder Quantity must be greater than 0")

            else:
                selected_product_id = product_ids[
                    product_names.index(selected_product_name)
                ]

                try:
                    place_reorder(
                        cursor,
                        db,
                        selected_product_id,
                        reorder_qty
                    )

                    st.success(
                        f"Order placed for {selected_product_name} "
                        f"with quantity {reorder_qty}"
                    )

                except Exception as e:
                    st.error(f"Error placing reorder: {e}")

    elif selected_task == "Receive Reorder":

            st.header("Receive Reorder")

            pending_reorders = get_pending_reorders(cursor)

            if not pending_reorders:

                st.success("No pending reorders found.")

            else:

                reorder_ids = [
                    row["reorder_id"]
                    for row in pending_reorders
                ]

                reorder_labels = [
                    f"ID {row['reorder_id']} - {row['product_name']}"
                    for row in pending_reorders
                ]

                selected_label = st.selectbox(
                    "Select Reorder",
                    reorder_labels
                )

                selected_reorder_id = reorder_ids[
                    reorder_labels.index(selected_label)
                ]

                if st.button("Mark As Received"):

                    try:

                        mark_reorder_as_received(
                            cursor,
                            db,
                            selected_reorder_id
                        )

                        st.success(
                            f"Reorder {selected_reorder_id} received successfully."
                        )

                    except Exception as e:

                        st.error(str(e))



#py -m streamlit run app.py

