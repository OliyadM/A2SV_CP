class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        
        p = 0
        t = 0
        match_count = 0
        
        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                match_count += 1
                p += 1
                t += 1
            else:
                t += 1
        
        return match_count
