from LogParser import LogParser
from Parser import Parser
from ParserFactory import ParserFactory


class LogParserFactory(ParserFactory):
    @staticmethod
    def create_parser(options: dict) -> Parser:
        return LogParser(options["nb_courses_per_session"])
