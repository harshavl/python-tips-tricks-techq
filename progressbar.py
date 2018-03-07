
from __future__ import print_function
from time import sleep
import tqdm



fruits = [
    "Acai", "Apple", "Apricots", "Avocado", "Banana", "Blackberry",
    "Blueberries", "Cherries", "Coconut", "Cranberry", "Cucumber",
    "Durian", "Fig", "Grapefruit", "Grapes", "Kiwi", "Lemon", "Lime",
    "Mango", "Melon", "Orange", "Papaya", "Peach", "Pear", "Pineapple",
    "Pomegranate", "Raspberries", "Strawberries", "Watermelon"
]


contains_berry = 0
for fruit in tqdm.tqdm(fruits):
	if "berr" in fruit.lower():
		contains_berry += 1
	sleep(.1)

print( contains_berry )

contains_berry = 0
pbar = tqdm.tqdm(fruits, desc="Reviewing names", unit="fruits" )

for fruit in pbar:
	if "berr" in fruit.lower():
		contains_berry += 1
	pbar.set_postfix(hits=contains_berry)
	sleep(.1)

print(contains_berry)


for i in tqdm.trange( 100000, unit_scale="telnet", desc='Trange:' ):
	tqdm.write()
	pass

