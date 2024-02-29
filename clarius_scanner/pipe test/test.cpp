#include <iostream>
#include <windows.h>   
#include <string>

#define PRINT(x) std::cout << (x) << std::endl

int main() {
    std::string message;
    std::getline(std::cin, message);
    if(message == "start"){
        Sleep(5000);
        PRINT("5");
    }
    
}
