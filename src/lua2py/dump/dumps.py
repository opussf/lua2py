from typing import Any


class dumps:
    def __new__(cls, obj_in: Any) -> str:
        """__init__ returns an object, __new__ can return a value"""
        instance = super().__new__(cls)
        instance.list_out = []
        instance.__parse_obj(obj_in)
        print(instance.list_out)
        return(instance.__str_out())

    def __parse_obj(instance, obj_in: Any) -> None:
        if isinstance(obj_in, bool):
            instance.list_out.append(obj_in and "true" or "false")
        elif isinstance(obj_in, (int,float)):
            instance.list_out.append(str(obj_in))
        elif isinstance(obj_in, str):
            instance.list_out.append(f'"{obj_in}"')
        elif isinstance(obj_in, list):
            instance.list_out.append("{")
            instance.__dumps_list(obj_in)
            instance.list_out.append("}")
        elif isinstance(obj_in, dict):
            instance.list_out.append("{")
            instance.__dumps_dict(obj_in)
            instance.list_out.append("}")
        elif obj_in is None:
            instance.list_out.append("nil")

    def __dumps_list(instance, list_in: list) -> None:
        print(f"{list_in} is a list!")
        for item in list_in:
            instance.__parse_obj(item)

    def __dumps_dict(instance, dict_in: dict) -> None:
        print(f"{dict_in} is a dict.")
        for key, value in dict_in.items():
            instance.list_out.append("[")
            instance.__parse_obj(key)
            instance.list_out.append("] = ")
            instance.__parse_obj(value)

            # instance.list_out.append(f"[{key}] = {value}")

    def __str_out(instance) -> str:
        tmp_list = []
        for ele in instance.list_out:
            print(f"{tmp_list}\t+\t{ele}")
            if len(tmp_list)>=1 and (tmp_list[-1][-1] == "{" or tmp_list[-1][-1] == "["):
                tmp_list[-1] = tmp_list[-1] + ele
            elif len(tmp_list)>=1 and tmp_list[-1][-2:] == "= ":
                tmp_list[-1] = tmp_list[-1] + ele
            elif ele == "] = ":
                tmp_list[-1] = tmp_list[-1] + ele
            elif ele == "}" or ele[0] == "]":
                tmp_list[-1] = tmp_list[-1] + ele
            else:
                tmp_list.append(ele)

        print(tmp_list)
        return(",".join(tmp_list))
