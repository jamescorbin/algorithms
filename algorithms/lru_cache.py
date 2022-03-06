from typing import Optional, List
import collections

class DLNode():
    def __init__(self,
                 key: object,
                 val: object,
                 forward: Optional[DLNode]=None,
                 backward: Optional[DLNode]=None,):
        self.key = key
        self.val = val
        self.f = forward
        self.b = backward

class LRUCache:
    """
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = dict()
        self.head = None
        self.tail = None

    def get(self, key:int) -> int:
        if key in self.buffer:
            nd = self.buffer[key]
            ret = nd.val
            if nd != self.head:
                if nd != self.tail:
                    ndb = nd.b
                    ndf = nd.f
                    ndb.f = ndf
                    ndf.b = ndb
                else:
                    ndf = nd.f
                    ndf.b = None
                ndh = self.head
                ndh.f = nd
                nd.b = ndh
        else:
            ret = -1
        return ret

    def put(self, key:int, value:int) -> None:
        if key in self.buffer:
            nd = self.buffer[key]
            nd.val = value
            if nd != self.head:
                if nd != self.tail:
                    ndb = nd.b
                    ndf = nd.f
                    ndb.f = ndf
                    ndf.b = ndb
                else:
                    ndf = nd.f
                    ndf.b = None
                ndh = self.head
                ndh.f = nd
                nd.b = ndh
        else:
            if len(self.buffer) >= self.capacity:
                ndt = self.tail
                self.buffer.pop(ndt.key)
                ndn = ndt.f
                if ndt.f is not None:
                    self.tail = ndt.f
                    self.tail.b = None
                else;
                    self.tail = None
            nd = DLNode(key, value)
            self.buffer[key] = nd
            ndh = self.head
            if ndh is not None:
                ndh.f = nd
                nd.b = ndh
            self.head = nd
        return None
