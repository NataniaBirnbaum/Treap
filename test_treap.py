import random
import pytest
from Treap import *

size = 300

def f(x):
    return (x*5)%17

def test_insert():
    # passes if node inserts "take" (number of nodes inserted equals __size)
    t = Treap()
    for i in range(size):
        #t.insert(i, str(i), f(i))
        t.insert(i, str(i))
        assert t.getSize() == i+1
    assert t.getSize() == size

def test_find():
    # passes if all nodes inserted can be found in treap
    t = Treap()
    for i in range(size):
        #t.insert(i, str(i), f(i))
        t.insert(i, str(i))
    t.traverse("in")
    for i in range(size-1, -1, -1):
        assert t.find(i)
        assert not t.find(i+size)

def test_delete():
    # passes if nodes removed can no longer be found, and __size decreases with each deletion
    t = Treap()
    for i in range(size):
        #t.insert(i, str(i), f(i))
        t.insert(i, str(i))
    for i in range(size//2, (size*3)//2):
        j = i%size
        s = t.getSize()
        t.delete(j)
        assert not t.find(j)
        assert t.getSize() == s-1


pytest.main(["-v"])