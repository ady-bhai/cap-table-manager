import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize the app
st.set_page_config(page_title="Cap Table Manager", layout="wide")
st.title("Cap Table Manager")

# Placeholder for data (use a database or persistent storage in production)
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame({
        "Name": ["Founder A", "Investor B"],
        "Share Class": ["Common", "Preferred"],
        "Shares": [1000, 500],
        "Ownership %": [66.67, 33.33],
    })

if "timeline" not in st.session_state:
    st.session_state["timeline"] = []

# Function to update ownership percentages
def update_ownership(data):
    total_shares = data["Shares"].sum()
    data["Ownership %"] = (data["Shares"] / total_shares * 100).round(2)
    return data

# Function to log timeline events
def log_event(event):
    st.session_state["timeline"].append(event)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Add Stakeholder", "Simulate Funding Round", "Convertible Notes & SAFEs", "Employee Equity", "Timeline", "Export Cap Table"])

# Dashboard Page
if page == "Dashboard":
    st.header("Ownership Overview")

    # Display data table
    data = st.session_state["data"]
    st.dataframe(data, use_container_width=True)

    # Visualization
    st.subheader("Equity Distribution")
    fig, ax = plt.subplots()
    ax.pie(data["Ownership %"], labels=data["Name"], autopct="%1.1f%%")
    st.pyplot(fig)

# Add Stakeholder Page
elif page == "Add Stakeholder":
    st.header("Add New Stakeholder")
    
    # Input Form
    with st.form("add_stakeholder"):
        name = st.text_input("Name")
        share_class = st.selectbox("Share Class", ["Common", "Preferred"])
        shares = st.number_input("Shares", min_value=1)
        submit = st.form_submit_button("Add Stakeholder")

    if submit:
        new_row = {"Name": name, "Share Class": share_class, "Shares": shares, "Ownership %": 0}
        data = st.session_state["data"]
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
        data = update_ownership(data)
        st.session_state["data"] = data
        log_event(f"Added stakeholder {name} with {shares} shares in {share_class} class.")
        st.success(f"Added {name} with {shares} shares in {share_class} class.")

# Simulate Funding Round Page
elif page == "Simulate Funding Round":
    st.header("Simulate a Funding Round")

    # Inputs for simulation
    with st.form("funding_round"):
        new_investor = st.text_input("New Investor Name")
        new_shares = st.number_input("Shares Issued", min_value=1)
        submit = st.form_submit_button("Simulate")

    if submit:
        new_row = {"Name": new_investor, "Share Class": "Preferred", "Shares": new_shares, "Ownership %": 0}
        data = st.session_state["data"]
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
        data = update_ownership(data)
        st.session_state["data"] = data
        log_event(f"Issued {new_shares} new shares to {new_investor} in a funding round.")
        st.success(f"Simulated {new_shares} new shares issued to {new_investor}.")

    # Display updated cap table
    data = st.session_state["data"]
    st.subheader("Updated Cap Table")
    st.dataframe(data, use_container_width=True)

    # Visualization
    st.subheader("Updated Equity Distribution")
    fig, ax = plt.subplots()
    ax.pie(data["Ownership %"], labels=data["Name"], autopct="%1.1f%%")
    st.pyplot(fig)

# Convertible Notes & SAFEs Page
elif page == "Convertible Notes & SAFEs":
    st.header("Manage Convertible Notes & SAFEs")

    # Input Form
    with st.form("add_safe"):
        name = st.text_input("Investor Name")
        amount = st.number_input("Investment Amount", min_value=1)
        cap = st.number_input("Valuation Cap", min_value=1)
        discount = st.number_input("Discount (%)", min_value=0, max_value=100)
        submit = st.form_submit_button("Add Convertible Note/SAFE")

    if submit:
        log_event(f"Added Convertible Note/SAFE for {name}: Amount=${amount}, Cap=${cap}, Discount={discount}%.")
        st.success(f"Added Convertible Note/SAFE for {name}: Amount=${amount}, Cap=${cap}, Discount={discount}%.")

# Employee Equity Page
elif page == "Employee Equity":
    st.header("Manage Employee Equity Grants")

    # Input Form
    with st.form("add_employee_equity"):
        employee_name = st.text_input("Employee Name")
        granted_shares = st.number_input("Granted Shares", min_value=1)
        vesting_years = st.number_input("Vesting Period (Years)", min_value=1)
        submit = st.form_submit_button("Add Employee Grant")

    if submit:
        log_event(f"Added equity grant for {employee_name}: {granted_shares} shares over {vesting_years} years.")
        st.success(f"Added equity grant for {employee_name}: {granted_shares} shares over {vesting_years} years.")

# Timeline Page
elif page == "Timeline":
    st.header("Timeline of Equity Events")

    # Display the logged timeline
    if st.session_state["timeline"]:
        for event in st.session_state["timeline"]:
            st.write(f"- {event}")
    else:
        st.write("No events logged yet.")

# Export Cap Table Page
elif page == "Export Cap Table":
    st.header("Export Cap Table")

    # Download button for cap table
    data = st.session_state["data"]
    csv = data.to_csv(index=False)
    st.download_button(
        label="Download Cap Table as CSV",
        data=csv,
        file_name="cap_table.csv",
        mime="text/csv",
    )

    st.success("Cap table exported successfully!")
