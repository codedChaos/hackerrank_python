#! python3
"""Scratch Pad 2 for Python

Place for hacking python together and testing.
"""
def scoreAverage(s1, d1):
    score = float()
    scores_length = int()
    if s1 in d1:
        try:
            for num in d1[s1]:
                score += num
            scores_length = len(d1[s1])
        except ValueError as e:
            print(e)
        return (score / scores_length)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float,
                          line))
        student_marks[name] = scores
    query_name = input()
    studentAvg = scoreAverage(query_name, student_marks)
    print("{:.2f}".format(studentAvg))
