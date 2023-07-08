#!/bin/python3
import os.path, sys, time, random, re, statistics, textwrap, shutil


def interview():
	global name
	global max
	cs()
	prin("Hi! What's your name?")
	slp(1)
	name = input("(Don't enter a name if you're feeling timid)\n\n")
	if name != "" and name != " ":
		cs()
		prin(f"Good luck with the gatekeepers {name}! I hear barely anybody passes them....\n\n")
		slp(1)
		questions = select_different_role()
	else:
		cs()
		name = random.choice(users)
		prin(f"Shy for an interview? Oh well, I'll just call you {name} for now.\n\n")
		slp(1)
		questions = select_different_role()
	cs()
	prin(f"My name is {interviewer}, and I'll be your interviewer. Thank you for applying for this position, {name}. I really liked your CV and you seem like a really strong candidate! Just need to ask you a couple of questions to make sure you're the real deal and not just some {fake}!\n")
	start_test(questions)

def select_different_role():
	global fake
	global role
	global pro
	while True:
		try:
			a = input("What role are you applying for?\n1. Hacker\n2. Other\n3. Exit\n\n")
			a = int(a)
			b = ""
			if a:
				if a == 1:
					cs()
					b = "hacker_qa.txt"
					pro = "hacker"
					fake = "script kiddy"
					prin(f"Awesome! here's a pro tip before your interview:\n\n{h_tips}", end="")
					slp(1)
					w()
					cs()
					break
				elif a == 2:
					while True:
						cs()
						pro = input("Role:\n\n")
						fake = "fake " + pro
						fake = validate(fake)
						if fake != "":
							while True:
								try:
									cs()
									b = input("Question & answer file:\n\n")
									if not os.path.isfile(b):
										raise FileNotFoundError
									else:
										cs()
										prin("Found your file!")
										slp(2)
									cs()
									prin(f"Here's a quick tip before your interview:\n\n{tips}")
									slp(2)
									w()
									break
								except FileNotFoundError:
									prin("\nUnfortunately it's not possible to find the file. Make sure it's spelled correctly and add the extension '.txt' to the file name if it exists")
									slp(1)
									w()
							break
						elif not fake:
							prin("\nYou can't have an interview if you don't apply for a position!")
							slp(1)
					break
				elif a == 3:
					prin("\nScared you off already? That was fast!")
					slp(2)
					quit()
				elif b:
					break
				else:
					prin("\nHey! Breathe and choose a number: 1-2 ")
					slp(2)
					cs()
			else:
				prin("\nDon't overcomplicate simple things! Just choose 1-3")
				slp(2)
				cs()
		except ValueError:
			prin("\nDon't overcomplicate simple things! Just choose 1-3")
			slp(2)
			cs()
	return role_selector(a, b)

def role_selector(role, f):
	global max
	if role == 5:
		select_different_role()
	else:
		pass
	file = open(f).read()
	file = file.splitlines()
	questions = []
	for fi in file:
		result = re.search(r'^(.*)[.?](?=:)', fi)
		if result:
			qa = result.group(0)
			question = {}
			question["q"] = qa
			result = re.search(r"(?<=:).*(\.)+", fi)
			if result:
				qa = result.group(0)
				question["a"] = qa
				questions.append(question)
	max = len(questions)
	return questions

def start_test(questions):
	global n_questions
	n_questions = begin()
	submitted = tests(questions)
	check_results(submitted, questions)

