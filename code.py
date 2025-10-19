import streamlit as st

# ===============================
# COMSATS GPA CALCULATOR
# ===============================
st.set_page_config(page_title="COMSATS GPA Calculator", page_icon="🎓", layout="centered")

st.title("🎓 COMSATS GPA CALCULATOR")
st.write("""
**Calculate your semester and cumulative GPA with ease using the COMSATS GPA Calculator.**  
Track your academic progress, check your grades, and gain a better understanding of the GPA scale.  
*We're here to support your journey to academic excellence!*
""")

# -------- Grading Scale Function ---------
def get_grade_and_gpa(marks):
    if marks >= 85:
        return "A", 4.00
    elif 80 <= marks <= 84:
        return "A-", 3.66
    elif 75 <= marks <= 79:
        return "B+", 3.33
    elif 71 <= marks <= 74:
        return "B", 3.00
    elif 68 <= marks <= 70:
        return "B-", 2.66
    elif 64 <= marks <= 67:
        return "C+", 2.33
    elif 61 <= marks <= 63:
        return "C", 2.00
    elif 58 <= marks <= 60:
        return "C-", 1.66
    elif 54 <= marks <= 57:
        return "D+", 1.30
    elif 50 <= marks <= 53:
        return "D", 1.00
    else:
        return "F", 0.00

# -------- Remarks Function ---------
def get_remarks(cgpa):
    if cgpa >= 3.50:
        return "🌟 Excellent work! Keep it up."
    elif cgpa >= 3.00:
        return "👍 Good job! You can aim even higher."
    elif cgpa >= 2.50:
        return "💪 You're doing okay. Work hard, you can do this."
    elif cgpa >= 2.00:
        return "⚠️ Below average. Stay focused and improve."
    else:
        return "🚨 You need to work very hard. Don't give up!"

# -------- User Input ---------
semesters = st.number_input("Enter the number of semesters:", min_value=1, step=1)

total_credit_hours = 0
total_quality_points = 0

for sem in range(1, semesters + 1):
    with st.expander(f"📚 Semester {sem}"):
        courses = st.number_input(f"Number of courses in Semester {sem}", min_value=1, step=1, key=f"course_count_{sem}")
        semester_credit_hours = 0
        semester_quality_points = 0

        for c in range(1, courses + 1):
            st.subheader(f"Course {c}")
            course_name = st.text_input(f"Course {c} Name", key=f"name_{sem}_{c}")
            credit_hours = st.number_input(f"Credit Hours for {course_name or f'Course {c}'}", min_value=1.0, step=1.0, key=f"ch_{sem}_{c}")
            marks = st.number_input(f"Marks for {course_name or f'Course {c}'}", min_value=0.0, max_value=100.0, step=1.0, key=f"marks_{sem}_{c}")

            if marks > 0 and credit_hours > 0:
                grade, gpa = get_grade_and_gpa(marks)
                st.write(f"**Grade:** {grade}  |  **GPA:** {gpa:.2f}")
                semester_credit_hours += credit_hours
                semester_quality_points += (gpa * credit_hours)

        if semester_credit_hours > 0:
            semester_gpa = semester_quality_points / semester_credit_hours
            st.success(f"✅ Semester {sem} GPA: {semester_gpa:.2f}")
            total_credit_hours += semester_credit_hours
            total_quality_points += semester_quality_points

# -------- Final CGPA ---------
if total_credit_hours > 0:
    cgpa = total_quality_points / total_credit_hours
    st.markdown("---")
    st.header("🎓 Final CGPA Result")
    st.write(f"**Total Credit Hours:** {total_credit_hours}")
    st.write(f"**Total Quality Points:** {total_quality_points:.2f}")
    st.subheader(f"📊 CGPA: {cgpa:.2f}")
    st.info(get_remarks(cgpa))
