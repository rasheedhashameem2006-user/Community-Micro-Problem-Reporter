import streamlit as st
from ultralytics import YOLO
from PIL import Image
import uuid

from database import (
    create_database,
    save_report,
    find_duplicate_reports
)


# ==========================================
# CREATE DATABASE
# ==========================================

create_database()


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Community Micro Problem Reporter",
    page_icon="🏙️",
    layout="centered"
)


# ==========================================
# LOAD MODEL
# ==========================================

MODEL_PATH = (
    "runs/classify/runs/"
    "community_problem_classifier/"
    "weights/best.pt"
)

model = YOLO(MODEL_PATH)


# ==========================================
# PROBLEM INFORMATION
# ==========================================

DEPARTMENT_INFO = {

    "road": {
        "department": "Roads & Highways",
        "severity": "High",
        "action": "Inspect and repair damaged road"
    },

    "road_not_broken": {
        "department": "Roads & Highways",
        "severity": "Low",
        "action": "No repair required"
    },

    "roadway_flooding": {
        "department": "Municipal / Drainage",
        "severity": "High",
        "action": "Inspect flooding and drainage"
    },

    "garbage_full": {
        "department": "Sanitation",
        "severity": "High",
        "action": "Arrange waste collection"
    },

    "garbage_empty": {
        "department": "Sanitation",
        "severity": "Low",
        "action": "No immediate action"
    },

    "pathole": {
        "department": "Roads & Highways",
        "severity": "High",
        "action": "Repair pothole"
    },

    "normal": {
        "department": "No department required",
        "severity": "Low",
        "action": "No action required"
    }
}


# ==========================================
# AUTOMATIC PRIORITY FUNCTION
# ==========================================

def calculate_priority(severity):

    if severity == "High":

        return "High"

    elif severity == "Medium":

        return "Medium"

    else:

        return "Low"


# ==========================================
# SESSION STATE
# ==========================================

if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False

if "class_name" not in st.session_state:
    st.session_state.class_name = None

if "confidence" not in st.session_state:
    st.session_state.confidence = None

if "report_submitted" not in st.session_state:
    st.session_state.report_submitted = False

if "report_id" not in st.session_state:
    st.session_state.report_id = None

if "duplicate_found" not in st.session_state:
    st.session_state.duplicate_found = False

if "duplicate_reports" not in st.session_state:
    st.session_state.duplicate_reports = []


# ==========================================
# TITLE
# ==========================================

st.title(
    "🏙️ Community Micro Problem Reporter"
)

st.write(
    "Report community problems using "
    "AI-powered image classification."
)


# ==========================================
# IMAGE UPLOAD
# ==========================================

st.subheader("📷 Upload Image")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)


# ==========================================
# AI PREDICTION
# ==========================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )


    if st.button("🔍 Detect Problem"):

        with st.spinner(
            "AI is analyzing the image..."
        ):

            results = model.predict(
                source=image,
                imgsz=224,
                verbose=False
            )

            result = results[0]

            class_id = result.probs.top1

            confidence = (
                result.probs.top1conf.item()
            )

            class_name = result.names[class_id]


        # Store prediction
        st.session_state.class_name = class_name

        st.session_state.confidence = confidence

        st.session_state.prediction_done = True


        # Reset submission
        st.session_state.report_submitted = False

        st.session_state.report_id = None


        # Reset duplicate detection
        st.session_state.duplicate_found = False

        st.session_state.duplicate_reports = []


        st.success(
            "✅ AI prediction completed!"
        )


# ==========================================
# DISPLAY PREDICTION
# ==========================================

