#include "Vector.h"
#include <iostream>

template<class T>
Vector<T>::Vector(int capacity) {
    _size = 0;
    _capacity = _DetermineCapacity(capacity);
    _data = std::unique_ptr<T[]>(new T[_capacity]);
}

template<class T>
Vector<T>::Vector(const Vector<T> &other) {
    _size = other.GetSize();
    _capacity = other.GetCapacity();
    
    std::unique_ptr<T[]> data(new T[_capacity]);
    for(int i = 0; i < _size; i++) {
        data[i] = other.GetValueAt(i);
    }
    
    _data = std::move(data);
}

template<class T>
Vector<T>::~Vector() {}

template<class T>
int Vector<T>::GetSize() const {
    return _size;
}

template<class T>
int Vector<T>::GetCapacity() const {
    return _capacity;
}

template<class T>
T Vector<T>::GetValueAt(int index) const {
    if (index < 0 || index >= _size) {
        std::cout << "Error: index " << index << " out of range.";
        exit(EXIT_FAILURE);
    }
    
    return _data[index];
}

template<class T>
bool Vector<T>::IsEmpty() const {
    return _size == 0;
}

template<class T>
void Vector<T>::Push(T newItem) {
    //_Resize(_size + 1);
    //_data[_size - 1] = newItem;
    Insert(newItem, _size);
}

// 0 1 2 3 4 5
// 1 3 2 6 2
// 1 3 7 2 6 2
template<class T>
void Vector<T>::Insert(T newItem, int at) {
    _Resize(_size + 1);
    
    // right shift
    for (int i = _size - 1; at < i; i--) {
        _data[i] = _data[i-1];
    }
    _data[at] = newItem;
}


template<class T>
void Vector<T>::Prepend(T newItem) {
    Insert(newItem, 0);
}

// 0 1 2 3 4
// 1 3 2 6 2
// 1 3 6 2
template<class T>
void Vector<T>::Delete(int at) {
    // shift left
    for (int i = at; i < _size - 1; i++) {
        _data[i] = _data[i+1];
    }
    
    // resize after shift to prevent shirnk the last value
    _Resize(_size - 1, true);
}

template<class T>
T Vector<T>::Pop() {
    if (_size == 0) {
        std::cout << "Nothing to pop." << std::endl;
        exit(EXIT_FAILURE);
    }
    auto element = _data[_size - 1];
    Delete(_size - 1);
    
    return element;
}

template<class T>
int Vector<T>::Find(T item) {
    int i = 0;
    for(; i < _size; i++) {
        if (_data[i] == item) {
            break;
        }
    }
    
    return i == _size ? -1 : i;
}

template<class T>
void Vector<T>::Remove(T item) {
    int index = Find(item);
    if (index != -1) {
        Delete(index);
    }
}


// change the size of vector
// and when size is full or has too many empty slots, adjust the capcaity
template<class T>
void Vector<T>::_Resize(int size, bool needShrink) {
    
    int realCapacity = _capacity;
    if (size == _capacity) {
        realCapacity *= GROWTH_FACTOR;
    }
    else if (
             needShrink &&
             size < _capacity &&
             MIN_CAPACITY < _capacity &&
             size <= _capacity / SHRINK_FACTOR
             ) {
        realCapacity /= GROWTH_FACTOR;
    }
    
    if (realCapacity != _capacity) {
        std::unique_ptr<T[]> newData(new T[realCapacity]);
        const int MIN_SIZE = _size < size ? _size : size;
        for (int i = 0; i < MIN_SIZE; i++) {
            newData[i] = _data[i];
        }
        _data = std::move(newData);
        _capacity = realCapacity;
    }
    
    _size = size;
}

template<class T>
int Vector<T>::_DetermineCapacity(int capacity) const {
    int realCapacity = MIN_CAPACITY;
    
    while (realCapacity <= capacity) {
        realCapacity *= GROWTH_FACTOR;
    }
    return realCapacity;
}
