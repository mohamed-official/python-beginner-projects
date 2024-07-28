tasks = [{"task": "Mohamed"}, {"task": "Ahmed"}]


keyword = "Am".lower()
results = filter(lambda task: keyword in task["task"].lower(), tasks)

print(list(results))
