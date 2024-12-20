#include <cmath>

double daily_rate(double hourly_rate) {
    return hourly_rate * 8.0;
}

double apply_discount(double before_discount, double discount) {
    return before_discount * (1.0 - (discount / 100.0));
}

int monthly_rate(double hourly_rate, double discount) {
    double monthly_rate = daily_rate(hourly_rate) * 22.0;
    double discounted_rate = monthly_rate * (1 - (discount / 100.0));
    return static_cast<int>(std::ceil(discounted_rate));
}

int days_in_budget(int budget, double hourly_rate, double discount) {
    double day_rate = daily_rate(hourly_rate);
    double discounted_day_rate = day_rate * (1.0 - discount / 100.0);
    int budget_in_days = static_cast<int>(budget / discounted_day_rate);
    return budget_in_days;
}