class FSA:

    def __init__(self):
        self.state = "q0"

    def transition(self, char):
        if self.state == "q0":
            if char == 'a':
                self.state = "q1"
            else:
                self.state = "q0"
        elif self.state == "q1":
            if char == 'a':
                self.state = "q1"
            elif char == 'b':
                self.state = "q2"
            else:
                self.state = "q0"
        elif self.state == "q2":
            if char == 'a':
                self.state = "q1"
            else:
                self.state = "q0"

    def is_accepted(self):
        return self.state == "q2"

def match_string(s):
    fsa = FSA()
    for char in s:
        fsa.transition(char)
    return fsa.is_accepted()
test_strings = ["ab", "aab", "bab", "abc", "abab", "ba", "b", "helloab"]

print("String\t\tEnds with 'ab'?")

print("-" * 30)

for s in test_strings:
    print(f"{s:<15}{match_string(s)}")