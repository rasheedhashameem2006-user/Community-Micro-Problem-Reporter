import sqlite3


# ==========================================
# DATABASE NAME
# ==========================================

DATABASE_NAME = "community_reports.db"


# ==========================================
# CREATE / UPDATE DATABASE
# ==========================================

def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    # Create table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            report_id TEXT UNIQUE NOT NULL,

            problem TEXT NOT NULL,

            confidence REAL,

            department TEXT,

            priority TEXT,

            severity TEXT,

            location TEXT NOT NULL,

            description TEXT NOT NULL,

            status TEXT DEFAULT 'Submitted'

        )
    """)

    # --------------------------------------
    # CHECK EXISTING COLUMNS
    # --------------------------------------

    cursor.execute("PRAGMA table_info(reports)")

    columns = [
        column[1]
        for column in cursor.fetchall()
    ]

    # --------------------------------------
    # ADD SEVERITY TO OLD DATABASE
    # --------------------------------------

    if "severity" not in columns:

        cursor.execute("""
            ALTER TABLE reports
            ADD COLUMN severity TEXT
        """)

    connection.commit()

    connection.close()


# ==========================================
# SAVE REPORT
# ==========================================

def save_report(
    report_id,
    problem,
    confidence,
    department,
    priority,
    severity,
    location,
    description
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO reports (

            report_id,
            problem,
            confidence,
            department,
            priority,
            severity,
            location,
            description,
            status

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        report_id,
        problem,
        confidence,
        department,
        priority,
        severity,
        location,
        description,
        "Submitted"

    ))

    connection.commit()

    connection.close()


# ==========================================
# GET ALL REPORTS
# ==========================================

def get_all_reports():

    # Make sure database structure is updated
    create_database()

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT

            report_id,
            problem,
            confidence,
            department,
            priority,
            severity,
            location,
            description,
            status

        FROM reports

        ORDER BY id DESC
    """)

    reports = cursor.fetchall()

    connection.close()

    return reports


# ==========================================
# UPDATE REPORT STATUS
# ==========================================

def update_report_status(
    report_id,
    new_status
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE reports

        SET status = ?

        WHERE report_id = ?
    """, (

        new_status,
        report_id

    ))

    rows_updated = cursor.rowcount

    connection.commit()

    connection.close()

    return rows_updated


# ==========================================
# FIND DUPLICATE REPORTS
# ==========================================

def find_duplicate_reports(
    problem,
    location
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT

            report_id,
            problem,
            location,
            status

        FROM reports

        WHERE LOWER(problem) = LOWER(?)

        AND LOWER(location) = LOWER(?)
    """, (

        problem.strip(),
        location.strip()

    ))

    duplicates = cursor.fetchall()

    connection.close()

    return duplicates