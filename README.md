# Dash Grocery docs

A small, single-page guide to [Dash Grocery](https://github.com/IcToxi/dash-grocery):
installation, a quick example, and a list of the available components.

## Run locally

Use Python 3.10 or later:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open the local URL printed by Dash. On Windows, activate the environment with
`.venv\Scripts\activate`.

To use Conda instead:

```bash
conda env create -f environment.yaml
conda activate dash-grocery-docs
python app.py
```

The page layout is in `app.py`; its responsive styles are in
`assets/style.css`.
