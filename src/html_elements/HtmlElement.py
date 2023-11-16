from abc import ABC


class HtmlElement(ABC):
    element_name: str = None

    def __init__(self, element_name: str):
        self.element_name = element_name
