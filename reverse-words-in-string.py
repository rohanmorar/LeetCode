"""
Given a string as an input. Reverse all the words in the string and return the new string with the words in reversed order.
Example: "A Wild Bat" ---> reverseString("A Wild Bat") ---> "Bat Wild A"

>>> reverseString("A Big Dog Sat On The Roof")
'Roof The On Sat Dog Big A'

        P : 1 input - type: String
        R : 1 output - type: String
        E :
            s = "A Bat Flew High" -> reverseWords(s) -> "High Flew Bat A"
            s = "A    Bat  Flew  High" -> reverseWords(s) -> "High Flew Bat A"
            s = "   A Bat  Flew   High  " -> reverseWords(s) -> "High Flew Bat A"
        P :
            s = "A Bat Flew High" -> reverseWords(s) -> "High Flew Bat A"
                s.split() --->  ["A", "Bat", "Flew", "High"]
                ["A", "Bat", "Flew", "High"][::-1] ---> ["High", "Flew", "Bat", "A"]
                " ".join(["High", "Flew", "Bat", "A"]) ---> "High Flew Bat A"
        A :
            s.split() - using default split() e.g. no param passed, is O(n), since it just scans through the string finding all whitespace.
            [::-1] - O(N), scanning each item from end to beginning
            " ".join() - O(N), go through each item in array
            Overall O(3 * N) ---> O(N) or Linear time complexity
            Space Complexity: O(1) since we are not creating new arrays or maps

"""

def reverseString(s):
    return " ".join(s.split()[::-1])