def begin():
	while True:
		start = input("Are you ready for your interview questions? (y/n)\n\n").lower()
		if start == "y":
			prin("\n\nGreat! Let's get to it then!")
			slp(1.5)
			while True:
				try:
					cs()
					qs = input(f"How many questions can you handle? (max: {max})\n\n")
					if validate(qs) == "":
						slp(2)
					qs = int(qs)
					if qs < 1 or qs > int(max):
						cs()
						prin("At least you have a sense of humor... but it'll cost you this job. Please give a valid numer so that we can begin. (1-159)\n")
						slp(2)
					elif qs < 10:
						cs()
						prin("Hmm.. Seems this will be quick!\n")
						slp(2)
						return qs
					elif qs >= 10 and qs < 40:
						cs()
						prin("That seems like a decent amount of questions! 10+ points to you! (Just kidding)\n")
						slp(2)
						return qs
					elif qs > 40:
						cs()
						prin("You know making me tired from asking so many questions isn't going to land you this job, right?\n")
						slp(2)
						return qs
				except ValueError:
					prin("\n\nCommon, this is a serious interview. Just answer the question...")
					slp(2)
		elif start == "n":
			cs()
			prin(f"No worries, I already knew you were a {fake}, I just wanted to see it in person! Bye!\n")
			quit()
		else:
			prin("\nInterview didn't start and you're already having trouble? Please give a valid answer.\n")
			slp(2)
			cs()

def tests(questions): #Generates a test based on the amount of questions the user desires
	global max
	cs()
	test = {}
	# b = 0
	i = 1
	# Chooses a random questions & answers and adds them to a dictionary
	perguntas = random.sample(questions, int(n_questions))
	for p in perguntas:
		# per = perguntas[b]
		test["q"+str(i)] = p["q"]
		test["a"+str(i)] = p["a"]
		# b += 1
		i += 1
	i -= 1
	# Generate questions to user and save responses to dictionary
	q = 1
	for num in range(i):
		test["s"+str(q)] = input(""+str(q) + ". " + test["q"+str(q)] + "\n")
		q +=1
		cs()
	# Ask if user wants to check their results
	if int(n_questions) < 10:
		prin("Hey, I told you this would be quick!")
		w()
	elif int(n_questions) > 10 and int(n_questions) < 40:
		prin("Good job! That was quite a few questions!")
		w()
	elif int(n_questions) > 40:
		prin("That was insane. I'm traumatized about giving interviews because of you.")
		w()
	while True:
		cs()
		a = input("Do you want to check your results? (y/n)\n\n").lower()
		validate(a)
		if a == "n":
			prin("\nGuess we'll never know if you're worth it or not!")
			w()
			try:
				while True:
					cs()
					ask = input("What do you want to do?\n1. New interview\n2. Exit and cry\n\n")
					if validate(ask) == "":
						slp(2)
					ask = int(ask)
					if ask == 1:
						cs()
						questions = select_different_role()
						max = len(questions)
						start_test(questions)
					elif ask == 2:
						cs()
						prin("Oh well... If you ever need anything, you know who to count on!")
						slp(2)
						prin("\n\nThe police or something, please don't count on me.")
						quit()
					else:
						prin("\n\nThe interview really messed you up, huh?")
						slp(2)
			except ValueError:
				prin("\nIt's just a simple question. Relax. Take a breath. Think of a valid number")
				slp(2)
		elif a == "y":
			break
		else:
			prin("\n\nDid the interview drive you crazy? Yeah me too, but just give me a valid answer!")
			slp(2)
	return test

def check_results(submitted, questions):
	c = 1
	i = 1
	f = 1
	correct_ans = []
	cor_ans = {}
	inc_ans = {}
	for n in range(int(n_questions)):
		# try:
		while True:
			cs()
			prin("+ Question "+str(f)+":\n\""+submitted["q"+str(f)]+"\"\n")
			slp(.5)
			prin("+ Example correct response:\n\""+submitted["a"+str(f)]+"\"\n")
			slp(.5)
			prin("+ Your response:\n\""+submitted["s"+str(f)]+"\"\n")
			ans = input("Did you answer correctly? (y/n)\n").lower()
			ans = validate(ans)
			if ans == "y":
				correct_ans.append(1)
				cor_ans["q"+str(c)] = submitted["q"+str(f)]
				cor_ans["a"+str(c)] = submitted["s"+str(f)]
				c += 1
				break
			if ans == "n":
				inc_ans["q"+str(i)] = submitted["q"+str(f)]
				inc_ans["a"+str(i)] = submitted["s"+str(f)]
				inc_ans["e"+str(i)] = submitted["a"+str(f)]
				i += 1
				break
			elif ans != "":
				print("Please select 'y' or 'n'\n")
				slp(2)
		f += 1
		cs()
		# except ValueError:
		# 	prin("Select 'y' or 'n'\n")
	display_results(correct_ans, cor_ans, inc_ans, questions)

