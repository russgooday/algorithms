import json

def _is_nested(lst: list) -> bool:
    basic_primitives = (str, int, float, bool)

    return not all(isinstance(i, (basic_primitives)) for i in lst)

def prettify_log(obj: any):
    return json.dumps(
        obj,
        indent=4 if _is_nested(obj) else None
    )
