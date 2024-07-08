from sys import stdin

club_dict = {"M": "MatKor",
            "W": "WiCys",
            "C": "CyKor",
            "A": "AlKor",
            "$": "$clear"}

club = stdin.readline().rstrip()

print(club_dict[club])