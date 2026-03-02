from dataclasses import dataclass
from typing import Optional, List


@dataclass
class User:
    id: str
    name: str
    email: str
    roles: List[str]


@dataclass
class Project:
    id: str
    name: str
    start_date: str
    end_date: str
    owner_id: str
    members: List[str]
