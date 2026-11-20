# Dash Hello World

A beginner introduction to Plotly Dash: step-by-step examples in `steps/`, then an exercise in `app.py`.

## Prerequisites

- Python 3.13 or newer. Production runs 3.13. Check with:

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

## 5. Walk through the steps

The `steps/` folder builds a small app one idea at a time where we will make small modifications to change the behaviour of the Dash app. Run each one from the repo root,
open <http://127.0.0.1:5050> in your browser, and compare it with the previous step:

| Step | What it adds |
|---|---|
| `python steps/step_1_hello.py` | The smallest Dash app: a heading and a paragraph |
| `python steps/step_2_components.py` | A button, a text input and a card |
| `python steps/step_3_callback.py` | A callback: clicking the button updates the card |
| `python steps/step_4_state.py` | `State` and `prevent_initial_call` |
| `python steps/step_5_duplicate_outputs.py` | Two callbacks updating the same output with `allow_duplicate` |

Stop each one with `Ctrl+C` before starting the next.

Because the apps run with `debug=True`, the page reloads automatically when you save changes to the file.

## 6. The exercise

Build a trigonometry explorer in `app.py`. The maths (`compute_trig`) and the plotting
(`make_figure`) are already written. Your job is the **layout** and the **callback**: follow the
`TODO` comments.

```bash
python app.py
```

Open <http://127.0.0.1:5050> again. Stuck? `suggested_solution.py` has one way to do it.

### Set the app title

The heading comes from the `APP_TITLE` environment variable. To try it locally in PowerShell:

```powershell
$env:APP_TITLE = "Wave explorer"
```

```powershell
python app.py
```

When you publish the app, set `APP_TITLE` in the dashboard's configuration in 4insight instead. If it isn't set, the heading is **My trigonometry app** by default.

## 7. Stop the app

Press `Ctrl+C` in the terminal.

To leave the virtual environment, run:

```bash
deactivate
```

## Resources

### How to use Dash

- Dash tutorial: [Part 1. Layout | Plotly Dash](https://dash.plotly.com/layout)
- Dash callbacks: [Basic Callbacks | Plotly Dash](https://dash.plotly.com/basic-callbacks)
- Debugging and dev tools: [Dev Tools | Plotly Dash](https://dash.plotly.com/devtools)
- Questions and answers: [Plotly Community Forum](https://community.plotly.com/)

### Dash UI components

- Dash core components (`dcc`): [Dash Core Components | Plotly Dash](https://dash.plotly.com/dash-core-components)
- Dash Bootstrap components (`dbc`): [Components - dbc docs](https://www.dash-bootstrap-components.com/docs/components/)
