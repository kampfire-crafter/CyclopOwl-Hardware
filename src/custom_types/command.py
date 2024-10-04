from typing import TypedDict, List, Union

class Command(TypedDict):
    """Defines a command structure with action and arguments."""
    command: str
    args: List[Union[int, bool, str]]
