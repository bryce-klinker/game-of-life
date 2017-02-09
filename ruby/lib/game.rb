class Game
  attr_reader :current_generation


  def initialize(size: nil, seed: nil)
    @current_generation = create_dead_generation(size) unless size.nil?
    @current_generation = seed unless seed.nil?
  end

  def size
    @current_generation.size
  end

  def next_generation
    next_gen = create_dead_generation(size)
    (0..size - 1).each { |row_index|
      (0..size - 1).each { |column_index|
        next_gen[row_index][column_index] = should_live_or_revive(row_index, column_index)
      }
    }
    next_gen
  end

  private
  def should_live_or_revive(row_index, column_index)
    return should_revive(row_index, column_index) if is_dead(row_index, column_index)
    should_live(row_index, column_index)
  end

  def should_live(row_index, column_index)
    living_neighbors = count_living_neighbors(row_index, column_index)
    return false if living_neighbors < 2
    return false if living_neighbors > 3
    true
  end

  def should_revive(row_index, column_index)
    living_neighbors = count_living_neighbors(row_index, column_index)
    living_neighbors == 3
  end

  def count_living_neighbors(row_index, column_index)
    living_neighbors = 0
    living_neighbors += 1 if is_upper_left_alive(row_index, column_index)
    living_neighbors += 1 if is_upper_alive(row_index, column_index)
    living_neighbors += 1 if is_upper_right_alive(row_index, column_index)

    living_neighbors += 1 if is_left_alive(row_index, column_index)
    living_neighbors += 1 if is_right_alive(row_index, column_index)

    living_neighbors += 1 if is_lower_left_alive(row_index, column_index)
    living_neighbors += 1 if is_lower_alive(row_index, column_index)
    living_neighbors += 1 if is_lower_right_alive(row_index, column_index)

    living_neighbors
  end

  def is_lower_right_alive(row_index, column_index)
    is_living(row_index + 1, column_index + 1)
  end

  def is_lower_alive(row_index, column_index)
    is_living(row_index + 1, column_index)
  end

  def is_lower_left_alive(row_index, column_index)
    is_living(row_index + 1, column_index - 1)
  end

  def is_right_alive(row_index, column_index)
    is_living(row_index, column_index + 1)
  end

  def is_left_alive(row_index, column_index)
    is_living(row_index, column_index - 1)
  end

  def is_upper_right_alive(row_index, column_index)
    is_living(row_index - 1, column_index + 1)
  end

  def is_upper_alive(row_index, column_index)
    is_living(row_index - 1, column_index)
  end

  def is_upper_left_alive(row_index, column_index)
    is_living(row_index - 1, column_index - 1)
  end

  def is_living(row_index, column_index)
    is_in_generation(row_index, column_index) && @current_generation[row_index][column_index]
  end

  def is_dead(row_index, column_index)
    not @current_generation[row_index][column_index]
  end

  def is_in_generation(row_index, column_index)
    row_index > -1 && row_index < size && column_index > -1 && column_index < size
  end

  def create_dead_generation(size)
    Array.new(size, Array.new(size, false))
  end
end