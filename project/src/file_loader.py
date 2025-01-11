import os

def load_php_snippets(base_path):
    snippets = {"secure": [], "vulnerable": []}
    for category in ["secure", "vulnerable"]:
        dir_path = os.path.join(base_path, category)
        for file_name in os.listdir(dir_path):
            if file_name.endswith(".php"):  # Only load PHP files
                file_path = os.path.join(dir_path, file_name)
                with open(file_path, 'r') as file:
                    snippets[category].append({
                        "file_name": file_name,
                        "content": file.read()
                    })
    return snippets

# Example usage
if __name__ == "__main__":
    base_path = "./data"
    snippets = load_php_snippets(base_path)
    print(f"Loaded {len(snippets['secure'])} secure files and {len(snippets['vulnerable'])} vulnerable files.")
