class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        loss_count = {}
        players = set()
        
        
        for winner, loser in matches:
            if loser in loss_count:
                loss_count[loser] += 1
            else:
                loss_count[loser] = 1
            players.add(winner)
            players.add(loser)
        
   
        no_losses = []
     
        one_loss = []
        
    
        for player in players:
            if loss_count.get(player, 0) == 0:
                no_losses.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)
        
      
        no_losses.sort()
        one_loss.sort()
        
        return [no_losses, one_loss]

