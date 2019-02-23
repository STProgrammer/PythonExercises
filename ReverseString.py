class PySolutions:
    def reverse_string(string):  
        chars = list(string)
        revchars = list(len(chars) * [None])
        for i in range(0, len(chars)):
            revchars[i] = chars.pop()
        revstring = ''.join(revchars)
        return revstring

class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_solution().reverse_words('hello .py'))


string = input("type in something: ")
print(PySolutions.reverse_string(string))


