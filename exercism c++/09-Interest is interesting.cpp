double interest_rate(double balance) {
    if (balance < 0) {
        return 3.213;
    }
    else if (balance >= 0 && balance < 1000) {
        return 0.5;
    }
    else if (balance >= 1000 && balance < 5000) {
        return 1.621;
    }else {
        return 2.475;
    }
}

double yearly_interest(double balance) {
    double rate = interest_rate(balance);
    return balance * (rate / 100);
}

double annual_balance_update(double balance) {
    double end_year_balance{yearly_interest(balance)};
    return end_year_balance + balance;
}

int years_until_desired_balance(double balance, double target_balance) {
    int years{0};
    while (balance < target_balance) {
        ++years;
        balance += yearly_interest(balance);
    }
    return years;
}