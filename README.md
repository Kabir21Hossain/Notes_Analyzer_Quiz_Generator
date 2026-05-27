# Practice Project

A small Python practice repository for working with APIs, text/audio processing, and image handling.

## Live Demo

- Visit the live app: https://notesquizexam.streamlit.app/

## Project Structure

- `main.py` - Project entry point or example runner.
- `call_api.py` - API request helper or integration sample.
- `text_audio.py` - Text and audio-related utilities or demonstration code.
- `working_images.py` - Image processing or handling examples.
- `Images/` - Directory for image assets used by the project.
- `design/` - Directory with UI / flow screenshots for the app.
- `requirements.txt` - Python dependencies.

## Design Screenshots

Screenshots from the `design/` folder in order:

1. `./design/1.png`
2. `./design/2.png`
3. `./design/3.png`
4. `./design/4.png`

### Preview Images

![Design step 1](design/1.png)

![Design step 2](design/2.png)

![Design step 3](design/3.png)

![Design step 4](design/4.png)

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the environment:
   - Windows PowerShell:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - Windows CMD:
     ```cmd
     .\.venv\Scriptsctivate.bat
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:

```bash
python main.py
```

For other modules, run them directly as needed, for example:

```bash
python call_api.py
```

## Notes

- Keep `.env` and virtual environment files out of version control.
- Customize `requirements.txt` as dependencies change.
