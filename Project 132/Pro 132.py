import csv
import matplotlib.pyplot as plt

rows = []
with open("Main.csv", "r") as f:
  csv_reader = csv.reader(f)
  for i in csv_reader:
    rows.append(i)

headers = rows[0]
star_data = rows[1:]
headers[0] = "row_num"
print(headers)
# print(star_data[6])

temp_star_data = list(star_data)

for i in temp_star_data:
  star_mass = i[3]
  if star_mass.lower() == "unknown":
    star_data.remove(i)
    continue
  else:
    i[3] = float(i[3])*1.989e+30

  star_radius = i[4]
  if star_radius.lower() == "unknown":
    star_data.remove(i)
    continue
  else:
    i[4] = float(i[4])*6.957e+8

print(len(star_data))

star_masses = []
star_radius = []
star_names = []

for i in star_data:
  star_masses.append(i[3])
  star_radius.append(i[4])
  star_names.append(i[1])

star_gravity = []

for index, name in enumerate(star_names):
  gravity = (float(star_masses[index])*5.972e+24)/(float(star_radius[index])*float(star_radius[index])*6371000*6371000)*6.674e-11

  star_gravity.append(gravity)

headers.append("Gravity")

for i in star_data:
    if star_gravity[int(i[0])]:
        i.append(star_gravity[int(i[0])])

print(headers)
# print(star_data)

plt.plot(star_masses, star_radius, 'ro')
plt.ylabel('star radius')
plt.xlabel('star masses')
plt.title('Relation Between Mass and Radius')
plt.show()

plt.plot(star_masses, star_gravity, 'ro')
plt.ylabel('star gravity')
plt.xlabel('star masses')
plt.title('Relation Between Mass and Gravity')
plt.show()