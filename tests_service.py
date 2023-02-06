from random import randint
from test_yourself.db_controls import *


def shuffle_answers_to_test(specified_test) -> tuple:
    if specified_test:
        specified_test = specified_test.replace(" ", "_")
    else:
        specified_test = "drivers_test"

    all_data = get_db(specified_test)
    correct = {i[0]: i[3] for i in all_data}
    [test.insert(randint(1, 3), test.pop(3)) for test in all_data]
    return correct, all_data


def count_correct_answers(correct_answers: dict, user_answers: dict) -> tuple:
    number_of_correct_answers = 0
    for i in correct_answers:
        if user_answers[i] == correct_answers[i]:
            number_of_correct_answers += 1

    if number_of_correct_answers / len(correct_answers) > 0.75:
        return True, number_of_correct_answers
    return False, number_of_correct_answers


def get_table_names_in_correct_format():
    all_topics = get_db()
    all_topics = [str(i[0]).replace("_", " ") for i in all_topics]
    return all_topics