students = {
    "student 1": {
        "name": "Naga",
        "age": 21,
        "subjects": {
            "subject1": "maths",
            "subject2": "physics",
            "subject3": "chemestry"
        }
    },
    "student 2": {
        "name": "Sai",
        "age": 22,
        "subjects": {
            "subject1": "biology",
            "subject2": "physics",
            "subject3": "chemestry"
        }
    },
    "student 3": {
        "name": "Manoj",
        "age": 23,
        "subjects": {
            "subject1": "history",
            "subject2": "economice",
            "subject3": "commerce"
        }
    }
}

print(students["student 3"]["subjects"]["subject1"])

students["student 3"]["subjects"]["subject1"] = "geography"

print(students["student 3"]["subjects"]["subject1"])
