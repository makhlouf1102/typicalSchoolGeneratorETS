
class Course:
    _id = _name = _cr = _description = None
    _link = "https://www.etsmtl.ca/etudes/cours"

    def __init__(self, id_course, name, cr, description=None) -> None:
        self._id = id_course
        self._name = name
        self._cr = cr
        self._link = self._link + '/' + str(self._id) if id_course is not None else None
        self._description = None

    def get_link(self) -> str:
        return self._link

    def set_description(self, description: str) -> None:
        self._description = description

    def get_dict(self) -> dict:
        return {
            "id": self._id,
            "name": self._name,
            "cr": self._cr,
            "description": self._description
        }

    def get_html(self) -> str:
        html: str = ""

        if self._id:
            # description = self._description.replace("\n", "<br>")
            html = f"""
                    <td>{ self._id }</td>
                    <td>{ self._name }</td>
                    <td>{ self._cr }</td>
                    <td class="description">{ self._description }</td>
                """
        else:
            if "complémentaire" in self._name:
                pass
            if "concentration " in self._name:
                html = f"""
                        <td>Aucun</td>
                        <td>{self._name}</td>
                        <td>{self._cr}</td>
                        <td class="description">* voir dans le tableau des cours complémentaires</td>
                    """
                html = f"""
                        <td>Aucun</td>
                        <td>{self._name}</td>
                        <td>{self._cr}</td>
                        <td class="description">* voir dans le tableau des cours de concentrations</td>
                    """
            else:
                html = ""

        html: str = f"""
                    <tr>
                        {html}
                    </tr>
                """
        return html

    def __str__(self) -> str:
        if self._id :
            s = f"{self._id}, {self._name} "
        else:
            s = f"{self._name} "
        return s + f"({self._cr} cr.) \n {self._description}"
