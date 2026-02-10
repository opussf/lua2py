import pytest
import lua2py


class Test_load:
    """Test cases for python to lua from file
    Will always return a dictionary."""

    @pytest.mark.skip("load() not yet implemented")
    def test_load_from_str_no_name_single_table(self):
        data = lua2py.load('{ 10 }')
        # assert data == {1: 10}

    @pytest.mark.skip("load() not yet implemented")
    def test_load_from_str_no_name_single_table_nospaces(self):
        data = lua2py.load('{ 10 }')

        assert data == "Frank"

