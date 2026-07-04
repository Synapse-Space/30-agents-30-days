import re
def validate_name(value: str)-> bool:
    parts=value.strip().split()
    return len(parts)>=2

def validate_email(value:str)->bool:
    pattern = r"^[^@]+@[^@]+\.[^@]+$"
    return bool(re.match(pattern,value))


SUPPORTED_COUNTRIES={"india",
    "usa",
    "canada",
    "uk",
    "germany",
    "france",
    "australia",}

def validate_country(value: str)-> bool:
    return (
        value.lower() in SUPPORTED_COUNTRIES
    )

def validate_phone(
    value: str,
) -> bool:

    pattern = r"^\+?[0-9]{10,15}$"

    return bool(
        re.match(
            pattern,
            value,
        )
    )

