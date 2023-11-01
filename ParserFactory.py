from abc import ABC, abstractmethod

from Parser import Parser


class ParserFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_parser(options: dict) -> Parser:
        return Parser(options["nb_course_per_session"])
