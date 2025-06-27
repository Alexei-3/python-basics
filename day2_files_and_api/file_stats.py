def get_file_stats(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.splitlines()
    words = text.split()
    return {
        "lines": len(lines),
        "words": len(words),
        "characters": len(text)
    }
stats = get_file_stats("day2_files_and_api/sample.txt")
print(" File statistics:")
print(f"Lines: {stats ['lines']}")
print(f"Words: {stats['words']}")
print(f"Characters: {stats['characters']}")