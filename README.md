# Dash Hello World

A minimal Plotly Dash app to use as the starting point for the training session.

## Prerequisites

- Python 3.9 or newer. Check with:

  ```bash
  python --version
  ```

  On macOS/Linux you may need to use `python3` instead of `python` in the commands below.
- [Git](https://git-scm.com/downloads) and a free [GitHub](https://github.com/signup) account.

## 1. Get your own copy of the code

You can't push to this repository directly. Instead you make a **fork**: your own copy on
GitHub that you are free to change.

1. On this repository's GitHub page, click **Fork** (top right), then **Create fork**.
   GitHub creates `https://github.com/<your-username>/<repo-name>`.
2. On **your fork's** page, click the green **Code** button and copy the HTTPS URL.
3. Clone your fork to your computer and go into the folder:

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   ```

   ```bash
   cd <repo-name>
   ```

Everything you change and push from here goes to your fork, not to this repository.

### Optional: get the latest updates

To pull in changes made here after you forked, open your fork on GitHub and click
**Sync fork**, then run `git pull` in your local folder.

## 2. Create a virtual environment

In the folder you just cloned, run:

```bash
python -m venv .venv
```

This creates a folder called `.venv` that holds a separate Python installation for this project.

## 3. Activate the virtual environment



```cmd
.venv\Scripts\activate
```


When it is active, you will see `(.venv)` at the start of your terminal prompt.

> If PowerShell says running scripts is disabled, run
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.

## 4. Install the dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the app

```bash
python app.py
```

Open <http://127.0.0.1:8050> in your browser. You should see **Hello, World!**

Because the app runs with `debug=True`, the page reloads automatically when you save changes to `app.py`.

## 6. Stop the app

Press `Ctrl+C` in the terminal.

To leave the virtual environment, run:

```bash
deactivate
```
