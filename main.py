#light red bags contain 1 bright white bag, 2 muted yellow bags.
#dark orange bags contain 3 bright white bags, 4 muted yellow bags.
#bright white bags contain 1 shiny gold bag.
#muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
#shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
#dark olive bags contain 3 faded blue bags, 4 dotted black bags.
#vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
#faded blue bags contain no other bags.
#dotted black bags contain no other bags.

luggage = []
package_colors = {}
number = 0

with open("luggage.txt", "r") as file1:
    for line in file1:
        luggage.append(line)
    print(luggage)
    print(len(luggage))

for item in luggage:
    key = item.split(" ")[0] + " " + item.split(" ")[1]
    package_colors[key] = item.split(" ")[4:]
print(package_colors)
print(len(set(package_colors)))

for key, value in package_colors.items():
    value = " ".join(value)
    if value.find("shiny gold bag") >= 0:
        number = number + 1
    if value.find("shiny gold bags") >= 0:
        number = number - 1
print(number)
