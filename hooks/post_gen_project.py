import shutil
import fileinput

print("\n\n------------------------------")
print("POST GEN HOOK\n")

# create a certain number of testcases, as specified by the user
number_of_test_cases = int(input("number_of_test_cases: "))
for i in range(number_of_test_cases):
    filename = input("testcase_%s_name [OPTIONAL]: " % (i + 1))
    uid = int(input("testcase_%s_id: " % (i + 1)))
    description = input("testcase_%s_description [OPTIONAL]: " % (i + 1))
    print()

    # making a copy of template_testcases.py
    src_file = "../{{ cookiecutter.project_name }}/testcases/template_testcases.py"
    dest_file = "../{{ cookiecutter.project_name }}/testcases/testcase_" + str(i + 1) + ".py"
    if filename: # file name not specified
        dest_file = "../{{ cookiecutter.project_name }}/testcases/" + filename + ".py"
    shutil.copy2(src_file, dest_file)

    # replacing text in the testcase file
    replacements = { '< docstring description of this testcase >': description }
    with open(dest_file, 'r') as file :
        filedata = file.read()
    for src, target in replacements.items():
        if target:
            filedata = filedata.replace(src, target)
    with open(dest_file, 'w') as file:
        file.write(filedata)
