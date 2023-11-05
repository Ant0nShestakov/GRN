import GenerateRandomNumbers
import ValidityCheck

if __name__ == '__main__':
    seed = 1234
    count = 10000
    print(f"seed: {seed}\ncount: {count}")
    list_number = GenerateRandomNumbers.GRN.get_random_numbers(seed, count)
    validChecker = ValidityCheck.ValidityChecker(list_number)
    print("--------------------------------------------------")
    print(f"Проверка на стахостичность: {validChecker.check_on_stochasticity(0.05)}")
    print("--------------------------------------------------")
    print(f"Проверка на мат. ожидание: {validChecker.check_on_mathematical_expectation()}")
    print("--------------------------------------------------")
    print(f"Проверка на дисперсию: {validChecker.check_on_dispersion()}")
    print("--------------------------------------------------")
    print(f"Проверка на среднеквадратическое отклонение: {validChecker.check_on_standard_deviation()}")
    print("--------------------------------------------------")
    print(f"Проверка на частотность: {validChecker.check_on_count_interval_and__digit_frequency()}")
    print("--------------------------------------------------")
    print(f"Проверка на серии из одинаковых цифр: {validChecker.check_on_series_identical_digits()}")
    print("--------------------------------------------------")
