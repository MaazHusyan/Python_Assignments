SENTENCE =  "GIAIC is fun. I learned to program and used Python to make my"
def main():
    noun = input("Enter a noun (e.g., cat, bike, apple): ")
    verb = input("Enter a verb (e.g., jump, crawl, blink): ")
    adjective = input("Enter an adjective (e.g., nasty, jiggly, funny etc..): ")

    print(f"{SENTENCE} {adjective} {noun} {verb}.")
    
if __name__ == '__main__':
    main()
