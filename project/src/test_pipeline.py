from file_loader import load_php_snippets
from generate_instructions import generate_debugging_instructions
from apply_instructions import apply_debugging_instructions
from validation import validate_sql_injection

if __name__ == "__main__":
    model_url = "http://localhost:11434/api/generate"
    base_path = "./data"
    # Load Snippets
    snippets = load_php_snippets(base_path)
    vulnerable_code = snippets["vulnerable"][0]["content"]
    secure_code = snippets["secure"][0]["content"]

    # Generate Instructions
    instructions = generate_debugging_instructions(vulnerable_code, secure_code, model_url)
    print("Debugging Instructions:", instructions)

    # Apply Instructions to Unseen Code
    unseen_vulnerable_code = snippets["vulnerable"][1]["content"]
    generated_secure_code = apply_debugging_instructions(unseen_vulnerable_code, instructions, model_url)
    print("Generated Secure Code:", generated_secure_code)

    # Validate Code
    is_valid = validate_sql_injection(generated_secure_code)
    print("Validation Result:", "Pass" if is_valid else "Fail")
