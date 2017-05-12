//
//  main.cpp
//  Vector
//
//  Created by Lauren on 2017/5/8.
//  Copyright © 2017年 Lauren. All rights reserved.
//

#include <iostream>
#include "Vector.cpp"

int main(int argc, const char * argv[]) {
    // insert code here...
//    std::cout << "Hello, World!\n";
    
    Vector<int> vect(8);
    for(int i = 0; i < 17; i++) {
        vect.Push(i);
    }
    std::cout << vect.GetSize() << std::endl;
    std::cout << vect.GetCapacity() << std::endl;
    
//    vect.Delete(1);
//    for (int i = 0; i < vect.GetSize(); i++) {
//        std::cout << vect.GetValueAt(i) << std::endl;
//    }
    
    for(int i = 0; i < 17; i++) {
        vect.Pop();
    }
    std::cout << vect.GetSize() << std::endl;
    std::cout << vect.GetCapacity() << std::endl;
    
    return 0;
}
