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



if __name__ == "__main__":
    app.run()