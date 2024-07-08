from sys import stdin

chant_dict = {"SONGDO": "HIGHSCHOOL",
                "CODE": "MASTER",
                "2023": "0611",
                "ALGORITHM": "CONTEST"}

chant = stdin.readline().rstrip()

print(chant_dict[chant])