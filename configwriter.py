from configparser import ConfigParser

config = ConfigParser()

config["Default"] = {
    "numberdigits": 6,
    "numbertries": 4,
    "playername" : "Player"
}
config["Purv"] = {
    "numberdigits": 10,
    "numbertries": 6,
    "playername" : "Purvansh"
}
config["SUDO"] = {
    "numberdigits": 6,
    "numbertries": 8,
    "playername" : "Cheater",
    "cheats": "on"
}

with open("number_guessing.ini","w") as f:
    config.write(f)
