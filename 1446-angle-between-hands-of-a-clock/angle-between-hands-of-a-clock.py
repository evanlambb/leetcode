class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour += minutes / 60
        hour %= 12
        angleHour = 0 if hour == 12 else hour * (360 / 12)
        angleMin = minutes * (360 / 60)
        ans = abs(angleHour - angleMin)
        return ans if ans <= 180 else 360 - ans