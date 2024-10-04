from typing import TypedDict, List, Union

class Command(TypedDict):
    command: str
    args: List[Union[int, bool, str]]
