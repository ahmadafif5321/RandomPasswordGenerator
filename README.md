# Random Password Generator

A small Python learning project: generate a random password of a requested length, implemented four ways — as a CLI script, a commented beginner version, a Tkinter GUI, and a Flask web app.

## What and why

My company requires a monthly password change, so I wrote a script to generate new passwords instead of inventing them myself. It started as a one-function CLI script and grew into a few variants of the same idea as I experimented with different Python interfaces.

The project later evolved into a hosted web app built with Streamlit — see [PasswordGeneratorStreamlite](https://github.com/ahmadafif5321/PasswordGeneratorStreamlite).

## Quick start

All variants share the same core: pick random characters from `string.ascii_letters + string.digits + string.punctuation` (default length 12).

**CLI** (no dependencies, prints one password):

```bash
python basicPasswordGen.py
```

**Commented beginner version** (same output, step-by-step comments):

```bash
python alternative
```

**Tkinter GUI** (enter a length, generate, copy to clipboard):

```bash
python GUI_Password_Generate.py
```

**Flask web app** (form-based page with a copy-to-clipboard button):

```bash
pip install Flask
python FlaskPassGen.py
```

Then open `http://localhost:5000`. A `Procfile` (`web: python FlaskPassGen.py`) is included for Heroku-style deployment; the port is read from the `PORT` environment variable.

Note: `requirements.txt` is a full environment freeze and includes packages unrelated to this project. Only Flask (and its dependencies) is actually needed, and only for the Flask variant — the CLI and Tkinter versions use the standard library alone.

## How it works

Every variant uses the same function:

```python
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
```

The variants only differ in how the length is supplied and the result displayed: hardcoded default (CLI), a Tkinter entry field, or an HTML form rendered by Flask (`templates/index.html`).

## Honest limitations

- Uses Python's `random`, which is not cryptographically secure; `secrets.choice` would be the correct choice for real credentials.
- No guarantee that every character class appears in the output.
- No tests or input validation (e.g., non-numeric length input will raise an error in the GUI/Flask versions).

## Tech stack

- Python standard library: `random`, `string`, `tkinter`
- Flask + Jinja2 template (web variant)
