import shutil

print("------------------------------")
print("POST GEN HOOK\n\n")

number_of_test_cases = int(input("number_of_test_cases: "))
for i in range(number_of_test_cases):
	name = input("testcase_%s_name [OPTIONAL]: " % (i + 1))
	uid = int(input("testcase_%s_id: " % (i + 1)))
	description = input("testcase_%s_description [OPTIONAL]: " % (i + 1))
	src = "/{{ cookiecutter.project_name }}/testcases/template_testcases.py"
	dest = "/{{ cookiecutter.project_name }}/testcases/testcase_" + str(i + 1) + ".py"
	shutil.copy2(src, dest)