require 'rspec'
require_relative '../lib/game.rb'

describe 'Game of life' do

  it 'should have all dead generation' do
    game = Game.new(size: 3)
    expect(game.current_generation).to eql [
     [false, false, false],
     [false, false, false],
     [false, false, false]
   ]
  end

  it 'should have generation of specified size' do
    game = Game.new(size: 4)
    expect(game.current_generation).to eql [
      [false, false, false, false],
      [false, false, false, false],
      [false, false, false, false],
      [false, false, false, false]
    ]
  end

  it 'should seed generation from seed' do
    seed = [
        [false, true],
        [true, false]
    ]
    game = Game.new(seed: seed)
    expect(game.current_generation).to eql seed
  end

  it 'should kill cells with fewer than two live neighbors' do
    seed = [
        [ true, false],
        [ false, false]
    ]

    game = Game.new(seed: seed)
    next_generation = game.next_generation
    expect(next_generation).to eql [
        [false, false],
        [false, false]
    ]
  end

  it 'should kill cells with more than three live neighbors' do
    seed = [
        [false, true, false],
        [true, true, true],
        [false, true, false]
    ]

    game = Game.new(seed: seed)
    next_generation = game.next_generation
    expect(next_generation[1][1]).to eql false
  end

  it 'should keep living cells if two living neighbors' do
    seed = [
        [true, true],
        [true, false]
    ]

    game = Game.new(seed: seed)
    next_generation = game.next_generation
    expect(next_generation[0][0]).to eql true
  end
end