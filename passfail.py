
scores = [65, 90, 45, 80, 50, 76, 88, 92, 59, 30]


results = []


for score in scores:
    if score >= 60:
        results.append((score, 'pass'))
    else:
        results.append((score, 'FAIL'))


for result in results:
    print(f"Score: {result[0]} -> {result[1]}")

