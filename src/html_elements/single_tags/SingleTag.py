from src.html_elements.HtmlElement import HtmlElement


class SingleTag(HtmlElement):
    def __init__(self, element_name: str):
        super().__init__(element_name)

    def __str__(self):
        return f"<{super.element_name}/>"
