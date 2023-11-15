from typing import List

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return self.all()

    def __repr__(self):
        return f"{self.val} -> {self.next.val if self.next else []}"

    def all(self):
        curr = self
        text = ""
        while curr:
            text += f"{curr.val}"
            if curr.next:
                text += " -> "
            curr = curr.next
        return text


class AnimalShelf:

    def __init__(self):
        self.catsHead = None
        self.catsTail = None
        
        self.dogsHead = None
        self.dogsTail = None
        
        self.orderMap = {}
        self.timeId = 0
        self.maxCount = 20000


    def enqueue(self, animal: List[int]) -> None:
        self.timeId += 1
        if animal[1] == 0:
            self.enqueueCat(animal)
        elif animal[1] == 1:
            self.enqueueDog(animal)


    def dequeueAny(self) -> List[int]:
        if self.catsHead is None and self.dogsHead is None:
            return [-1, -1]
        elif self.catsHead is None:
            return self.dequeueDog()
        elif self.dogsHead is None:
            return self.dequeueCat()

        catTime = self.orderMap.get(self.catsHead.val[0], self.maxCount)
        dogTime = self.orderMap.get(self.dogsHead.val[0], self.maxCount)

        if catTime < dogTime:
            return self.dequeueCat()
        else:
            return self.dequeueDog()


    def dequeueDog(self) -> List[int]:
        if self.dogsHead is None:
            return [-1, -1]
        
        node = self.dogsHead
        del self.orderMap[node.val[0]]
        
        self.dogsHead = self.dogsHead.next
        if self.dogsHead is None:
            self.dogsTail = None
        
        return node.val


    def dequeueCat(self) -> List[int]:
        if self.catsHead is None:
            return [-1, -1]
        
        node = self.catsHead
        del self.orderMap[node.val[0]]
        
        self.catsHead = self.catsHead.next
        if self.catsHead is None:
            self.catsTail = None
        
        return node.val


    def enqueueCat(self, animal: List[int]) -> None:
        node = ListNode(animal)
        self.orderMap[node.val[0]] = self.timeId
        
        if self.catsHead is None:
            self.catsHead = node
        
        if self.catsTail is None:
            self.catsTail = node
        else:
            self.catsTail.next = node
            self.catsTail = node


    def enqueueDog(self, animal: List[int]) -> None:
        node = ListNode(animal)
        self.orderMap[node.val[0]] = self.timeId
        
        if self.dogsHead is None:
            self.dogsHead = node
        
        if self.dogsTail is None:
            self.dogsTail = node
        else:
            self.dogsTail.next = node
            self.dogsTail = node
        

# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()