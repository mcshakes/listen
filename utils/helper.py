import re
from typing import List

def parse_title(title: str):
    pass

def check_for_dollah_bill(string: str) -> List[str]:
    return re.findall(r"[$][A-Za-z][\S]*", string)
