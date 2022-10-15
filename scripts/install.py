import os

filepath = "../modlist.md"

os.chdir("pack")

with open(filepath) as file:
    for line in file:
        print(line.rstrip())
        if "modrinth" in line.rstrip():
            print("installing: ", line)
            os.system("packwiz -y modrinth install " + line.rstrip())
        if "curseforge" in line.rstrip():
            os.system("packwiz -y curseforge install " + line.rstrip())
