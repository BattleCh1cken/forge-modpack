import os

filepath = "../modlist.md"

os.chdir("pack")

with open(filepath) as file:
    for line in file:
        if line[0] != "<":
            if "modrinth" in line.rstrip():
                os.system("packwiz -y modrinth install " + line.rstrip())
            if "curseforge" in line.rstrip():
                os.system("packwiz -y curseforge install " + line.rstrip())
os.system("packwiz refresh")

os.system("packwiz modrinth export --pack-file pack.toml -o ../build/forge-modpack.mrpack")
