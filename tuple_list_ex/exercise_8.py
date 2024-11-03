print("Write the scores for the test. Use -1 if you want to finish")
# print(float(input("score: ")))
score = 0
scores = []

while score != -1:
    score = float(input("score: "))
    scores.append(score)

scores.sort()
print(f'The scores (ordered): {scores}')
print(f"The average of these {len(scores)} scores - {sum(scores) / len(scores)}")