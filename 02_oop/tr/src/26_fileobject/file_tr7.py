math_reports = [
    {"subject": "math", "name": "Alice", "score": 90},
    {"subject": "math", "name": "Bob", "score": 80},
]
english_reports = [
    {"subject": "english", "name": "Alice", "score": 90},
    {"subject": "english", "name": "Bob", "score": 100},
]
file = "report.csv"

reports = math_reports + english_reports
with open(file, "w") as f:
    for report in reports:
        f.write(f"{report['subject']},{report['name']},{report['score']}\n")
