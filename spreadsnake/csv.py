class alias(obj):

    def __init__(self, *args):
        self.aliases = aliases

    def __call__(self, f):
        f._aliases = self.aliases
        return f

def identifier(a_cls):
    original = a_cls.__dict__.copy()
    for name, method in original.iteritems():
        if hasattr(method, '_aliases'):
            for alias in method._aliases - set(original):
                setattr(a_cls, alias, method)
    return a_cls

def connect(fp: str) -> Connection:
    f = open(fp, "w")
    return Connection(f)

@identifier
class Connection:

    def __init__(self: Connection, f: file) -> Connection:
        self.f = f
        self.contents = f.read().split('\n')
        for i in range(len(self.contents)):
            self.contents[i] = self.contents[i].split(',')
        self.width = len(self.contents[0])
        self.height = len(self.contents)

    def clear(self: Connection) -> None:
        self.f.truncate()

    @alias('commit')
    def close(self: Connection) -> None:
        self.f.close()
    
    def append_row(self: Connection, *args: list) -> bool:
        return True

    def insert_row(self: Connection, row: int, *args: list) -> bool:
        return True

    def append_column(self: Connection, *args: list) -> bool:
        return True

    def insert_column(self: Connection, col: int, *args: list) -> bool:
        return True
