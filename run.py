from random import randint


class Door(object):
    # Represents a door with either a car or goat behind it.

    def __init__(self, has_car):
        self.has_car = has_car

    def whats_behind(self):
        # Returns a string representation of what's behind this door.
        return 'car' if self.has_car else 'goat'


def pick_random_door(num_doors):
    # Randomly selects a door, starting with index 0
    return randint(0, num_doors - 1)


def create_doors(num_doors=3):
    # Creates a number of doors with a car behind one, goats behind the others.
    doors = []
    car_index = pick_random_door(num_doors)
    for i in range(0, num_doors):
        doors.append(Door(car_index == i))

    return doors, car_index


def run_game(switch=False, num_doors=3):
    # Runs a single round of the game. If switch is true, the player switches from their initial guess. Otherwise they
    # stick with the door they originally selected. The host will always select one losing door. The round's outcome
    # is returned as true or false.
    assert(num_doors >= 3)  # Need at least three doors.

    # Create a set of doors.
    doors, car_at = create_doors(num_doors)

    # Let the player randomly select a door.
    player_choice = pick_random_door(num_doors)

    # The host opens a second door the player didn't select, and it must have a goat behind it. In this version of the
    # problem the host only opens one door. When increasing num_doors you may wish to alter the host's behavior to
    # open more than one losing door per round.
    host_choice = car_at
    while host_choice == player_choice or host_choice == car_at:
        host_choice = pick_random_door(num_doors)

    # Sanity check: Fail here if the host's selected door has a car behind it.
    assert(doors[host_choice].whats_behind() == 'goat')

    # If the player switches, they must choose a door not previously selected by themselves or the host.
    if switch:
        old_player_choice = player_choice
        player_choice = old_player_choice
        while player_choice == old_player_choice or player_choice == host_choice:
            player_choice = pick_random_door(num_doors)

    # Returns true if the player won a car, otherwise false.
    return doors[player_choice].whats_behind() == 'car'


def run_multiple_games(num_games=1, num_doors=3):
    # Runs one or more rounds of the Monty Hall game and prints a tally of the results at the end. For each round, both
    # a "stay" and a "switch" round are simulated. Set num_games to the number of rounds you wish to run.
    #
    # You may also change the number of doors with the num_doors argument. There will still be only one car available
    # with any number of doors, this feature is for those who find the problem more intuitive with more doors.

    assert(num_games >= 1)
    games_won_stayed = 0
    games_won_switched = 0
    for i in range(0, num_games):
        # Run without switching
        if run_game(False, num_doors=num_doors):
            games_won_stayed += 1

        # Run without switching
        if run_game(True, num_doors=num_doors):
            games_won_switched += 1

    # Print out a tally of the results.
    print('Games run: %d' % num_games)
    print('Games won stayed: %d' % games_won_stayed)
    print('Games won switched: %d' % games_won_switched)


# Run the game one or more times. Set num_games to the number of rounds. If you'd like to run with more than three
# doors, set num_doors to a greater value.
run_multiple_games(num_games=1000, num_doors=3)
