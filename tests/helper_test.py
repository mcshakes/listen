from utils import helper

class TestPostTitleParsing:
    def test_always_passes(self):
        assert True

    def test_dollar_bill_in_single_ticker(self):
        title = "this $AAPL shit is gnna MOON $$$"
        response = helper.check_for_dollah_bill(title)

        assert response is not None
        assert type(response) == list