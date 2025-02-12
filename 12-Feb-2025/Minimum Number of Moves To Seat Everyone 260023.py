# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        count=0
        for i in range(len(seats)):
            count+=abs(seats[i]-students[i])
        return count
        