# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from collections import defaultdict

class Solution(object):
    def findWinners(self, matches):
        freq_loss = defaultdict(int)
        players = set()
        
        for match in matches:
            winner, loser = match
            freq_loss[loser] += 1
            players.add(winner)
            players.add(loser)
        
        no_loss = []
        one_loss = []
        
        for player in players:
            if freq_loss[player] == 0:
                no_loss.append(player)
            elif freq_loss[player] == 1:
                one_loss.append(player)
        
        no_loss.sort()
        one_loss.sort()
        
        return [no_loss, one_loss]


