inp = input()
if int(inp[1]) % 2 == 0 and int(inp[1]) % 3 == 0 and int(inp[1]) != 0: print('Best')
elif int(inp[1]) % 2 == 0 and int(inp[1]) != 0: print('Good')
elif int(inp[1]) % 3 == 0 and int(inp[1]) != 0: print('Very good')
else: print('None')