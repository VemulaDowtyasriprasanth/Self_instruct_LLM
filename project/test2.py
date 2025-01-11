import os
import subprocess

def create_and_add_gitignore(project_path, exclusions):
    """
    Creates a .gitignore file with specified exclusions and adds it to Git.

    Args:
        project_path (str): Path to the project directory.
        exclusions (list): List of directories or files to exclude.
    """
    gitignore_path = os.path.join(project_path, ".gitignore")

    # Ensure the project path exists
    if not os.path.exists(project_path):
        raise FileNotFoundError(f"Project path does not exist: {project_path}")

    # Write exclusions to the .gitignore file
    with open(gitignore_path, "w") as gitignore_file:
        gitignore_file.write("\n".join(exclusions))
    print(f".gitignore created with the following exclusions:\n{exclusions}")

    # Add .gitignore to Git
    try:
        subprocess.run(["git", "add", ".gitignore"], check=True, cwd=project_path)
        subprocess.run(["git", "commit", "-m", "Add .gitignore to exclude specified files"], check=True, cwd=project_path)
        print(".gitignore added and committed to Git.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding .gitignore to Git: {e}")

if __name__ == "__main__":
    # Update project_path to your actual project directory
    project_path = r"C:\Users\wwwdo\Desktop\Final Project\project"

    # Directories or files to exclude
    exclusions = [
        "env_name/",
        "virtual_llm/",
        "*.lib",
        "*.dll",
        "__pycache__/",
        "*.log"
    ]

    # Run the function
    create_and_add_gitignore(project_path, exclusions)
