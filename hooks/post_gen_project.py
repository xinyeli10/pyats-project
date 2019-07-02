print("------------------------------")
print("POST GEN HOOK\n\n")

number_of_test_cases = int(input("number_of_test_cases: "))
for i in range(number_of_test_cases):
	name = input("testcase_%s_name [OPTIONAL]: " % (i + 1))
	print(name)
	uid = int(input("testcase_%s_id: " % (i + 1)))
	print(uid)
	description = input("testcase_%s_description: " % (i + 1))
	print(description)
