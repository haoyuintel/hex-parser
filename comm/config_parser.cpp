#include "includes/defines.h"
#include <fstream>
#include <map>
using namespace std;

class config_parser
{
private:
    /* data */
public:
    config_parser(const string& path);
    ~config_parser();
    bool load();
    string get(string section, string k);

private:
    string file;
    ifstream config;
    map<string, map<string, string>> data;
};

config_parser::config_parser(const string& path) : file(path) {}

config_parser::~config_parser() {}

bool config_parser::load() {
    config.open(file, ios::in);
    if (!config.is_open()) 
    {
        cerr << "config not open" << endl;
        return false;
    }

    string line, section;
    while (getline(config, line))
    {
        if (line.empty() || line[0] == ';' || line[0] == '#')
        {
            continue;
        }
        line.erase(0, line.find_first_not_of("\t"));
        line.erase(line.find_last_not_of("\t") + 1);

        if (line[0] == '[' && line.back() == ']')
        {
            section = line.substr(1, line.size() - 2);
            continue;
        }
        
        u32 pos = line.find("=");
        if (pos != string::npos) {
            string k = line.substr(0, pos);
            string v = line.substr(pos + 1);
            k.erase(0, k.find_first_not_of("\t"));
            k.erase(k.find_last_not_of("\t") + 1);
            v.erase(0, v.find_first_not_of("\t"));
            v.erase(v.find_last_not_of("\t") + 1);
            data[section][k] = v;
        }

    }
    
    config.close();
    return true;
}

string config_parser::get(string section, string k) {
    auto item = data.find(section);
    if (item != data.end()) {
        auto v = item->second.find(k);
        if (v != item->second.end())
        {
            return v->second;
        }
    }
    return "";
}
