import functools

from generator.consts import (
    BUILTIN_TYPES,
    RETURN_PATTERNS,
    READ_MORE_PATTERN,
    SYMBOLS_MAP,
)


def normalize_description(text: str) -> str:
    for bad, good in SYMBOLS_MAP.items():
        text = text.replace(bad, good)
    text = READ_MORE_PATTERN.sub("", text)
    text.strip()
    return text


def normalize_annotation(item: dict):
    for key in list(item.keys()):
        item[key.lower()] = item.pop(key)

    item["description"] = normalize_description(item["description"])


def normalize_method_annotation(item: dict):
    normalize_annotation(item)
    item["required"] = {"Optional": False, "Yes": True}[item["required"]]
    item["name"] = item.pop("parameter")


def normalize_type_annotation(item: dict):
    normalize_annotation(item)

    item["name"] = item.pop("field")

    if item["description"].startswith("Optional"):
        item["required"] = False
        item["description"] = item["description"][10:]
    else:
        item["required"] = True


@functools.lru_cache()
def normalize_type(string):
    if not string:
        return "typing.Any"

    lower = string.lower()
    split = lower.split()

    if split[0] == "array":
        new_string = string[lower.index("of") + 2 :].strip()
        return f"List[{normalize_type(new_string)}]"
    if "or" in split:
        split_types = string.split(" or ")
        norm_str = ", ".join(map(normalize_type, map(str.strip, split_types)))
        return f"Union[{norm_str}]"
    if "number" in lower:
        return normalize_type(string.replace("number", "").strip())
    if lower in ["true", "false"]:
        return "bool"
    if string not in BUILTIN_TYPES and string[0].isupper():
        return f"{string}"
    elif string in BUILTIN_TYPES:
        return BUILTIN_TYPES[string]
    return "Any"


@functools.lru_cache()
def get_returning(description):
    parts = list(filter(lambda item: "return" in item.lower(), description.split(".")))
    if not parts:
        return "Any", ""
    sentence = ". ".join(map(str.strip, parts))
    return_type = None

    for pattern in RETURN_PATTERNS:
        temp = pattern.search(sentence)
        if temp:
            return_type = temp.group("type")
            if "other" in temp.groupdict():
                otherwise = temp.group("other")
                return_type += f" or {otherwise}"
        if return_type:
            break

    return return_type, sentence + "."


def normalize_optional(python_type: str, required: bool = True) -> str:
    if not required:
        if "Union" in python_type and "," not in python_type:
            python_type = python_type.replace("Union", "Optional")
        else:
            python_type = f"Optional[{python_type}]"
    return python_type


def pythonize_name(name: str) -> str:
    return "".join(
        f"_{s}" if i > 0 and s.isupper() else s for i, s in enumerate(name)
    ).lower()


def collect_imports(python_type, telegram_types):
    from generator.structures import Import

    for typing_import in {"Any", "Union", "Optional", "List"}:
        if typing_import in python_type:
            yield Import("typing", {typing_import})
    for telegram_import in telegram_types:
        if telegram_import in python_type:
            yield Import(f".{pythonize_name(telegram_import)}", {telegram_import})
