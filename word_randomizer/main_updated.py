import random

def load_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            entries = file.read().strip().split("\n\n")
            words = [
                (
                    entry.split("\n")[0].split(".")[1].strip(),  # Kelime
                    entry.split("\n")[1].split("Definition:")[1].strip(),  # Tanım
                    "\n".join(entry.split("\n")[2:]).replace("Examples:", "").strip()  # Örnekler
                )
                for entry in entries if len(entry.split("\n")) > 1
            ]
            return words
    except Exception as e:
        print(f"Error loading file: {e}")
        return []


file_path = "your_file_path.txt"
words = load_words(file_path)


if words:
    word, definition, examples = random.choice(words)
    print(f"Word: {word}\nDefinition: {definition}\nExamples:\n{examples}")
else:
    print("No words available.")