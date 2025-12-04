"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    round_score = []
    for value in student_scores:
        round_score.append(round(value))
    return round_score

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    accu = 0

    for value in student_scores:
        if value <= 40:
            accu += 1

    return accu

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    new_list = []
    for value in student_scores:
        if value >= threshold:
            new_list.append(value)
    return new_list
        

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    base = (highest-40)/4
    new_list = []
    val = 41
    new_list = [int(val)]
    for value in range(3):
        new_list.append(int(val+base))
        val = new_list[-1]
    return new_list

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    sort_list=[]
    if len(student_names) == len(student_scores):
        for i in range(1, len(student_names)+1):
            value_str = f"{i}. {student_names[i-1]}: {student_scores[i-1]}"
            sort_list.append(value_str)
    return sort_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for list in student_info:
        if list[-1] == 100: return list
    return []
