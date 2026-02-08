from typing import Any

def dumps(obj_in: Any) -> str:
    if isinstance(obj_in, list):
        return __dumps_list(obj_in)
    if isinstance(obj_in, dict):
        return __dumps_dict(obj_in)

def __dumps_any(obj_in: Any) -> str:
    if isinstance(obj_in, bool):
        print(f"{obj_in} is a bool.")
    elif isinstance(obj_in, int):
        print(f"{obj_in} is an int.")
    elif isinstance(obj_in, str):
        print(f"{obj_in} is a str.")
    elif isinstance(obj_in, list):
        print(f"{obj_in} is a list.")
    elif isinstance(obj_in, dict):
        print(f"{obj_in} is a dict.")
    elif obj_in is None:
        print(f"{obj_in} is a None")

def __dumps_list(list_in: list) -> str:
    print("I am a list!")
    for i in list_in:
        print(i, type(i))
        __dumps_any(i)

def __dumps_dict(dict_in: dict) -> str:
    print("I am a dict")