from Course import Course
from Parser import Parser
from Session import Session


class LogParser(Parser):
    _COURSE_PER_SESSION_CONTENT = "Cheminement à [number] cours par session"

    def __init__(self, nb_course_per_session: int = 4):
        super().__init__(nb_course_per_session)

    @staticmethod
    def _parse_course(html, options: dict) -> dict:
        after_2023 = options["after_2023"]
        td_list = html.find_all("td")
        course_id = None
        if len(td_list) == 2:
            a = td_list[1].find_all("a")
            course_id = td_list[0].text.strip()
            if course_id == "COM120" and after_2023:
                course_id = a[-1].text.strip()

            name = a[0].text.strip()
            cr = int(td_list[1].text.strip().split("(")[1][0])
        else:
            name = td_list[0].text.strip().split("(")[0].strip()
            cr = int(td_list[0].text.strip().split("(")[1][0].strip())

        return {
            "course_id": course_id,
            "name": name,
            "cr": cr,
            "description": None
        }

    @classmethod
    def parse_all_courses(cls, html, options: dict) -> [Session]:
        sessions: [Session] = []
        for div in html:
            if div.name == "h3":
                title = div.text.strip()
                if title:
                    sessions.append(Session(title=title))
            if sessions and div.name == "table":
                current_session = sessions[-1]
                courses = div.find_all("tr")
                for c in courses:
                    c = cls._parse_course(c, options)
                    current_session.add_course(Course(c["course_id"], c["name"], c["cr"], c["description"]))
        return sessions