def display_results(correct_ans, cor_ans, inc_ans, questions):
	global num_of_tests
	z = len(correct_ans)
	percentage = (z/int(n_questions))*100
	total_percent.append(percentage)
	num_of_tests += 1
	prin("Let's check your results...")
	slp(1)
	if percentage == 100:
		prin("That's amazing! You answered 100% of the questions correctly!")
		slp(1)
		prin("You can start immediately, no doubt about that. Be here in 1hr ready to hack some big corporations... And serve me some coffee, of course...\n")
	elif percentage >= 50 and percentage < 80:
		prin("I feel like this isn't going to work out... It's not you, it's us...")
		slp(1)
		prin(f"Actually, to be honest, our standards require someone that can get more correct answers than that, and you only got {percentage:.2f}% correct.\n")
	elif percentage < 50:
		prin(f"I don't get paid enough for this. Just waisted my precious time for {percentage:.2f}%? Sorry but this job ain't for you.\n")
	else:
		prin(f"That was actually pretty good. You got {percentage:.2f}% correct! The final decision doesn't depend on me unfortunately, but I'll definitely let my superiors know how good you went!\n")
	while True:
		try:
			choice = input("What would you like to do now?\n1. Another interview\n2. Check correct questions\n3. Check wrong questions\n4. Check example correct answers (For failed questions only)\n5. Check total result until now\n6. Leave\n\n")
			choice = int(choice)
			if choice == 1:
				start_test(questions)
			elif choice == 2:
				cs()
				l = 1
				for a in range(z):
					prin(str(l)+": "+cor_ans["q"+str(l)]+"\n\n")
					prin(cor_ans["a"+str(l)])
					l += 1
					slp(1)
					w()
					cs()
			elif choice == 3:
				cs()
				if int(n_questions) - z == 0:
					prin("But you didn't get any wrong!")
					slp(1)
					w()
					cs()
				else:
					l = 1
					for a in range(int(n_questions) - z):
						prin(str(l)+": " + inc_ans["q" + str(l)] + "\n\n")
						prin(inc_ans["a" + str(l)])
						l += 1
						slp(1)
						w()
						cs()
			elif choice == 4:
				cs()
				l = 1
				for a in range(int(n_questions) - z):
					prin(str(l)+": " + inc_ans["q" + str(l)] + "\n\n")
					prin(inc_ans["e" + str(l)])
					l += 1
					slp(1)
					w()
					cs()
			elif choice == 5:
				cs()
				if num_of_tests < 2:
					m_percent = statistics.median(total_percent)
					prin(f"So far you have done only one interview, and you got {m_percent:.2f}% correct")
					w()
					cs()
				else:
					m_percent = statistics.median(total_percent)
					prin(f"In total, you have gone through {num_of_tests} interviews and answered {m_percent:.2f}% of all questions correctly")
					slp(1)
					w()
					cs()
			elif choice == 6:
				cs()
				prin(f"Ok! Just don't forget: No matter your results, being a {pro} is a life long journey of studying and self improvement. So go study some more!")
				slp(2)
				quit()
			else:
				cs()
				prin("There are more people I need to interview today. Select a valid answer already. '1-5'")
				slp(2)
		except ValueError:
			cs()
			prin("There are more people I need to interview today. Select a valid answer already. '1-5'")
			slp(2)

def cs():
	sys.stdout.write("\033[2J\033[H")
	sys.stdout.flush()

