# Self_instruct_LLM
This project implements a Proof of Concept (PoC) using Large Language Models (LLMs) like Llama2 to debug and secure PHP code by addressing SQL Injection vulnerabilities. It automates tasks such as loading PHP snippets, generating debugging instructions, applying them to secure code, and validating results, showcasing LLM-driven vulnerability 
# Secure Code Debugging with LLMs

This project demonstrates a Proof of Concept (PoC) for using Large Language Models (LLMs) to automate the process of identifying and mitigating **SQL Injection vulnerabilities** in PHP code. It focuses on loading vulnerable and secure PHP snippets, generating debugging instructions, and transforming insecure code into secure versions.

---

## **Project Features**

1. **Code Parsing and Loading**:
   - Secure and vulnerable PHP code snippets are loaded dynamically from the dataset.

2. **Generate Debugging Instructions**:
   - Step-by-step instructions are generated to transform vulnerable code into secure code using LLMs.

3. **Secure Code Generation**:
   - The LLM uses debugging instructions and vulnerable code to produce secure PHP code.

4. **Validation**:
   - Generated secure code is validated against expected functionality to ensure vulnerabilities are mitigated.

---

## **Getting Started**

### **Prerequisites**

1. Python (>=3.8)
2. A running instance of a Local LLM (e.g., Llama2 API).
3. PHP (optional, for manual validation).

### **Folder Structure**

```plaintext
project/
│
├── config/
│   ├── .env                # Environment variables
│   ├── config.yaml         # Configuration for the project
│
├── data/
│   ├── secure/             # Secure PHP snippets
│   ├── vulnerable/         # Vulnerable PHP snippets
│
├── src/
│   ├── file_loader.py      # Script to load PHP snippets
│   ├── generate_instructions.py # Generates debugging instructions
│   ├── apply_instructions.py    # Applies instructions to generate secure code
│   ├── validation.py       # Validation logic
│
├── local_database/
│   ├── vector_store.db     # Optional local database
│
├── debugging_instructions.txt # Generated debugging instructions
├── generated_secure_code.php  # Generated secure PHP code
├── README.md               # Project description
├── requirements.txt        # Required Python dependencies





Here is the project description and a draft for the README.md file:

Project Description
This project demonstrates a Proof of Concept (PoC) for leveraging Large Language Models (LLMs) to automate the debugging and generation of secure code from vulnerable PHP snippets. It primarily focuses on addressing SQL Injection vulnerabilities, converting insecure PHP code into secure versions using debugging instructions provided by an LLM (e.g., Llama2). The project automates the following tasks:

Parsing and Loading Code:
Loads secure and vulnerable PHP snippets for SQL Injection from a structured dataset.
Generating Debugging Instructions:
Uses a secure-vulnerable code pair to generate step-by-step debugging instructions for securing the vulnerable code.
Applying Instructions:
Passes debugging instructions and unseen vulnerable code to the LLM to generate secure PHP code.
Validation:
Validates the generated secure code manually and through automated tests.
This workflow demonstrates how LLMs can assist developers in identifying and mitigating security vulnerabilities in legacy or poorly written code.

README.md
markdown
Copy code
# Secure Code Debugging with LLMs

This project demonstrates a Proof of Concept (PoC) for using Large Language Models (LLMs) to automate the process of identifying and mitigating **SQL Injection vulnerabilities** in PHP code. It focuses on loading vulnerable and secure PHP snippets, generating debugging instructions, and transforming insecure code into secure versions.

---

## **Project Features**

1. **Code Parsing and Loading**:
   - Secure and vulnerable PHP code snippets are loaded dynamically from the dataset.

2. **Generate Debugging Instructions**:
   - Step-by-step instructions are generated to transform vulnerable code into secure code using LLMs.

3. **Secure Code Generation**:
   - The LLM uses debugging instructions and vulnerable code to produce secure PHP code.

4. **Validation**:
   - Generated secure code is validated against expected functionality to ensure vulnerabilities are mitigated.

---

## **Getting Started**

### **Prerequisites**

1. Python (>=3.8)
2. A running instance of a Local LLM (e.g., Llama2 API).
3. PHP (optional, for manual validation).

### **Folder Structure**

```plaintext
project/
│
├── config/
│   ├── .env                # Environment variables
│   ├── config.yaml         # Configuration for the project
│
├── data/
│   ├── secure/             # Secure PHP snippets
│   ├── vulnerable/         # Vulnerable PHP snippets
│
├── src/
│   ├── file_loader.py      # Script to load PHP snippets
│   ├── generate_instructions.py # Generates debugging instructions
│   ├── apply_instructions.py    # Applies instructions to generate secure code
│   ├── validation.py       # Validation logic
│
├── local_database/
│   ├── vector_store.db     # Optional local database
│
├── debugging_instructions.txt # Generated debugging instructions
├── generated_secure_code.php  # Generated secure PHP code
├── README.md               # Project description
├── requirements.txt        # Required Python dependencies
Setup Instructions
Clone the repository:

bash
Copy code
git clone <repository_url>
cd project
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the .env file:

Set up your local LLM endpoint and any required API keys:
bash
Copy code
LLM_URL=http://localhost:11434/api/generate
Running the Project
1. Generate Debugging Instructions
Run the script to generate debugging instructions from the secure-vulnerable code pair:

bash
Copy code
python src/generate_instructions.py
Debugging instructions are saved in debugging_instructions.txt.
2. Apply Debugging Instructions
Use the generated instructions and vulnerable code to produce secure PHP code:

bash
Copy code
python src/apply_instructions.py
The generated secure code will be saved in generated_secure_code.php.
Example Output
Debugging Instructions (debugging_instructions.txt):

sql
Copy code
Step 1: Use prepared statements for SQL queries.
Step 2: Sanitize user input with filter_var().
Step 3: Replace raw SQL with bound parameters.
Generated Secure Code (generated_secure_code.php):

php
Copy code
$id = filter_var($_GET['id'], FILTER_SANITIZE_NUMBER_INT);

$conn = new mysqli("localhost", "root", "", "test_db");
$query = $conn->prepare("SELECT * FROM users WHERE id = ?");
$query->bind_param("i", $id);
$query->execute();
$result = $query->get_result();

if ($result->num_rows > 0) {
    echo "Record exists.";
} else {
    echo "No record found.";
}
Next Steps
Extend the dataset to include more categories of vulnerabilities (e.g., XSS, CSRF).
Automate the validation of generated secure code.
Explore scalability to handle larger projects or multi-file vulnerabilities.
Contributing
Feel free to fork this repository and submit pull requests. Contributions for improving the validation process or extending the dataset are welcome.

License
This project is open-source and licensed under the MIT License.

yaml
Copy code

---

This **README.md** file provides a complete description of your project, setup instructions, and an overview of the workflow. Let me kn
