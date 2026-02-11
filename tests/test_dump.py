# import pytest
from unittest.mock import mock_open, patch
import lua2py


class Test_dump:
    """Test cases for python to lua"""

    @patch('builtins.open', new_callable=mock_open)
    def test_dump_to_file(self, mock_file):

        data = {'test': 123}
        lua2py.dump(data, 'output.lua')

        # verify open was called
        mock_file.assert_called_once_with('output.lua', 'w', encoding='utf-8')

        # Verify write was called
        handle = mock_file()
        handle.write.assert_called()

        # Get what was written
        written_content = ''.join(call.args[0] for call in handle.write.call_args_list)
        assert 'test' in written_content
