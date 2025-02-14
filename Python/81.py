import re
# Teksti fillestar
a = "Mëso Python, mëso programim!"
# Zëvendësimi i të gjitha paraqitjeve të "mëso" me "studio"
b = re.sub(r"mëso", "studio", a)
# Shfaqja e rezultatit
print(b)
