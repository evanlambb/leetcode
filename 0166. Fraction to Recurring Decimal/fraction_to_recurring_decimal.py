class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"


        res = []

        if (numerator > 0) != (denominator > 0):
            res.append("-")

        num, denom = abs(numerator), abs(denominator)

        res.append(str(num//denom))

        remainder = num % denom

        if remainder == 0:
            return "".join(res)

        res.append(".")
        remainder_seen = {}
        while(remainder != 0):
            if remainder in remainder_seen:
                # This part is repeating
                res.insert(remainder_seen[remainder], "(")
                res.append(")")
                return "".join(res)

            # This part is not repeating
            remainder_seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder//denom))
            remainder %= denom

        return "".join(res)
            