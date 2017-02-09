import { GameOfLife } from './game-of-life';

describe('Game of Life', () => {
    it('should have dead current_generation', () => {
        const game = new GameOfLife();

        expect(game.current_generation).toEqual([
            [false, false, false],
            [false, false, false],
            [false, false, false]
        ])
    });

    it('should have the seeded generation', () => {
        const seed = [
            [false, false],
            [false, false]
        ];
        const game = new GameOfLife(seed);

        expect(game.current_generation).toEqual(seed)
    })
});