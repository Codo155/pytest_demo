import pytest


@pytest.fixture(scope="class")
def message():
    return "hello"

@pytest.mark.usefixtures("message")
class TestWord:
    @pytest.fixture(autouse=True)
    def _inject_message(self, message):
        # hängt die Fixture an self.message
        self.message = message

    def test_change_message(self):
        self.message = "world"
        assert self.message == "world"

    def test_message(self):
        assert self.message== "hello"