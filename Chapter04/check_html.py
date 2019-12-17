from stack import Stack

def check_tags(html_string):
    s = Stack()
    i = 0
    while i < len(html_string):

        if html_string[i] == "<":
            temp = ""
            i += 1
            while i != len(html_string) - 1 and html_string[i] != ">":
                temp += html_string[i]
                i += 1
            if html_string[i] != ">":
                return False
            if temp[0] == "/":
                if s.is_empty():
                    return False
                elif temp[1:] == s.peek():
                    s.pop()
                else:
                    return False
            elif temp[-1] == "/":
                pass
            else:
                s.push(temp)

        i += 1
    if s.is_empty():
        return True
    else:
        return False

a = """
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>"""

print(check_tags(a))
