from parsers.factories.LogParserFactory import LogParserFactory
from parsers.Parser import Parser

# --------- Constants ---------
PROGRAMS_TO_PICK = {
    1: "LOG",
    2: "TI"
}

PROGRAMS = {
    "LOG": "logiciel",
    "TI": "des-TI",
}


# --------- Functions ---------


def display_content_dic(dic: dict) -> None:
    for key, value in dic.items():
        print(f"{key} --> {value}")


def get_parser_of(options: dict) -> Parser:
    match options["program"]:
        case "logiciel":
            return LogParserFactory.create_parser(options=options)
        case "des-TI":
            return LogParserFactory.create_parser(options=options)


def ask_right_questions(options: dict) -> dict:
    from src.prompts.LogUserPrompt import LogUserPrompt
    match options["program"]:
        case "logiciel":
            return LogUserPrompt.other_questions(options=options)
        case "des-TI":
            return LogUserPrompt.other_questions(options=options)
