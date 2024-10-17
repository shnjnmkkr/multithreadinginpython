import json
import urllib.request
import time


def count_letters(url, frequency):
    response = urllib.request.urlopen(url)
    txt = str(response.read())
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter]=0


def main():
    frequency = {}
    start = time.time()
    for i in range(1000, 1020):
        count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
    end = time.time()
    sorted_freq = dict(sorted(frequency.items()))
    print(json.dumps(sorted_freq, indent=4))
    print("Done, time taken", end - start)


main()
