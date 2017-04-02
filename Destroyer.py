import digitalocean
import sys
from time import sleep

token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #API TOKEN GOES HERE
manager = digitalocean.Manager(token=token)
if not token:
	print("please make sure you have entered your API token in the program code...")
my_droplets = manager.get_all_droplets()
print("fetching droplets...")
print(my_droplets)
if not my_droplets:
    print("no droplets currently active")
    sleep(2)
    sys.exit()
choice = input("destroy all droplets? (y/n):    ")
if choice == "y":
    for droplet in my_droplets:
        droplet.destroy()
else:
    sys.exit()
