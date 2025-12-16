class Reverse:
    def __init__(self, s):
        self.s=s
    def reversed(self):
        reversed_string=""
        for char in self.s:
            reversed_string=char+reversed_string
        return reversed_string
if __name__=="__main__":
    string = input("Enter a string/sentence: ")
    r = Reverse(string)
    print("Reversed string:",r.reversed())