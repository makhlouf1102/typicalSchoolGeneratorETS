from UserPrompt import UserPrompt


class LogUserPrompt(UserPrompt):
    @classmethod
    def other_questions(cls, options: dict) -> dict:
        options = cls._ask_debut_year(options)
        return options

    @staticmethod
    def _ask_debut_year(options: dict) -> dict:
        while True:
            after_2023 = input("\nHave you started your journey after autumn 2023 (Y/N): ")

            if after_2023 == 'Y' or after_2023 == '':
                after_2023 = True
                break
            if after_2023 == 'N':
                after_2023 = False
                break
            else:
                print(f"\"{after_2023}\" is not a right answer !\n")
        options["after_2023"] = after_2023
        return options
