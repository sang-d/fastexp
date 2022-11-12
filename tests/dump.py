class Base:
    id: int
    desc: str

    def __init__(self, id, desc=""):
        self.id = id
        self.desc = desc

    def __repr__(self) -> str:
        return str(self.id) + " " + self.desc

    def __str__(self) -> str:
        return str(self.id) + " " + self.desc


class Item:
    def __init__(self, id: int, desc: str, children: list[Base] = []):
        self.id = id
        self.desc = desc
        self.children = children

    def __repr__(self) -> str:
        children = " ".join([str(item) for item in self.children])
        return str(self.id) + " " + self.desc + " " + children


a = Item(1, "testa")
b = Item(2, "testb")
c = Item(3, "c", [Base(a), Base(b)])

print(c)
