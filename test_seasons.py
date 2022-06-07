from seasons import validate, convert
import pytest
import unittest

class TestDate(unittest.TestCase):
    def test_validate(my_date):
        assert validate("1990-02-14") == ("1990-02-14")

        with pytest.raises(SystemExit):
            assert validate("cat") == "Invalid date"
            assert validate("1990 Jan, 12") == "Invalid date"

    def test_convert(my_date):
        # date changes accordin to  the today's date
        assert convert("1990-02-14") == "Sixteen million, nine hundred ninety-three thousand, four hundred forty minutes"
        
if __name__ == "__main__":
    unittest.main()
