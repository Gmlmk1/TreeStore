import pytest
import copy

from TreeStore import TreeStore


def test_get_all(items: dict, store: TreeStore):
    copied_items = copy.deepcopy(items)
    res = store.getAll()        
    assert copied_items == res
    
def test_item(store: TreeStore):
    res = store.getItem(7)
    assert res == {"id":7,"parent":4,"type":None}
    
def test_get_children(store: TreeStore):
    res = store.getChildren(4)
    assert res == [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
    res = store.getChildren(5)
    assert res == []
    
def test_get_all_parents(store: TreeStore):
    res = store.getAllParents(7)
    assert res == [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]