
file = open('example_file', 'r')
try:
    content = file.read()
finally:
    file.close()
