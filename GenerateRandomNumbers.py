class GRN:
    seed = 0
    seed_length = 0

    # метод генерации числа методом серединных квадратов
    @staticmethod
    def __generate_next():
        squared_seed = str(GRN.seed ** 2)

        while len(squared_seed) < GRN.seed_length * 2:
            squared_seed = '0' + squared_seed

        start_index = (GRN.seed_length // 2)
        end_index = start_index + GRN.seed_length
        GRN.seed = int(squared_seed[start_index:end_index])
        return GRN.seed

    # Метод генерации списка из n случайных чисел. Начальное число и n передаются в качестве вх. параметра
    @staticmethod
    def get_random_numbers(seed: int, n: int):
        GRN.seed = seed
        GRN.seed_length = len(str(GRN.seed))
        list_numbers = []
        for i in range(n):
            list_numbers.append(GRN.__generate_next())
        return list_numbers
