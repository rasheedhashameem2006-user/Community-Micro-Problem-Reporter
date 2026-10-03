import streamlit as st
import pandas as pd

from database import create_database, get_all_reports


# ==========================================
# CREATE DATABASE
# ==========================================

create_database()


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("📊 Community Micro Problem Reporter")

st.header("🛠️ Admin Dashboard")

st.write(
    "View, analyze, search and filter community problem reports."
)


# ==========================================
# GET REPORTS
# ==========================================

reports = get_all_reports()


# ==========================================
# NO REPORTS
# ==========================================

if not reports:

    st.info(
        "📭 No reports are currently available."
    )


# ==========================================
# REPORT DATA AVAILABLE
# ==========================================

else:

    data = []

    for report in reports:

        data.append({

            "Report ID": report[0],

            "Problem": report[1],

            "Confidence": report[2],

            "Department": report[3],

            "Priority": report[4],

            "Severity": report[5],

            "Location": report[6],

            "Description": report[7],

            "Status": report[8]

        })


    df = pd.DataFrame(data)


    # ======================================
    # REPORT STATISTICS
    # ======================================

    st.subheader("📈 Report Statistics")


    total_reports = len(df)


    high_priority = len(
        df[df["Priority"] == "High"]
    )


    high_severity = len(
        df[df["Severity"] == "High"]
    )


    under_review = len(
        df[df["Status"] == "Under Review"]
    )


    resolved = len(
        df[df["Status"] == "Resolved"]
    )


    # ======================================
    # STATISTICS CARDS
    # ======================================

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:

        st.metric(
            "📋 Total Reports",
            total_reports
        )


    with col2:

        st.metric(
            "🔴 High Severity",
            high_severity
        )


    with col3:

        st.metric(
            "🚨 High Priority",
            high_priority
        )


    with col4:

        st.metric(
            "🟡 Under Review",
            under_review
        )


    with col5:

        st.metric(
            "🟢 Resolved",
            resolved
        )


    # ======================================
    # SEVERITY SUMMARY
    # ======================================

    st.subheader("🚨 Severity Summary")


    severity_counts = (
        df["Severity"]
        .value_counts()
        .rename("Reports")
    )


    col1, col2, col3 = st.columns(3)


    high_count = int(
        severity_counts.get("High", 0)
    )

    medium_count = int(
        severity_counts.get("Medium", 0)
    )

    low_count = int(
        severity_counts.get("Low", 0)
    )


    with col1:

        st.error(
            f"🔴 High Severity: {high_count}"
        )


    with col2:

        st.warning(
            f"🟡 Medium Severity: {medium_count}"
        )


    with col3:

        st.success(
            f"🟢 Low Severity: {low_count}"
        )


    # ======================================
    # CHARTS
    # ======================================

    st.subheader("📊 Report Charts")


    # --------------------------------------
    # PROBLEM-WISE
    # --------------------------------------

    st.write("### 🔎 Problem-wise Reports")


    problem_counts = (
        df["Problem"]
        .value_counts()
        .rename("Reports")
    )


    st.bar_chart(
        problem_counts
    )


    # --------------------------------------
    # DEPARTMENT-WISE
    # --------------------------------------

    st.write("### 🏢 Department-wise Reports")


    department_counts = (
        df["Department"]
        .value_counts()
        .rename("Reports")
    )


    st.bar_chart(
        department_counts
    )


    # --------------------------------------
    # SEVERITY-WISE
    # --------------------------------------

    st.write("### 🚨 Severity-wise Reports")


    severity_chart = (
        df["Severity"]
        .value_counts()
        .rename("Reports")
    )


    st.bar_chart(
        severity_chart
    )


    # --------------------------------------
    # STATUS-WISE
    # --------------------------------------

    st.write("### 📌 Report Status")


    status_counts = (
        df["Status"]
        .value_counts()
        .rename("Reports")
    )


    st.bar_chart(
        status_counts
    )


    # ======================================
    # SEARCH AND FILTER
    # ======================================

    st.subheader("🔎 Search & Filter Reports")


    # --------------------------------------
    # SEARCH
    # --------------------------------------

    search_text = st.text_input(
        "🔍 Search",
        placeholder=(
            "Search by Report ID, location "
            "or description..."
        )
    )


    # ======================================
    # FILTER COLUMNS
    # ======================================

    col1, col2, col3, col4, col5 = st.columns(5)


    # --------------------------------------
    # PROBLEM FILTER
    # --------------------------------------

    with col1:

        problem_options = (
            ["All"]
            + sorted(
                df["Problem"]
                .dropna()
                .unique()
                .tolist()
            )
        )


        selected_problem = st.selectbox(
            "🏷️ Problem",
            problem_options
        )


    # --------------------------------------
    # DEPARTMENT FILTER
    # --------------------------------------

    with col2:

        department_options = (
            ["All"]
            + sorted(
                df["Department"]
                .dropna()
                .unique()
                .tolist()
            )
        )


        selected_department = st.selectbox(
            "🏢 Department",
            department_options
        )


    # --------------------------------------
    # PRIORITY FILTER
    # --------------------------------------

    with col3:

        priority_options = (
            ["All"]
            + sorted(
                df["Priority"]
                .dropna()
                .unique()
                .tolist()
            )
        )


        selected_priority = st.selectbox(
            "🚦 Priority",
            priority_options
        )


    # --------------------------------------
    # SEVERITY FILTER
    # --------------------------------------

    with col4:

        severity_options = (
            ["All"]
            + sorted(
                df["Severity"]
                .dropna()
                .unique()
                .tolist()
            )
        )


        selected_severity = st.selectbox(
            "🚨 Severity",
            severity_options
        )


    # --------------------------------------
    # STATUS FILTER
    # --------------------------------------

    with col5:

        status_options = (
            ["All"]
            + sorted(
                df["Status"]
                .dropna()
                .unique()
                .tolist()
            )
        )


        selected_status = st.selectbox(
            "📌 Status",
            status_options
        )


    # ======================================
    # APPLY FILTERS
    # ======================================

    filtered_df = df.copy()


    # --------------------------------------
    # SEARCH FILTER
    # --------------------------------------

    if search_text.strip():

        search_value = (
            search_text
            .strip()
            .lower()
        )


        filtered_df = filtered_df[
            filtered_df.apply(
                lambda row:

                    search_value
                    in str(
                        row["Report ID"]
                    ).lower()

                    or

                    search_value
                    in str(
                        row["Location"]
                    ).lower()

                    or

                    search_value
                    in str(
                        row["Description"]
                    ).lower(),

                axis=1
            )
        ]


    # --------------------------------------
    # PROBLEM FILTER
    # --------------------------------------

    if selected_problem != "All":

        filtered_df = filtered_df[
            filtered_df["Problem"]
            == selected_problem
        ]


    # --------------------------------------
    # DEPARTMENT FILTER
    # --------------------------------------

    if selected_department != "All":

        filtered_df = filtered_df[
            filtered_df["Department"]
            == selected_department
        ]


    # --------------------------------------
    # PRIORITY FILTER
    # --------------------------------------

    if selected_priority != "All":

        filtered_df = filtered_df[
            filtered_df["Priority"]
            == selected_priority
        ]


    # --------------------------------------
    # SEVERITY FILTER
    # --------------------------------------

    if selected_severity != "All":

        filtered_df = filtered_df[
            filtered_df["Severity"]
            == selected_severity
        ]


    # --------------------------------------
    # STATUS FILTER
    # --------------------------------------

    if selected_status != "All":

        filtered_df = filtered_df[
            filtered_df["Status"]
            == selected_status
        ]


    # ======================================
    # FILTER RESULT COUNT
    # ======================================

    st.write(
        f"**Showing {len(filtered_df)} "
        f"of {len(df)} report(s)**"
    )


    # ======================================
    # DISPLAY REPORTS
    # ======================================

    if not filtered_df.empty:

        display_df = filtered_df.copy()


        # Convert confidence to percentage
        display_df["Confidence"] = (
            display_df["Confidence"] * 100
        ).round(2).astype(str) + "%"


        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )


    else:

        st.warning(
            "🔍 No reports match the selected "
            "search/filter criteria."
        )


# ==========================================
# FOOTER
# ==========================================

st.divider()


st.caption(
    "Community Micro Problem Reporter — "
    "Local Admin Dashboard"
)