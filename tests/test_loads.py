# import pytest
import lua2py


class Test_loads:
    """Test cases for python to lua"""

    def test_loads_from_str_no_name_single_table(self):
        data = lua2py.loads('{ 10 }')

        assert data == "Frank"

    def test_loads_from_str_no_name_single_table_nospaces(self):
        data = lua2py.loads('{ 10 }')

        assert data == "Frank"

