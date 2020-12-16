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
        self.directions = ('north', 'west', 'south', 'east')
        self.room = 1
        self.direction = 0

    def play_game(self):
        print("""You are in room 1 and facing north.
    Valid commands are the following:
    move: move to next room if not facing a wall,
    face <cardinal direction>: which way to face, 
    describe: will describe the room
    quit: quit game.""")
        command: str = ''
        while True:
            self.parseinput(input('What do you do?: '))

    def parseinput(self, cmd: str):
        if cmd.lower() == 'move':
            status = self.game_map[self.room][self.direction]
            if status == 0:
                print('You facing a wall and cannot move. Maybe turn a little?')
            else:
                self.room = status
                print(f'You have moved to room {self.room}')
        elif cmd.lower() == 'describe':
            print(f'You are in room number {self.room} and facing {self.directions[self.direction]}')
        elif cmd.lower() == 'quit':
            print('Game quits.')
            exit(0)
        else:
            try:
                if 'face' in cmd.lower():
                    self.direction = self.directions.index(cmd.lower()[5:])
                    print(f'You are now facing {self.directions[self.direction]}')
                else:
                    raise ValueError('Invalid command')
            except ValueError:
                print('Invalid command.')


if __name__ == '__main__':
    game = AdventureGame()
    game.play_game()


