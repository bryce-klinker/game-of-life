from unittest import TestCase
from nose.tools import assert_equals, assert_false, assert_true

from game_of_life.game import Game


class GameOfLifeTest(TestCase):

    @staticmethod
    def test_game_should_have_empty_generation():
        game_of_life = Game()

        assert_equals(game_of_life.current_generation, [])

    def test_game_should_have_all_dead_generation(self):
        game = Game(size=3)

        self.__assert_dead_generation(game.current_generation)

    @staticmethod
    def test_game_should_seed_generation():
        seed = [
            [True, False],
            [False, True]
        ]
        game = Game(seed=seed)

        assert_true(game.current_generation[0][0])
        assert_true(game.current_generation[1][1])

        assert_false(game.current_generation[0][1])
        assert_false(game.current_generation[1][0])

    @staticmethod
    def test_next_generation_should_kill_cells_with_fewer_than_two_live_neighbors():
        seed = [
            [True, False],
            [False, False]
        ]
        game = Game(seed=seed)
        generation = game.next_generation()

        assert_false(generation[0][0])

    @staticmethod
    def test_game_next_generation_should_revive_any_cell_with_exactly_three_live_neighbors():
        seed = [
            [False, True],
            [True, True]
        ]

        game = Game(seed=seed)
        generation = game.next_generation()

        assert_true(generation[0][0])

    @staticmethod
    def test_game_next_generation_should_kill_any_cell_with_fewer_than_two_living_neighbors():
        seed = [
            [True, False],
            [True, False]
        ]

        game = Game(seed=seed)
        generation = game.next_generation()

        assert_false(generation[0][0])

    @staticmethod
    def test_game_next_generation_should_kill_any_cell_with_more_than_three_living_neighbors():
        seed = [
            [True, True, True],
            [True, True, False],
            [False, False, False]
        ]

        game = Game(seed=seed)
        generation = game.next_generation()
        assert_false(generation[0][1])

    @staticmethod
    def test_game_next_generation_should_keep_living_cell_with_two_living_neighbors():
        seed = [
            [True, False],
            [True, True]
        ]

        game = Game(seed=seed)
        generation = game.next_generation()
        assert_true(generation[0][0])

    @staticmethod
    def test_game_next_generation_should_keep_living_cell_with_three_living_neighbors():
        seed = [
            [True, True],
            [True, True]
        ]

        game = Game(seed=seed)
        generation = game.next_generation()
        assert_true(generation[0][0])

    @staticmethod
    def __assert_dead_generation(generation):
        assert_equals(len(generation), 3)
        assert_equals(len(generation[0]), 3)
        assert_equals(len(generation[1]), 3)
        assert_equals(len(generation[2]), 3)
        for row in generation:
            for y in row:
                assert_false(y)
