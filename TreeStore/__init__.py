from collections import defaultdict

class Node:
    def __init__(self) -> None:
        self.index: int = None
        self.childrens: list = []
        self.parent: int = None

class TreeStore:            
    
    def __init__(self, items: list[dict]) -> None:
        self.items = items        
        self.objs = defaultdict(Node)
        for index, value in enumerate(items):
            id, parent = value["id"], value["parent"]
            node = self.objs[id]
            node.index = index
            if parent == "root": continue
            
            node.parent = parent
            self.objs[parent].childrens.append(id)
            
            
    def getAll(self) -> list[dict]:
        return self.items
    
    def __get_obj(self, id: int):
        obj: Node = self.objs.get(id, None)
        if not obj:
            raise Exception(f"hasn't id - {id}")
        return obj
    
    def __get_index(self, id: int) -> int:
        return self.objs[id].index
    
    def getItem(self, id: int) -> dict:                
        obj = self.__get_obj(id)
        return self.items[obj.index]
    
    def getChildren(self, id: int) -> list[dict]:
        obj = self.__get_obj(id)    
        return [self.items[self.__get_index(id)] for id in obj.childrens]
    
    def getAllParents(self, id: int) -> list[dict]:
        obj = self.__get_obj(id)
        if not isinstance(obj.parent, int):
            return []
        result = []
        while isinstance(obj.parent, int):
            parent = self.__get_obj(obj.parent)
            result.append(self.items[parent.index])
            obj = parent
        
        return result