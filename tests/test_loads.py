# import pytest
import lua2py


class Test_lua2py:
    """Test cases for lua to python"""

    def test_load_from_str_no_name(self):
        data = lua2py.loads('{ 10 }')

        assert data == "Frank"
