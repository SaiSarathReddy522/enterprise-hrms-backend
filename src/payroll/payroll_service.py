def calculate_gross_salary(basic_salary, hra, allowance):
    return basic_salary + hra + allowance


def calculate_net_salary(gross_salary, deductions):
    return gross_salary - deductions


def calculate_salary(basic_salary, hra, allowance, deductions=0):
    gross_salary = calculate_gross_salary(
        basic_salary,
        hra,
        allowance
    )

    net_salary = calculate_net_salary(
        gross_salary,
        deductions
    )

    return {
        "gross_salary": gross_salary,
        "net_salary": net_salary
    }