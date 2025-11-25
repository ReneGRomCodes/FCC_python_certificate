class HashTable:

    def __init__(self):
        self.collection: dict[int, dict[str, str]] = {}

    @staticmethod
    def hash( k: str) -> int:
        return sum(ord(c) for c in k)

    def add(self, k: str, v: str) -> None:
        hash_value: int = self.hash(k)

        if hash_value not in self.collection:
            self.collection[hash_value] = {k: v}
        else:
            self.collection[hash_value][k] = v

    def remove(self, k: str) -> None:
        hash_value: int = self.hash(k)

        if hash_value in self.collection:
            del self.collection[hash_value][k]

    def lookup(self, k: str) -> str | None:
        hash_value = self.hash(k)

        if hash_value in self.collection:
            return self.collection[hash_value][k]

        return None
