class HtmlElement:
    element_name: str = None

    def __init__(self, element_name: str):
        self.element_name = element_name

    def __str__(self):
        return f"<{self.element_name}>"