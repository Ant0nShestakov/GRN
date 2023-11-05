import math


class ValidityChecker:
    __list_numbers = None
    __count = 0

    def __init__(self, list_numbers: list):
        self.__list_numbers = list_numbers
        self.__count = len(list_numbers)

    def check_on_stochasticity(self, alpha):
        theta = 1 / self.__count
        x = sum(math.comb(i, self.__count) * theta
                ** i * (1 - theta) ** (self.__count - 1) for i in range(self.__count))
        print(f"stochasticity: {x}")
        return x < alpha

    def __mathematical_expectation(self):
        theta = 1 / self.__count
        return sum((self.__list_numbers[i] / self.__count) * theta for i in range(self.__count))

    def check_on_mathematical_expectation(self):
        print(f"math. expectation: {self.__mathematical_expectation()}")
        return round(self.__mathematical_expectation(), 1) == 0.5

    def __dispersion(self):
        theta = 1 / self.__count
        mq = self.__mathematical_expectation() ** 2
        m2 = sum((self.__list_numbers[i] / self.__count) ** 2 * theta for i in range(self.__count))
        return m2 - mq

    def check_on_dispersion(self):
        print(f"dispersion: {self.__dispersion()}")
        return round(self.__dispersion(), 2) == 0.08

    def __standard_deviation(self):
        return self.__dispersion() ** (1 / 2)

    def check_on_standard_deviation(self):
        print(f"std deviation: {self.__standard_deviation()}")
        return round(self.__standard_deviation(), 2) == 0.29

    def __count_interval(self):
        i1 = round(self.__mathematical_expectation() - self.__standard_deviation(), 5)
        i2 = round(self.__mathematical_expectation() + self.__standard_deviation(), 5)
        count_deviation = 0  # Счетчик для интервала отклонения относительно математического ожидания
        count_less = 0  # Счетчик для интервала меньше середины интервала от 0 до 1
        count_greater = 0  # Счетчик для интервала больше середины интервала от 0 до 1
        for num_item in self.__list_numbers:
            num = num_item / self.__count  # Приводим значенеие к диапазону от 0 до 1
            if i1 <= num <= i2:
                count_deviation = count_deviation + 1
            if num >= 0.5:
                count_greater = count_greater + 1
            if num < 0.5:
                count_less = count_less + 1
        return (round(count_deviation / self.__count * 100, 5),
                round(count_less / self.__count * 100, 5), round(count_greater / self.__count * 100, 5))

    def __calc_interval(self):
        me = self.__mathematical_expectation()
        sd = self.__standard_deviation()
        return round((me + sd) - (me - sd), 2)

    def __digit_frequency(self):
        digit_count = {}
        for number in self.__list_numbers:
            digits = str(number)
            for digit in digits:
                digit_count[digit] = digit_count.get(digit, 0) + 1
        sum_xi = 0
        total_count = sum(digit_count.values())

        for digit, count in digit_count.items():
            frequency = count / total_count
            p = 0.1
            sum_xi += (frequency - p / p) ** 2
        return sum_xi

    def __check_on_digit_frequency(self):
        return self.__digit_frequency() > 14.68

    def check_on_count_interval_and__digit_frequency(self):
        intervals = self.__count_interval()
        print(f"calc interval: {intervals[0]};\ninterval 0-5: {intervals[1]};\ninterval 0.5-1: {intervals[2]};")
        print(f"digit frequency: {self.__digit_frequency()}")
        return (round(intervals[0]) == round(self.__calc_interval() * 100)
                and round(intervals[1]) == 50 and round(intervals[2]) == 50) and self.__check_on_digit_frequency()

    def __series_identical_digits(self):
        digit_count = {}

        series_count = 0
        last_digit = None
        for number in self.__list_numbers:
            digits = str(number)
            for digit in digits:
                if digit == last_digit:
                    series_count += 1
                else:
                    series_count = 1
                last_digit = digit
            digit_count[series_count] = digit_count.get(series_count, 0) + 1

        digit_probability = {}
        sum_xi = 0
        for degree in digit_count:
            digit_probability[degree] = digit_count[degree] / self.__count
            sum_xi += (digit_probability[degree] - 9 * 10 ** (-degree) / 9 * 10 ** (-degree)) ** 2
        return sum_xi

    def check_on_series_identical_digits(self):
        print(f"ident. digit frequency: {self.__series_identical_digits()}")
        return self.__series_identical_digits() < 0.58
