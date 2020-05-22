

if __name__ == '__main__':
    students_grades = list()
    low_score = float(100.00)
    scores_list = list()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores_list.append(score)
        students_grades.append([str(name), float(score)])
        low_score = min(scores_list)
        
    print("low score: ", low_score)
    print("students_grades: ", students_grades)
    print("scores_list: ", scores_list)
    
    while low_score in scores_list:
        scores_list.remove(low_score)
    
    print("scores_list 2nd pass: ", scores_list)