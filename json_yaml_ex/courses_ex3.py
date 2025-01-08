import json

with open("3_courses.json", 'r') as json_file:
    courses = json.load(json_file)

for course in courses["courses"]:
    print(course.get("name"))
    total = 0
    for group in course["groups"]:
        print("\t" + group.get("name"), end='')
        total += group.get("students")
    print(f"\n\tTotal students for {course['name']}: {total}")
    print("")


