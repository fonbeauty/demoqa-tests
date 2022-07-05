import pytest
from selene.support.shared import browser


def test_submit_form():
    browser.open('/text-box')