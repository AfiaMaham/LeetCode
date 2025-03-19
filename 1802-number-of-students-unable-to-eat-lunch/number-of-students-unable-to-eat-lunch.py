from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentDeque = deque(students)
        sandwichDeque = deque(sandwiches)
        count = 0
        while True:
            if len(studentDeque) == 0:
                return 0
            if studentDeque[0] == sandwichDeque[0]:
                count = 0
                studentDeque.popleft()
                sandwichDeque.popleft()
            else:
                st = studentDeque.popleft()
                studentDeque.append(st)
                count += 1
                if count == len(studentDeque):
                    break

        return(len(studentDeque))
        

