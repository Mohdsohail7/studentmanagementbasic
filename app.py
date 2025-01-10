from flask import Flask, request, jsonify

app = Flask(__name__)

# 1 String Manipulation Utilities
# Add endpoints to handle household-related string operations.

# Find Assignment Title Length
@app.route("/title-length", methods = ["GET"])
def title_length():
    title = request.args.get("title", 0)
    return f"Assignment title length: {len(title)}"

# Extract Initials from a Student Name
@app.route("/extract-initials", methods = ["GET"])
def extract_initials():
    name = request.args.get("name", 0)
    words = name.split()
    initials = "".join(word[0] for word in words)
    return f"Student initials: {initials}"

# Create Assignment Slug
# Create an endpoint to generate a slug for an assignment title by replacing spaces with hyphens and converting it to lowercase.
@app.route("/create-slug", methods = ["GET"])
def create_slug():
    title = request.args.get("title", 0)
    generateSlug = title.replace(" ", "-").lower()
    return f"Assignment slug: {generateSlug}"


# 2. Calculations
# Add endpoints to calculate utilities

# Calculate Total Marks
# Create an endpoint to calculate the total marks of a student by summing up marks for three subjects.
@app.route("/calculate-total-marks", methods = ["GET"])
def calculate_total_marks():
    marks1 = int(request.args.get("marks1", 0))
    marks2 = int(request.args.get("marks2", 0))
    marks3 = int(request.args.get("marks3", 0))
    totalMarks = marks1 + marks2 + marks3
    return f"Total marks: {totalMarks}"

# Calculate Average Marks
# Create an endpoint to calculate the average marks of a student from three subjects.
@app.route("/calculate-average-marks", methods = ["GET"])
def calculate_average_marks():
    marks1 = float(request.args.get("marks1", 0))
    marks2 = float(request.args.get("marks2", 0))
    marks3 = float(request.args.get("marks3", 0))
    avgMarks = (marks1 + marks2 + marks3) / 3
    return f"Average marks: {round(avgMarks, 2)}"

# Calculate Grade
# Create an endpoint to assign a grade based on a student’s total marks.
@app.route("/calculate-grade", methods = ["GET"])
def calculate_grade():
    totalMarks = int(request.args.get("totalMarks", 0))
    if totalMarks >= 90:
        grade = "A"
    elif totalMarks >= 80:
        grade = "B"
    elif totalMarks >= 70:
        grade = "C"
    elif totalMarks >= 35:
        grade = "D"
    else:
        grade = "F"
    return f"Grade: {grade}"


# 3. Conditional Checks
# Add endpoints to check the given conditions.

# Check Pass or Fail
# Create an endpoint that checks whether a student passed or failed based on their marks.
@app.route("/check-pass-fail", methods = ["GET"])
def check_pass_fail():
    marks = int(request.args.get("marks", 0))
    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"
    return result

# Check Eligibility for Scholarship
# Create an endpoint to check if a student is eligible for a scholarship.
@app.route("/check-scholarship", methods = ["GET"])
def check_scholarship():
    marks = int(request.args.get("marks", 0))
    attendance = int(request.args.get("attendance", 0))
    if marks >= 85 & attendance >= 90:
        result = "Eligible for Scholarship"
    else:
        result = "Not Eligible for Scholarship"
    return result

# 4. Function-Based
# Create helper functions for reusable logic.
# Calculate Late Submission Penalty
# Create an endpoint to calculate the penalty for a late submission based on the number of days late.
def calculatePenalty(daysLate, penaltyPerDay):
    penalty =  daysLate * penaltyPerDay
    return f"Total penalty: {penalty}"

@app.route("/calculate-late-penalty", methods = ["GET"])
def calculate_late_penalty():
    daysLate = int(request.args.get("daysLate", 0))
    penaltyPerDay = int(request.args.get("penaltyPerDay", 0))
    return calculatePenalty(daysLate, penaltyPerDay)

# Estimate Study Hours
# Create an endpoint that estimates the total study hours required based on daily hours and total days.
def calculateStudyHours(dailyHours, totalDays):
    total = dailyHours * totalDays
    return f"Total study hours: {total}"

@app.route("/estimate-study-hours", methods = ["GET"])
def estimate_study_hours():
    dailyHours = int(request.args.get("dailyHours", 0))
    totalDays = int(request.args.get("totalDays", 0))
    return calculateStudyHours(dailyHours, totalDays)

# Recommend Assignment Topics
# Create an endpoint that recommends topics to students based on their interests.
topics_data = {
    'AI': ['Machine Learning', 'Neural Networks', 'Natural Language Processing'],
    'Web Development': ['HTML', 'CSS', 'JavaScript', 'React'],
    'Data Science': ['Data Analysis', 'Visualization', 'Pandas', 'NumPy']
}

def recommendTopics(interest):
    topics = topics_data.get(interest, [])
    if topics:
        return f"Recommended Topics: {', '.join(topics)}"
    return "No topics found for the given interest."

@app.route("/recommend-topics", methods = ["GET"])
def recommend_topics():
    interest = request.args.get("interest", 0)
    return recommendTopics(interest)

if __name__ == "__main__":
    app.run()