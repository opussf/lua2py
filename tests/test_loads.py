import pytest
import lua2py


class Test_loads:
    """Test cases for python to lua
    Will always return a dictionary."""

    @pytest.mark.skip("load() not yet implemented")
    def test_loads_from_str_no_name_single_table(self):
        data = lua2py.loads('{ 10 }')
        assert data == {1: 10}

    @pytest.mark.skip("load() not yet implemented")
    def test_loads_from_str_no_name_single_table_nospaces(self):
        data = lua2py.loads('{10}')
        assert data == {1: 10}

    @pytest.mark.skip("load() not yet implemented")
    def test_loads_multiple_tables(self):
        data = lua2py.loads('a = {11}\nb = {12}\n')
        assert data["a"] == {1: 11}
        assert data["b"] == {1: 12}
