import time

def typewriter(text, delay=0.05):
    for char in text:
        # print each character, prevent a new line, and force immediate output
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Print a final newline after the text finishes
def nontypewriter(text):
  print(text)
