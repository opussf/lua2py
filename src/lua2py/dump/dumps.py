from typing import Any


class dumps:
    def __new__(cls, obj_in: Any) -> str:
        """__init__ returns an object, __new__ can return a value"""
        instance = super().__new__(cls)
        instance.list_out = [[]]
        instance.list_num = 0

        instance.__parse_obj(obj_in)
        print(instance.list_out)

        return "".join(instance.list_out)

    def __parse_obj(instance, obj_in: Any) -> None:
        if isinstance(obj_in, bool):
            instance.list_out[instance.list_num].append(obj_in and "true" or "false")
        elif isinstance(obj_in, int):
            instance.list_out.append(str(obj_in))
        elif isinstance(obj_in, str):
            instance.list_out.append(f'"{obj_in}"')
        elif isinstance(obj_in, list):
            instance.list_out.append("{")
            instance.__dumps_list(obj_in)
        elif isinstance(obj_in, dict):
            instance.list_out.append("{")
            instance.__dumps_dict(obj_in)
        elif obj_in is None:
            instance.list_out.append("nil")

    def __dumps_list(instance, list_in: list) -> None:
        print(f"{list_in} is a list!")
        for item in list_in:
            instance.__parse_obj(item)
            instance.list_out.append(",")

    def __dumps_dict(instance, dict_in: dict) -> None:
        print(f"{dict_in} is a dict.")
        for key, value in dict_in.items():
            print(f"[{key}] = {value}")
