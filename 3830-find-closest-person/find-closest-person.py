class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
          per1 = abs(x - z)
          per2 = abs(y - z)
          if per1 == per2:
                return 0
          elif per1 < per2:
            return 1
          else:
                return 2