class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # okay a stack implementation works here
        # because each car is limited by the one directly ahead of it
        # if its less then it gets appended to the stack and ig itss more then its all good.

        # wait what im doing wrong here is that if a car behind another car catches up that is part of the same thing so the stack doesn't count it when a behind car gets there before it should 

        stack = []
        new_thing = []
        for i in range(len(position)):
            new_thing.append((position[i], speed[i]))
        new_thing.sort()


        for i in range(len(position) - 1, -1, -1):
            time = (target - new_thing[i][0]) / new_thing[i][1]
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)
        