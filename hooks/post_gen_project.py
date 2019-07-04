import os
import logging
import shutil
import fileinput

logger = logging.getLogger(__name__)

def generate_testcases():
    # create a certain number of testcases, as specified by the user
    number_of_testcases = int(input("number_of_testcases: "))
    for i in range(number_of_testcases):
        filename = input("testcase_%s_name (OPTIONAL): " % (i + 1))
        if not filename:
            filename = "testcase_" + str(i + 1)
        uid = int(input("testcase_%s_id: " % (i + 1)))
        description = input("testcase_%s_description (OPTIONAL): " % (i + 1))
        print("\n")

        # making a copy of template_testcases.py
        src_file = "../{{ cookiecutter.project_name }}/testcases/template_testcases.py"
        dest_file = "../{{ cookiecutter.project_name }}/testcases/" + filename + ".py"
        shutil.copy2(src_file, dest_file)

        # replacing text in the testcase file
        replacements = { '< describe your testcases >': description, "template_testcases": filename }
        with open(dest_file, 'r') as file :
            filedata = file.read()
        for src, target in replacements.items():
            if target:
                filedata = filedata.replace(src, target)
        with open(dest_file, 'w') as file:
            file.write(filedata)


def generate_datafile():
    src_file = "../{{ cookiecutter.project_name }}/data/template_datafile.yaml"
    
    include_datafile = input("include_datafile? (yes or no): ")
    if 'y' in include_datafile.lower(): # yes, include the datafile
        filename = input("datafile_name [template_datafile]: ")
        if not filename:
            filename = "template_datafile"
        dest_file = "../{{ cookiecutter.project_name }}/data/" + filename + ".yaml"
        os.rename(src_file, dest_file)
    else: # no, don't include the datafile
        os.remove(src_file)


def main():
    print("\n")
    generate_testcases()
    generate_datafile()
    


if __name__ == "__main__":
    main()
