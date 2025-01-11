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






