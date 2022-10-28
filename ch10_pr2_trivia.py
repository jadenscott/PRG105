"""
This program uses a class to create trivia question objects in order to design a trivia game for two players.
"""


class Question:

    def __init__(self, question, answer_one, answer_two, answer_three, answer_four, correct_answer):
        self.__question = question
        self.__answer_one = answer_one
        self.__answer_two = answer_two
        self.__answer_three = answer_three
        self.__answer_four = answer_four
        self.__correct_answer = correct_answer

    def set_question(self, question):
        self.__question = question

    def get_question(self):
        return self.__question

    def set_answer_one(self, answer_one):
        self.__answer_one = answer_one

    def get_answer_one(self):
        return self.__answer_one

    def set_answer_two(self, answer_two):
        self.__answer_two = answer_two

    def get_answer_two(self):
        return self.__answer_two

    def set_answer_three(self, answer_three):
        self.__answer_three = answer_three

    def get_answer_three(self):
        return self.__answer_three

    def set_answer_four(self, answer_four):
        self.__answer_four = answer_four

    def get_answer_four(self):
        return self.__answer_four

    def set_correct_answer(self, correct_answer):
        self.__correct_answer = correct_answer

    def get_correct_answer(self):
        return self.__correct_answer


def main():
    p1_question_list = [Question('1. What does LED stand for?', 'Light-emulating dark', 'Light-emitting diode',
                                 'Low-end dialysis', 'Late-entertainment dame', 'B'),
                        Question('2. Who is the lead scorer of all time'
                                 ' in the NBA?', 'Michael Jordan', 'LeBron James', 'Wilt Chamberlain',
                                 'Kareem Abdul-Jabbar', 'D'),
                        Question('3. What is the number of the expressway that runs through Chicago from the north/south?',
                                 '90, 94', '51', '55', '290', 'A'),
                        Question("4. Which programming language is Bitcoin's source code written "
                                 "in?", 'C', 'Solidity', 'C++', 'Java', 'C'),
                        Question('5. Which year did Suzuki stop selling cars'
                                 'in North America?', '2012', '2009', '2016', '2005', 'A')]

    p2_questions_list = [Question('1. How far apart are the release dates of the PlayStation 4 and PlayStation 5,'
                                  ' respectively, in years?', '4', '5', '8', '7', 'D'),
                         Question('2. Who did the Chicago Bears '
                                  'select as the eleventh overall pick in the 2021 NFL draft?', 'Justin Fields',
                                  'Jaylen '
                                  'Waddle', 'Najee Harris', 'Mac Jones', 'A'),
                         Question('3. Which year did the Nintendo Switch '
                                  'come out?', '2016', '2018', '2017', '2015', 'C'),
                         Question('4. How many Grammy awards was '
                                  'Metallica nominated for?', '23', '15', '19', '27', 'A'),
                         Question('5. What is the name of '
                                  'highly anticipated upcoming Travis Scott album?', 'Escape Plan', 'Utopia',
                                  'Astroworld',
                                  'Mafia', 'B')]

    p1_score = 0
    p2_score = 0

    print('Each player will answer five questions.\nTYPE IN THE UPPERCASE LETTER.\n')

    for question in p1_question_list:

        print(f'{question.get_question()}\nA. {question.get_answer_one()}\nB. {question.get_answer_two()}\n'
              f'C. {question.get_answer_three()}\nD. {question.get_answer_four()}')

        p1_answer = input(f'Player 1: ')

        if p1_answer == question.get_correct_answer():
            print('Correct!\n')
            p1_score += 1
        else:
            print('Incorrect...\n')

    for question in p2_questions_list:

        print(f'{question.get_question()}\nA. {question.get_answer_one()}\nB. {question.get_answer_two()}\n'
              f'C. {question.get_answer_three()}\nD. {question.get_answer_four()}')

        p2_answer = input(f'Player 2: ')

        if p2_answer == question.get_correct_answer():
            print('Correct!\n')
            p2_score += 1
        else:
            print('Incorrect...\n')

    print(f"Player 1's score was {p1_score}/5")
    print(f"Player 2's score was {p1_score}/5")

    if p1_score > p2_score:
        print('Player 1 wins!')
    elif p2_score > p1_score:
        print('Player 2 wins!')
    else:
        print("Tie game!")


if __name__ == '__main__':
    main()
