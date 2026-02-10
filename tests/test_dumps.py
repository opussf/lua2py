import pytest
import lua2py


class Test_py2lua:
    """Test cases for python to lua"""

    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_list_to_lua_one_entry(self):
        data = lua2py.dumps([10])
        assert data == "{10}"

    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_list_to_lua_multiple(self):
        data = lua2py.dumps([1, 2, 3, 5, 7, 11])
        assert data == "{1,2,3,5,7,11}"

    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_list_to_lua_mixed(self):
        data = lua2py.dumps([1, "2", True, False, None, 11])
        assert data == "{1,\"2\",true,false,nil,11}"

    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_list_with_nested_list(self):
        data = lua2py.dumps([1, [2, [3, 4]]])
        assert data == "{1,{2,{3,4}}}"

    # ----------------
    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_dict_to_lua_one_entry_key(self):
        data = lua2py.dumps({"key": "value"})
        assert data == "{[\"key\"] = \"value\"}"

    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_dict_to_lua_multiple(self):
        data = lua2py.dumps({"k1": "v1", "k2": "v2"})
        assert data == "Write me"

    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_dict_to_lua_mixed(self):
        data = lua2py.dumps({"1": 1, "2": True, "3": False, "4": "4", "k1": "v1", "k2": 5})
        assert data == "Write me"

    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_dict_with_nested_dict(self):
        data = lua2py.dumps({"5": {"10": 42}})
        assert data == "{[\"5\"] = {[\"10\"] = 42}}"

    # ----------------  Primatives
    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_bool_true(self):
        data = lua2py.dumps(True)
        assert data == "true"

    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_bool_false(self):
        data = lua2py.dumps(False)
        assert data == "false"

    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_int_only(self):
        data = lua2py.dumps(42)
        assert data == "42"

    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_float_only(self):
        data = lua2py.dumps(3.1415927)
        assert data == 3.1415927

    @pytest.mark.skip("dumps() not yet implemented")
    def test_dumps_float_sub1(self):
        data = lua2py.dumps(0.01)
        assert data == 0.01

    def test_dumps_str_only(self):
        data = lua2py.dumps("lua rules")
        assert data == '"lua rules"'
