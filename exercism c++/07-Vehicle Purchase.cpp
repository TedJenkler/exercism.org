#include <iostream>
#include <string>

namespace vehicle_purchase {

    bool needs_license(std::string kind){
        return kind == "car" || kind == "truck";
    }

    std::string choose_vehicle(std::string option1, std::string option2) {
        if (option1 > option2) {
            return option2 + " is clearly the better choice.";
        } else {
            return option1 + " is clearly the better choice.";
        }
    }

    double calculate_resell_price(double original_price, double age) {
        if (age < 3.0) {
            return static_cast<int>(original_price * 0.8);
        }
        else if(age >= 3 and age < 10) {
            return static_cast<int>(original_price * 0.7);
        }else {
            return static_cast<int>(original_price * 0.5);
        }
    }

}




#pragma once

#include <string>

namespace vehicle_purchase {

    bool needs_license(std::string kind);
    std::string choose_vehicle(std::string option1, std::string option2);
    double calculate_resell_price(double original_price, double age);

} 