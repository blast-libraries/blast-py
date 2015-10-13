class Node:

    def __init__(self, kind=None, **fields):
        self.kind = kind
        for field, value in fields:
            setattr(self, field, value)
