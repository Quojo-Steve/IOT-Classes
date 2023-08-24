tutor_list = ["andrea","tomi","kelvin"]

print(tutor_list[2])
def whatage():
	age_list = {}
	for i in tutor_list:
		age_input = input(f"Hello {i}, what is your age ?")
		age_list[i]=age_input
		print(age_input)
	print(age_list)
		
whatage()




class math:
	def pi():
		return 3.124
		
math.pi()
