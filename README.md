# Install package

Follow these steps. You need `pyenv` and `poetry` installed within a specific Python env
  1. Install pyenv (see instructions here: https://github.com/pyenv/pyenv)
    - `curl https://pyenv.run | bash`
    - If the above command alone isn't enough try the bash commands here (https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv)
  2. Get Python 3.9.5 in pyenv `pyenv install 3.9.5`
  3. Create a venv using 3.9.5 `pyenv virtualenv 3.9.5 co2_dashboard `
  4. Activate venv `pyenv activate co2_dashboard`
  5. Install poetry in venv `pip install poetry`
  6. Now you can install the env with `poetry install`

# Run the dashboard locally
  - `poetry run streamlit run app.py`

If it doesn't pop up automatically in Chrome, copy paste the `Local URL:` from Terminal into a Chrome tab

# Access the Jupyter dev notebook
You can access the notebook used in dev with the following command
  - `poetry run jupyter lab`

This will activate a Jupyter Notebook environment where you can run commands in the attached `testing_notebook.ipynb`