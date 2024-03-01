languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
lang1 = 'Rust'
for lang in languages:
    if lang.lower() == lang1.lower():
        print("This language is in the list")
        break
