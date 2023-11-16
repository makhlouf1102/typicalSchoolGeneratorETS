from abc import ABC
from typing import List

from src.html_elements.HtmlElement import HtmlElement


class Tag(ABC, HtmlElement):
    _children: List[HtmlElement] = []

    def __init__(self, element_name: str):
        super().__init__(element_name)

    def add(self, child: HtmlElement) -> None:
        self._children.append(child)

    def add_children(self, children: List[HtmlElement]) -> None:
        for child in children:
            self._children.append(child)

    def __str__(self) -> str:
        string: str = f"<{super.element_name}>\n"
        for child in self._children:
            string += "\t" + str(child) + "\n"
        string += f"\n<{super.element_name}/>"
        return string
