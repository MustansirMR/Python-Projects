from typing import Dict, List, Tuple


class AdventureGame:
    def __init__(self):
        self.game_map: [int, Tuple] = {
            1: (0, 0, 2, 0),
            2: (1, 0, 3, 5),
            3: (2, 0, 0, 0),
            4: (5, 0, 0, 9),
            5: (0, 2, 4, 0),
            6: (0, 0, 0, 0),
            7: (0, 0, 8, 0),
            8: (7, 0, 9, 0),
            9: (8, 4, 0, 0)
        }
        self.score = 50
        self.directions = ('north', 'west', 'south', 'east')
        self.room = 1
        self.direction = 0

    def play_game(self):
        print("""\
    You are in room 1 and facing north. Your job is to reach room 7
    with minimum possible moves. Your score starts at 50 which will be lowered
    for every move.
    Valid commands are the following:
    move: move to the next room if not facing a wall, cost 1 score;
    face <cardinal direction>: which way to face, cost 1 score; 
    describe: will describe the room, no score cost;
    quit: quit game.""")
        command: str = ''
        while True:
            self.perform_game_step(input('What do you do?: '))
            if self.room == 7:
                print(f'Congrats! You have reached room 7! Your score is {self.score}')
                exit(0)
            elif self.score == 0:
                print('You have failed to reach room 7. Better luck next time.')
                exit(0)

    def perform_game_step(self, cmd: str):
        if cmd.lower() == 'move':
            status = self.game_map[self.room][self.direction]
            if status == 0:
                print(f'You are facing a wall and cannot move. Maybe turn a little? Score now {self.score-1}')
            else:
                self.room = status
                print(f'You have moved to room {self.room}. Score now {self.score-1}')
            self.score -= 1
        elif cmd.lower() == 'describe':
            print(f'You are in room number {self.room} and facing {self.directions[self.direction]}. '
                  f'Score {self.score}')
        elif cmd.lower() == 'quit':
            print('Game quits.')
            exit(0)
        else:
            try:
                if 'face' in cmd.lower():
                    self.direction = self.directions.index(cmd.lower()[5:])
                    self.score -= 1
                    print(f'You are now facing {self.directions[self.direction]}. Score now {self.score}')
                else:
                    raise ValueError('Invalid command')
            except ValueError:
                self.score -= 1
                print(f'Invalid command. Score now {self.score}')


if __name__ == '__main__':
    game = AdventureGame()
    game.play_game()


