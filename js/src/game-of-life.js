export class GameOfLife {
    constructor(seed) {
        this.current_generation = seed ? seed : this.createDefault();
    }

    createDefault() {
        return [
            [false, false, false],
            [false, false, false],
            [false, false, false]
        ]
    }
}