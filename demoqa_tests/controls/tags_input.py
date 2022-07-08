from selene import have
from selene.core.entity import Element
from selene.support.shared import browser


class TagsInput:
    def __init__(self, element: Element):
        self.element = element

    def autocomplete(self, from_: str, autocomplete: str):
        self.element.type(from_)
        self._click_on_subject(autocomplete)

    def type(self, type: str):
        self.element.type(type)
        self._click_on_subject(type)

    def _click_on_subject(self, type):
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(type)).click()

