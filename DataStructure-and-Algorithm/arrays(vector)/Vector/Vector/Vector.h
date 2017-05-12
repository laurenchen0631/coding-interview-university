//
//  Vector.h
//  Vector
//
//  Created by Lauren on 2017/5/8.
//  Copyright © 2017年 Lauren. All rights reserved.
//

#ifndef Vector_h
#define Vector_h

#include <memory>

template<class T>
class Vector {
public:
    Vector<T>(int capacity);
    Vector<T>(const Vector<T> &other);
    ~Vector<T>();
    
    // Access Method
    int GetSize() const;
    int GetCapacity() const;
    T GetValueAt(int index) const;
    
    // Operation Method
    bool IsEmpty() const;
    void Push(T newItem);
    void Insert(T newItem, int at);
    void Prepend(T newItem);
    T Pop();
    void Delete(int at);
    void Remove(T item);
    int Find(T item);
    
private:
    int _size;
    int _capacity;
    const int MIN_CAPACITY = 16;
    const int GROWTH_FACTOR = 2;
    const int SHRINK_FACTOR = 4;
    
    std::unique_ptr<T[]> _data;
    
    // Private Operation Method
    void _Resize(int size, bool needShrink = false);
    // void _IncreaseCapacity();
    // void _ShrinkCapacity();
    int _DetermineCapacity(int capacity) const;
};


#endif /* Vector_h */
