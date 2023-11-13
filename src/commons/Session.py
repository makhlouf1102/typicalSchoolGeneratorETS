from src.commons.Course import Course


class Session:
    _title = None
    _courses: [Course] = None

    def __init__(self, title: str):
        self._title = title
        self._courses = []

    def add_course(self, c: Course) -> None:
        self._courses.append(c)

    def remove_course(self, c: Course) -> None:
        self._courses.remove(c)

    def get_title(self) -> str:
        return self._title

    def set_title(self, title: str) -> None:
        self._title = title

    def get_courses(self) -> [Course]:
        return self._courses

    def get_dict(self) -> [dict]:
        result = []
        for c in self._courses:
            result.append(c.get_dict())
        return result

    def get_html(self) -> str:
        html: str = f"""
                    <h2>{self._title}</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Identifiant</th>
                                <th>Nom du cours</th>
                                <th>Nombre de credits</th>
                                <th>Description</th>
                            </tr>
                        </thead>
                        <tbody>
                """
        for c in self._courses:
            html += c.get_html()
        html += """
                </tbody>
            </table>
            """

        return html

    def __str__(self) -> str:
        s = self._title + "\n"
        for c in self._courses:
            s += str(c) + "\n"
        return s
