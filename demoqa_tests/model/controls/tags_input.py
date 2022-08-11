from selene import have
from selene.core.entity import Element
from selene.support.shared import browser


class TagsInput:

    def __init__(self, element: Element):
        self.element = element

    def add_by_click(self, from_: str):
        self.element.type(from_)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(from_)).click()
        return self

    def add_by_tab(self, from_: str, /):
        self.element.type(from_).press_tab()
        return self