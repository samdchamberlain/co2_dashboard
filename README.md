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

# Directly re-run the data extraction

From the base directory the following commands on Terminal will get you to the right path and execute.
  1. `cd co2_dashboard`
  2. `poetry run python load_data.py`