from abc import ABC, abstractmethod
from constants import *


class UserPrompt(ABC):

    @staticmethod
    def pick_a_program() -> dict:
        while True:
            display_content_dic(PROGRAMS_TO_PICK)
            pick = input("\nPick one of the numbers displayed (To pick LOG by default press ENTER): ")

            if pick == '':
                pick = "1"

            if not pick.isdigit():
                print(f"{pick} is not a number, press a number please\n")

            else:
                program_number = int(pick)
                if PROGRAMS_TO_PICK.get(program_number) is not None:
                    print(f"\nYou picked {PROGRAMS_TO_PICK[program_number]}\n")
                    pick = PROGRAMS[PROGRAMS_TO_PICK[program_number]]
                    break
                else:
                    print(f"{pick} is out of range !\n")

        while True:
            nb_course_per_session = input("How much course per session would/do you take ? (4 or 5)")
            if nb_course_per_session == '':
                nb_course_per_session = '4'
            if not nb_course_per_session.isdigit():
                print(f"{nb_course_per_session} is not a number, press a number please\n")
                break
            else:
                nb_course_per_session = int(nb_course_per_session)
                if nb_course_per_session == 4 or nb_course_per_session == 5:
                    break
                else:
                    print(f"{nb_course_per_session} is out of range !\n")

        return {
            "program": pick,
            "nb_courses_per_session": nb_course_per_session
        }

    @classmethod
    @abstractmethod
    def other_questions(cls, OPTIONS: dict) -> dict:
        pass