if st.session_state.prediction_done:

    class_name = st.session_state.class_name

    confidence = st.session_state.confidence


    info = DEPARTMENT_INFO.get(
        class_name,
        {
            "department": "Unknown",
            "severity": "Unknown",
            "action": "Manual inspection required"
        }
    )


    # ======================================
    # SEVERITY
    # ======================================

    severity = info["severity"]


    # ======================================
    # AUTOMATIC PRIORITY
    # ======================================

    priority = calculate_priority(
        severity
    )


    # ======================================
    # AI RESULT
    # ======================================

    st.subheader("🤖 AI Prediction")


    st.write(
        f"**Problem:** {class_name}"
    )


    st.write(
        f"**Confidence:** "
        f"{confidence * 100:.2f}%"
    )


    # ======================================
    # SEVERITY DISPLAY
    # ======================================

    st.subheader("🚨 Problem Severity")


    if severity == "High":

        st.error(
            "🔴 High Severity"
        )

    elif severity == "Medium":

        st.warning(
            "🟡 Medium Severity"
        )

    else:

        st.success(
            "🟢 Low Severity"
        )


    # ======================================
    # PRIORITY DISPLAY
    # ======================================

    st.subheader("🚦 Report Priority")


    if priority == "High":

        st.error(
            "🔴 High Priority"
        )

    elif priority == "Medium":

        st.warning(
            "🟡 Medium Priority"
        )

    else:

        st.success(
            "🟢 Low Priority"
        )


    # ======================================
    # DEPARTMENT
    # ======================================

    st.subheader(
        "🏢 Responsible Department"
    )


    st.write(
        f"**Department:** "
        f"{info['department']}"
    )


    st.write(
        f"**Recommended Action:** "
        f"{info['action']}"
    )


    # ======================================
    # VERIFY PREDICTION
    # ======================================

    st.subheader(
        "✅ Verify Prediction"
    )


    verification = st.radio(
        "Is this prediction correct?",
        ["Yes", "No"],
        key="verification"
    )


    if verification == "No":

        st.warning(
            "⚠️ Please verify the prediction "
            "before submitting the report."
        )


    # ======================================
    # LOCATION
    # ======================================

    st.subheader(
        "📍 Problem Location"
    )


    location = st.text_input(
        "Enter the location",
        placeholder=(
            "Example: Gandhipuram, Coimbatore"
        ),
        key="location"
    )


    # ======================================
    # DESCRIPTION
    # ======================================

    st.subheader(
        "📝 Problem Description"
    )


    description = st.text_area(
        "Describe the problem",
        placeholder=(
            "Example: Large pothole near the "
            "main road causing difficulty "
            "for vehicles."
        ),
        key="description"
    )


    # ======================================
    # SUBMIT REPORT
    # ======================================

    st.subheader(
        "📨 Submit Report"
    )


    if st.button(
        "Submit Report",
        type="primary"
    ):


        # ----------------------------------
        # VALIDATION
        # ----------------------------------

        if verification == "No":

            st.error(
                "❌ Please confirm that the "
                "prediction is correct."
            )


        elif not location.strip():

            st.error(
                "❌ Please enter the problem location."
            )


        elif not description.strip():

            st.error(
                "❌ Please enter a problem description."
            )


        else:


            # ----------------------------------
            # DUPLICATE CHECK
            # ----------------------------------

            duplicates = find_duplicate_reports(

                problem=class_name,

                location=location

            )


            if duplicates:

                st.session_state.duplicate_found = True

                st.session_state.duplicate_reports = duplicates


            else:

                st.session_state.duplicate_found = False

                st.session_state.duplicate_reports = []


                # ----------------------------------
                # CREATE REPORT ID
                # ----------------------------------

                report_id = (

                    "RPT-"

                    + str(uuid.uuid4())[:8].upper()

                )


                try:


                    # ----------------------------------
                    # SAVE REPORT
                    # ----------------------------------

                    save_report(

                        report_id=report_id,

                        problem=class_name,

                        confidence=confidence,

                        department=info["department"],

                        priority=priority,

                        severity=severity,

                        location=location,

                        description=description

                    )


                    st.session_state.report_id = report_id

                    st.session_state.report_submitted = True


                    st.success(
                        "✅ Report submitted and saved "
                        "successfully!"
                    )


                except Exception as e:

                    st.error(
                        f"❌ Failed to save report: {e}"
                    )


