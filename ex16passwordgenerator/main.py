import string
import random

passgenindex = string.ascii_letters + string.punctuation + string.digits
passgenwords = ["alpha", "bravo", "cobra", "delta", "eagle", "falcon", "gamma", "hydra",
    "indigo", "jade", "kappa", "lunar", "mango", "nebula", "omega", "phantom",
    "quasar", "raven", "sigma", "titan", "ultra", "viper", "wolf", "xenon",
    "yield", "zephyr", "amber", "blaze", "crystal", "dagger", "ember", "frost",
    "glacier", "horizon", "iris", "jungle", "karma", "laser", "mystic", "nova",
    "orbit", "pulse", "quantum", "razor", "storm", "thunder", "umbra", "vertex",
    "winter", "zenith"]

orientations = {"lower": str.lower, "upper": str.upper, "capitalize": str.capitalize}

def passwordLengthCheck(password, limit):
    if limit != "0":
        try:
            while len(password) > int(limit):
                password = password.replace(password[random.randrange(0, len(password))], "")
            print(f"> Password limited to a number of characters ({limit})")
        except ValueError:
            print("> No restriction selected.")
    else:
        print("> No restriction selected.")
    return password

def main():
    choices = ["1", "easy", "2", "medium", "3", "hard"]
    print("Password Generator\n"
    "[1] / [easy] - Easy Difficuilty Password\n"
    "[2] / [medium] - Medium Difficuilty Password\n"
    "[3] / [hard] - Hard Difficuilty Password\n")
    while True:
        passwordDiffPick = input("What kind of password do you want?: ")
        if passwordDiffPick.lower() in choices:
            break
        else:
            print("> Please select an existing option!")
    passwordLengthLimit = input("How long your password should be at most? (Type \"0\" for no restriction): ")
# easy password generator
    if passwordDiffPick == "1" or passwordDiffPick == "easy":
        wordAmount = random.randrange(2, 4)
        passwordResult = "".join(random.choices(passgenwords, k=wordAmount))
        passwordResult = passwordLengthCheck(passwordResult, passwordLengthLimit)
        return passwordResult
# medium password generator
    elif passwordDiffPick == "2" or passwordDiffPick == "medium":
        numberCap = 0
        wordAmount = random.randrange(2, 5)
        passwordResult = ""
        while wordAmount != 0:
            if random.choice([0, 1]) == 0:
                passwordResult = passwordResult + random.choice(list(orientations.values()))(random.choice(passgenwords))
                wordAmount -= 1
            elif numberCap != 3:
                passwordResult = passwordResult + str(random.randrange(1, 9999))
                numberCap += 1
        if random.choice([0, 1]) == 0 and numberCap != 3 or numberCap == 0:
            passwordResult = passwordResult + str(random.randrange(1, 9999))
        passwordResult = passwordLengthCheck(passwordResult, passwordLengthLimit)
        return passwordResult
# hard password generator
    elif passwordDiffPick == "3" or passwordDiffPick == "hard":
        pickedNumbers = []
        pickedWords = []
        pickedStrings = []
        passwordResult = ""
        for _ in range(random.randrange(2, 4)):
            pickedNumbers.append(str(random.randrange(1, 9999)))
        for _ in range(random.randrange(2, 7)):
            pickedWords.append(random.choice(list(orientations.values()))(random.choice(passgenwords)))
        for _ in range(random.randrange(2, 4)):
            pickedStrings.append(str("".join(random.sample(passgenindex, k=random.randrange(3, 8)))))
        passwordElements = pickedNumbers + pickedWords + pickedStrings
        random.shuffle(passwordElements)
        for _ in range(0, len(passwordElements)):
            passwordResult = passwordResult + passwordElements[0]
            passwordElements.pop(0)
        passwordResult = passwordLengthCheck(passwordResult, passwordLengthLimit)
        return passwordResult

while True:
    generatedPassword = main()
    print(f"Your password result: {generatedPassword}")
    retryCheck = input("Do you wish to generate a new one? (y/n): ")
    if retryCheck.lower() == "n":
        print("> Program closing. Have a good day.")
        break
