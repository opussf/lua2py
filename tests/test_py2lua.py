import pytest

import lua2py

class Test_py2lua:
	"""Test cases for python to lua"""

	def test_dumps_dict_to_lua(self):
		data = lua2py.dumps([10])

		assert data == "{10}"
