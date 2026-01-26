fileOpening = {"file": "anime.txt", "mode": "r+"}
all_in_file = [t for t in open(fileOpening['file'], fileOpening["mode"]).readlines()]
anime = {}
for unit in all_in_file:
    current_type: str
    if ":\n" in unit:
        current_type = unit[:unit.find(":\n")]
        anime[current_type] = []
    if not (":\n" in unit):
        unit = ((unit.replace("\n", "")).replace('   -', ''))[1:]
        anime[current_type].append(unit)
print(anime.values())