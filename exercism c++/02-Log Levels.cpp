#include <string>

namespace log_line {
    std::string message(std::string line) {
        size_t colonPos = line.find(":");
        return line.substr(colonPos + 2);
    }

    std::string log_level(std::string line) {
        size_t colonPos = line.find(":");
        return line.substr(1, colonPos - 2);
    }

    std::string reformat(std::string line) {
        size_t colonPos = line.find(":");
        std::string part1 = line.substr(1, colonPos - 2);
        std::string part2 = line.substr(colonPos + 2);
        return part2 + " (" + part1 + ")";
    }
}