def w():
	input("\n\nPress enter to continue...")

def validate(a):
	sa = a.strip()
	if sa == "":
		prin("\nYou gotta enter something.. Anything...")
		slp(2)
	else:
		return sa
	
def prin(*args, **kwargs):
	terminal_width = shutil.get_terminal_size().columns
	wrapped_args = []
	for arg in args:
		if "\n" in str(arg):
			wrapped_text = "\n".join(textwrap.fill(line, width=terminal_width) for line in str(arg).split("\n"))
			wrapped_args.append(wrapped_text)
		else:
			wrapped_args.append(textwrap.fill(str(arg), width=terminal_width))
	print(*wrapped_args, **kwargs)

#Variables and lists
slp = time.sleep
num_of_tests = 0
total_percent = []
names = ["Heath Aldams", "IddSec", "Alexis Alhmmod", "David Bombon", "John Hammock", "Offline Overflow", "Worknet Chuck", "Shannon Codemorse", "Stoked Fredrik", "Chris Greering", "Nah Amsec", "Zaid Z", "Jazon Haddox", "Ryan 0night"]
users = ["Alan Smithee", "Satoshi Nakamoto", "Unknown Soldier", "Jane Doe", "John Doe", "Patient Zero", "Publius"]
name = ""
fake = ""
role = ""
pro = ""
n_questions = ""
max = ""
interviewer = random.choice(names)
hak_tips = open("hacking_protips.txt").read()
h_tips = random.choice(hak_tips.splitlines())
gen_tips = open("tips.txt").read()
tips = random.choice(gen_tips.splitlines())
#Start of Program
try:
	cs()
	prin("""\n\n            ▄▄▄█████▓ ██░ ██ ▓█████                    
            ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀                    
            ▒ ▓██░ ▒░▒██▀▀██░▒███                      
            ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄                    
              ▒██▒ ░ ░▓█▒░██▓░▒████▒                   
              ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░                   
                ░     ▒ ░▒░ ░ ░ ░  ░                   
              ░       ░  ░░ ░   ░                      
                      ░  ░  ░   ░  ░                   
                                                       
           ▄████  ▄▄▄      ▄▄▄█████▓▓█████             
          ██▒ ▀█▒▒████▄    ▓  ██▒ ▓▒▓█   ▀             
         ▒██░▄▄▄░▒██  ▀█▄  ▒ ▓██░ ▒░▒███               
         ░▓█  ██▓░██▄▄▄▄██ ░ ▓██▓ ░ ▒▓█  ▄             
         ░▒▓███▀▒ ▓█   ▓██▒  ▒██▒ ░ ░▒████▒            
          ░▒   ▒  ▒▒   ▓▒█░  ▒ ░░   ░░ ▒░ ░            
           ░   ░   ▒   ▒▒ ░    ░     ░ ░  ░            
         ░ ░   ░   ░   ▒     ░         ░               
               ░       ░  ░            ░  ░            
                                                       
 ██ ▄█▀▓█████ ▓█████  ██▓███  ▓█████  ██▀███    ██████ 
 ██▄█▒ ▓█   ▀ ▓█   ▀ ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ 
▓███▄░ ▒███   ▒███   ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░ ▓██▄   
▓██ █▄ ▒▓█  ▄ ▒▓█  ▄ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒
▒██▒ █▄░▒████▒░▒████▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒▒██████▒▒
▒ ▒▒ ▓▒░░ ▒░ ░░░ ▒░ ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
░ ░▒ ▒░ ░ ░  ░ ░ ░  ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░
░ ░░ ░    ░      ░   ░░          ░     ░░   ░ ░  ░  ░  
░  ░      ░  ░   ░  ░            ░  ░   ░           ░  
                                                       

""")
	slp(2)
	w()
	interview()
except KeyboardInterrupt:
	if name:
		prin(f"\n\nGoodbye {name}! Hopefully your next interview will be the real thing!")
	else:
		prin("\n\nSee ya!")
