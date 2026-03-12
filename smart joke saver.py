import requests

try:
    response = requests.get("https://official-joke-api.appspot.com/random_joke")

    if response.status_code == 200:
        data = response.json()
        joke = data["setup"] + " - " + data["punchline"] + "\n"

        with open("jokes.txt", "a") as file:
            file.write(joke)

        print("Joke saved successfully!")
    else:
        print("Could not fetch joke. Try again.")

except:
    print("Something went wrong. Check your internet connection.")