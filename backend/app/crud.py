from typing import List

class CRUD:
    def __init__(self):
        self._store: List[dict] = []

    def create(self, item: dict) -> dict:
        self._store.append(item)
        return item

    def read_all(self) -> List[dict]:
        return list(self._store)

    def read(self, item_id: str) -> dict:
        for it in self._store:
            if it.get('id') == item_id:
                return it
        return {}