# ==========================================
# DUPLICATE REPORT WARNING
# ==========================================

if st.session_state.duplicate_found:

    st.warning(
        "⚠️ A similar report already exists "
        "for this problem and location."
    )


    st.write(
        "Existing report(s):"
    )


    # --------------------------------------
    # SHOW EXISTING REPORTS
    # --------------------------------------

    for duplicate in (
        st.session_state.duplicate_reports
    ):

        st.write(
            f"**Report ID:** {duplicate[0]}"
        )

        st.write(
            f"**Problem:** {duplicate[1]}"
        )

        st.write(
            f"**Location:** {duplicate[2]}"
        )

        st.write(
            f"**Status:** {duplicate[3]}"
        )

        st.divider()


    # --------------------------------------
    # DUPLICATE CONFIRMATION
    # --------------------------------------

    submit_duplicate = st.checkbox(

        "I still want to submit this report.",

        key="submit_duplicate"

    )


    if st.button(
        "Submit Anyway"
    ):


        if submit_duplicate:

            class_name = (
                st.session_state.class_name
            )

            confidence = (
                st.session_state.confidence
            )


            info = DEPARTMENT_INFO.get(

                class_name,

                {
                    "department": "Unknown",
                    "severity": "Unknown",
                    "action": (
                        "Manual inspection required"
                    )
                }

            )


            severity = info["severity"]


            priority = calculate_priority(
                severity
            )


            location = (
                st.session_state.location
            )


            description = (
                st.session_state.description
            )


            # ----------------------------------
            # CREATE REPORT ID
            # ----------------------------------

            report_id = (

                "RPT-"

                + str(uuid.uuid4())[:8].upper()

            )


            try:


                save_report(

                    report_id=report_id,

                    problem=class_name,

                    confidence=confidence,

                    department=info["department"],

                    priority=priority,

                    severity=severity,

                    location=location,

                    description=description

                )


                st.session_state.report_id = report_id

                st.session_state.report_submitted = True

                st.session_state.duplicate_found = False


                st.success(
                    "✅ Report submitted successfully!"
                )


            except Exception as e:

                st.error(
                    f"❌ Failed to save report: {e}"
                )


        else:

            st.info(
                "Please tick the checkbox if you "
                "still want to submit this report."
            )


# ==========================================
# DISPLAY SUBMITTED REPORT
# ==========================================

if st.session_state.report_submitted:


    class_name = (
        st.session_state.class_name
    )


    confidence = (
        st.session_state.confidence
    )


    info = DEPARTMENT_INFO.get(

        class_name,

        {
            "department": "Unknown",
            "severity": "Unknown",
            "action": (
                "Manual inspection required"
            )
        }

    )


    severity = info["severity"]


    priority = calculate_priority(
        severity
    )


    st.divider()


    st.subheader(
        "📄 Submitted Report"
    )


    st.write(
        f"**Report ID:** "
        f"{st.session_state.report_id}"
    )


    st.write(
        f"**Problem:** "
        f"{class_name}"
    )


    st.write(
        f"**Confidence:** "
        f"{confidence * 100:.2f}%"
    )


    st.write(
        f"**Severity:** "
        f"{severity}"
    )


    st.write(
        f"**Priority:** "
        f"{priority}"
    )


    st.write(
        f"**Department:** "
        f"{info['department']}"
    )


    st.write(
        f"**Recommended Action:** "
        f"{info['action']}"
    )


    st.write(
        f"**Location:** "
        f"{st.session_state.location}"
    )


    st.write(
        f"**Description:** "
        f"{st.session_state.description}"
    )


    st.write(
        "**Status:** Submitted"
    )


    st.success(

        f"Your Report ID is "

        f"{st.session_state.report_id}"

    )