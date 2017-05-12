from linked_list import LinkedList

list = LinkedList()
list.push_front(5)
list.push_front(4)
list.push_front(3)
list.push_back(6)
list.push_back(7)
list.push_front(2)
list.push_front(1)
print(list)

list.pop_back()
print(list)

list.pop_front()
print(list)

list.reverse()
print(list)
list.reverse()
print(list)

list.insert(0, -1)
list.insert(list.size(), 100)
print(list)
list.insert(3, 0)
print(list)
print(list.size())
print(list.front())
print(list.back())

list.erase(3)
list.erase(0)
list.erase(list.size() - 1)
print(list)
print(list.front())
print(list.back())

print(list.value_at(0))
print(list.value_at(1))
print(list.value_at(2))
print(list.value_at(3))
print(list.value_at(4))

print(list.value_n_from_end(1))
print(list.value_n_from_end(2))
print(list.value_n_from_end(3))
print(list.value_n_from_end(4))
print(list.value_n_from_end(5))
print(list)

list.remove_value(2)
print(list)
print(list.front())
print(list.back())
print(list.size())

list.remove_value(6)
print(list)
print(list.front())
print(list.back())
print(list.size())

list.remove_value(4)
print(list)
