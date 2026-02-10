from typing import Any, IO
import lua2py


def dump(obj_in: Any, file_in: IO[str]) -> None:
    with open(file_in, "w", encoding="utf-8") as fh:
        fh.write(lua2py.dumps(obj_in))
