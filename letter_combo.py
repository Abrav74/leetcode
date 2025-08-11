from typing import List


def letterCombinations(self, digits: str) -> List[str]:
    output = []
    if digits == "":
        return output

    phone_alpha = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def combo(phone_num, letters=""):
        if phone_num == "":
            output.append(letters)
            return
        for letter in phone_alpha[phone_num[0]]:
            combo(phone_num[1:], letters + letter)

    combo(digits)

    return output
