def count_words_in_file(MYFILE):
    try:
        with open(MYFILE, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"

MYFILE = input("Enter the MYFILE (with extension): ")
result = count_words_in_file(MYFILE)

print("Word Count:" if isinstance(result, int) else "Error:", result)
