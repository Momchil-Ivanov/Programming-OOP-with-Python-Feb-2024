from typing import List
from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.players.append(player)
            return f'Welcome player {player.name} to the guild {self.name}'
        elif player.guild == self.name:
            return f'Player {player.name} is already in the guild.'
        else:
            return f'Player {player.name} is in another guild.'

    def kick_player(self, player_name: str):
        for c_player in self.players:
            if c_player.name == player_name:
                self.players.remove(c_player)
                c_player.guild = 'Unaffiliated'
                return f'Player {player_name} has been removed from the guild.'

        return f'Player {player_name} is not in the guild.'

    def guild_info(self) -> str:
        players_details = "\n".join(p.player_info() for p in self.players)
        return f'Guild: {self.name}\n' \
               f'{players_details}'


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.kick_player("George"))
# player1 = Player("Georgeeeeeee", 50, 100)
# player1.add_skill("Shield Breakeeeeeee", 20)
# guild.assign_player(player1)
# print(guild.guild_info())


