#include <iostream>
#include "config_parser.cpp"
using namespace std;

int main() {
    auto config = config_parser("./config.ini");
    if (config.load())
    {
        config.get("server", "host");
    } else {
        cout << "false" << endl;
    }
    
}
