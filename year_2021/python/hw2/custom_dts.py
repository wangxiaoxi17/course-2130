from __future__ import annotations

from typing import List, Any


class CycledList:
    """
    Реализуйте список фиксированой длины, в котором новые элементы перезаписываются

    ```
    cycled_list = CycledList(5)
    cycled_list.append(1)
    cycled_list.append(2)
    cycled_list.append(3)
    cycled_list.append(4)
    cycled_list.append(5)
    cycled_list.append(6)
    ```

    Expected Output:
    ```
    [6, 2, 3, 4, 5]
    ```
    """
    def __init__(self, size: int):
        self._data = [None]*size
        self.size = size
        self.now = 0
        self.cnt = 0

    def append(self, item):
        self._data[self.cnt] = item
        self.cnt = (self.cnt + 1) % self.size
        if self.now != self.size:
            self.now = self.now + 
        pass


class Fraction:
    """
    Написать класс чисел с бесконечной точностью. Дроби.
    Определите следующие операции:
    1. a / b
    2. a + b
    3. a * b
    4. a - b

    Вы можете найти больше здесь https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types

    В каждый момент времени дробь должна быть правильной

    """
    def gcd(self, a, b):
        if a % b == 0:
            return b
        else:
            return self.gcd(b, a % b)

    
    def __init__(self, nominator, denominator):
        g = self.gcd(nominator, denominator)
        self.nominator = nominator / g
        self.denominator = denominator / g

    def __truediv__(self, other):
        return Fraction(self.nominator * other.denominator, self.denominator * other.nominator)

    def __add__(self, other):
        a = self.nominator * other.denominator + self.denominator * other.nominator;
        b = self.denominator * other.denominator
        return Fraction(a, b)

    def __mul__(self, other):
        return Fraction(self.nominator * other.nominator, self.denominator * other.denominator)

    def __sub__(self, other: Fraction) -> Fraction:
        a = self.nominator * other.denominator - self.denominator * other.nominator;
        b = self.denominator * other.denominator
        return Fraction(a, b)

    def __repr__(self):
        return f'{self.nominator}/{self.denominator}'
    
    class Node:
    def __init__(self, key):
        self.key = key
        self.val = 1
        self.nxt = None

class MyCounter:
    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter

    Достаточно поддерживать только два метода

    """

    
    def __init__(self, iterable=None):
        self._data = None
        self.len = 1021
        self.now = 0
        self._data = [None] * self.len
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def _hash(self, key):
        return hash(key) % self.len

    def append(self, item):
        pos = self._hash(item)
        cur = self._data[pos]
        while cur is not None:
            if cur.key == item:
                cur.val = cur.val + 1
                return
            cur = cur.nxt
        node = Node(item)
        node.nxt = self._data[pos]
        self._data[pos] = node

    def remove(self, item):
        pos = self._hash(item)
        cur = self._data[pos]
        if cur is not None:
            if cur.key == item:
                cur.val = cur.val - 1
                if cur.val == 0:
                    self._data[pos] = cur.nxt
                    return
        last = cur
        cur = cur.nxt
        while cur is not None:
            if cur.key == item:
                cur.val = cur.val - 1
                if cur.val == 0:
                    self._data[pos] = cur.nxt
                return
            last = cur
            cur = cur.nxt

    def __getitem__(self, item):  # test
        pos = self._hash(item)
        cur = self._data[pos]
        while cur is not None:
            if cur.key == item:
                return cur.val
            cur = cur.nxt
        return 0


class Figure:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        return None

    def square(self):
        return None

    def __repr__(self):
        return f'Figure({self.name})'


class Square(Figure):
    """
   Implement the square class and two methods for it
    """

    def __init__(self, name, len):
        self.len = len
        Figure.__init__(self, name)

    def perimeter(self):
        return self.len

    def square(self):
        return self.len * self.len

    pass


class Container:
    def __init__(self, data):
        self.data = data

    def __delitem__(self, key):
        del self.data[key]

    def __getitem__(self, item):
        return self.data[item]

    def append(self, item):
        self.data.append(item)


class PersistentList:
    """
    Реализуйте список где передаваемый список записывается в файл
    Любая операция удаления/добавления должна изменять файл

    Формат файла - json
    """
    def __init__(self, iterable: List[Any], path_to_file: str):
        self.path = path_to_file
        with open(self.path, 'r', encoding='utf8') as fp:
            self.list = json.load(fp)
        if iterable is not None:
            for item in iterable:
                self.list.append(item)
        with open('test.json', 'w', encoding='utf8') as fp:
            json.dump(self.list, fp, ensure_ascii=False)

   def append(self, item) -> None:
        """add item to list"""
        self.list.append(item)
        with open('test.json', 'w', encoding='utf8') as fp:
            json.dump(self.list, fp, ensure_ascii=False)
            
  
    def __getitem__(self, index):
        """ return item by index """
        return self.list[index]

    def delete(self, index: int) -> None:
        """ delete item by index

            if index greater then length of list back to start and repeat
                [1, 2, 3] -> delete(4) -> [1, 3]

            if index lower then delete from end of list

        """
        length = len(self.list)
        index = index % length
        del self.list[index]
        with open('test.json', 'w', encoding='utf8') as fp:
            json.dump(self.list, fp, ensure_ascii=False)

    def __repr__(self):
        return 'PersistentList '+self.list.__str__()
