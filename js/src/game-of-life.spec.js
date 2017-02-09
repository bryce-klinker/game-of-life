import { GameOfLife } from './game-of-life';

describe('Game of Life', () => {
    it('should have dead generation', () => {
        var game = new GameOfLife();
        expect(game.generation).toEqual([
            [false, false, false],
            [false, false, false],
            [false, false, false]
        ])
    })
});