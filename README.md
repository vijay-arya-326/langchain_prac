(Project) LangChain Practice

This repository contains small experiments and notebooks for working with LangChain-related libraries.

**Run Instructions**
- **Prerequisite**: Python >= 3.12 installed.
- **Create venv**: run the commands below from the repository root.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

macOS / Linux (bash):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

- **Install dependencies** (example using `pip`):

```powershell
pip install python-dotenv ipykernel langchain-core langchain-openai langgraph \
	langgraph-checkpoint-sqlite "langsmith[claude-agent-sdk]" mlflow
```

- **Environment variables**: copy `sample.env` to `.env` and update any keys needed (API keys, etc.). The code uses `python-dotenv` to load env vars where applicable.
- **Run scripts**: examples from the project root

```powershell
# Run the users management script
py .\users.py add <username>

# Run a notebook server to explore .ipynb files
jupyter lab
```

- **Notebooks**: open the notebooks under `module1/`, `module2/`, `module3/` in Jupyter Lab/Notebook.

- **Notes**:
	- The project `pyproject.toml` lists the intended dependencies and Python version. If you use a dependency manager (Poetry), prefer that workflow.
