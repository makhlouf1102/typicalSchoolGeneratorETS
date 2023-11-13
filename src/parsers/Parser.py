from abc import ABC, abstractmethod

from src.commons.Session import Session


class Parser(ABC):
    COURSE_PER_SESSION_DIV = "rte js-collapse-element collapse__content collapse__content--open"

    _nb_course_per_session = _COURSE_PER_SESSION_CONTENT = None

    def __init__(self, nb_course_per_session: int = 4) -> None:
        self._nb_course_per_session = nb_course_per_session

    @staticmethod
    @abstractmethod
    def _parse_course(html, OPTIONS: dict) -> dict:
        pass

    @classmethod
    @abstractmethod
    def parse_all_courses(cls, html, options: dict) -> [Session]:
        pass

    @staticmethod
    def parse_course_details(html) -> str:
        html = html.find_all("div")[0]
        html = str(html)
        return html

    def get_courses_div_content(self) -> str:
        s = self._COURSE_PER_SESSION_CONTENT
        s = s.replace("[number]", str(self._nb_course_per_session))
        return s

    def set_nb_course_per_session(self, n: int) -> None:
        self._nb_course_per_session = n

    def get_nb_course_per_session(self) -> int:
        return self._nb_course_per_session

