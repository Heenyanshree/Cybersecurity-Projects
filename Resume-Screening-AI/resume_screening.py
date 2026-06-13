print("================================")
print("       RESUME SCREENING AI")
print("================================")

resume = input("Paste resume text: ")

required_skills = [
    "python",
    "cybersecurity",
    "networking",
    "linux",
    "sql",
    "git",
    "machine learning"
]

score = 0
matched_skills = []

for skill in required_skills:
    if skill in resume.lower():
        score += 1
        matched_skills.append(skill)

print("\nResume Screening Report")
print("------------------------")
print("Matched Skills:", matched_skills)
print("Score:", score, "/", len(required_skills))

if score >= 5:
    print("Result: Shortlisted")
elif score >= 3:
    print("Result: Maybe")
else:
    print("Result: Not Shortlisted")