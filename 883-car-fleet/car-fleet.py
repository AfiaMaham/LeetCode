class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(
            [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))],
            reverse=True  
        )

        stack = []

        for pos, t in cars:
            if not stack or t > stack[-1]:
                stack.append(t) 

        return len(stack)  
