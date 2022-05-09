"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

    NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
    int next() Returns the next integer in the nested list.
    boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res

If res matches the expected flattened list, then your code will be judged as correct.
"""
from typing import Optional

class NestedIterator():
    def __init__(self, nestedList: "[NestedInteger]"):
        self.nested_iters = [iter(nestedList)]
        self.cached_value = None

    def next(self) -> Optional[int]:
        if self.cached_value is None:
            if len(self.nested_iters) > 0:
                it = self.nested_iters[-1]
                try:
                    val = next(it)
                    if type(val) is list:
                        self.nested_iters.append(iter(val))
                        ret = self.next()
                    else:
                        ret = val
                except StopIteration:
                    self.nested_iters.pop()
                    ret = self.next()
            else:
                ret = None
        else:
            ret = self.cached_value
            self.cached_value = None
        return ret

    def hasNext(self) -> bool:
        if self.cached_value is None:
            self.cached_value = self.next()
        return (self.cached_value is not None)

def test():
    arrs = [
        [[1, 1], 2, [1, 1]],
        [1, [4, [6]]],
        ]
    nest_it = NestedIterator(arrs[0])
    output = []
    while nest_it.hasNext():
        output.append(nest_it.next())
    print(output)
    output = []
    nest_it = NestedIterator(arrs[1])
    while nest_it.hasNext():
        output.append(nest_it.next())
    print(output)

if __name__=="__main__":
    test()
