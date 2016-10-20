class Game():
    def __init__(self, size=0, seed=None):
        self.size = len(seed) if seed is not None else size
        self.current_generation = self.__create_dead_generation()

        if seed is not None:
            self.__seed_board(seed)

    def next_generation(self):
        next_generation = self.__create_dead_generation()
        for row_index in range(self.size):
            for column_index in range(self.size):
                next_generation[row_index][column_index] = self.__get_next_state(row_index, column_index)
        return next_generation

    def __count_living_neighbors(self, row_index, column_index):
        living_count = 0
        living_count += 1 if self.__is_upper_left_alive(row_index, column_index) else 0
        living_count += 1 if self.__is_upper_alive(row_index, column_index) else 0
        living_count += 1 if self.__is_upper_right_alive(row_index, column_index) else 0

        living_count += 1 if self.__is_left_alive(row_index, column_index) else 0
        living_count += 1 if self.__is_right_alive(row_index, column_index) else 0

        living_count += 1 if self.__is_lower_left_alive(row_index, column_index) else 0
        living_count += 1 if self.__is_lower_alive(row_index, column_index) else 0
        living_count += 1 if self.__is_lower_right_alive(row_index, column_index) else 0
        return living_count

    def __is_upper_left_alive(self, row_index, column_index):
        return self.__is_alive(row_index - 1, column_index - 1)

    def __is_upper_alive(self, row_index, column_index):
        return self.__is_alive(row_index - 1, column_index)

    def __is_upper_right_alive(self, row_index, column_index):
        return self.__is_alive(row_index - 1, column_index + 1)

    def __is_left_alive(self, row_index, column_index):
        return self.__is_alive(row_index, column_index - 1)

    def __is_right_alive(self, row_index, column_index):
        return self.__is_alive(row_index, column_index + 1)

    def __is_lower_left_alive(self, row_index, column_index):
        return self.__is_alive(row_index + 1, column_index - 1)

    def __is_lower_alive(self, row_index, column_index):
        return self.__is_alive(row_index + 1, column_index)

    def __is_lower_right_alive(self, row_index, column_index):
        return self.__is_alive(row_index + 1, column_index + 1)

    def __is_alive(self, row_index, column_index):
        return -1 < row_index < self.size \
               and -1 < column_index < self.size \
               and self.current_generation[row_index][column_index]

    def __seed_board(self, seed):
        for row_index in range(len(seed)):
            for column_index in range(len(seed[row_index])):
                self.current_generation[row_index][column_index] = seed[row_index][column_index]

    def __create_dead_generation(self):
        return [[False for i in range(self.size)] for i in range(self.size)]

    def __get_next_state(self, row_index, column_index):
        living_neighbors = self.__count_living_neighbors(row_index, column_index)

        if self.__is_alive(row_index, column_index):
            return 2 <= living_neighbors < 4

        return living_neighbors == 3
