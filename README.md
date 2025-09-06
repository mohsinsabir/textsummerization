## Text Summarization (Streamlit + Hugging Face)

A simple Streamlit web app for abstractive text summarization using Hugging Face Transformers. The default model is `facebook/bart-large-cnn`.

### Features
- **Web UI**: Paste text and get a concise summary with one click
- **Pretrained model**: Uses a state-of-the-art summarization model out of the box
- **Configurable**: Swap in any compatible summarization model by editing one line

### Quickstart
1. Install Python 3.9+ (3.10 recommended)
2. Create and activate a virtual environment
   - Linux/macOS:
     - `python3 -m venv .venv && source .venv/bin/activate`
   - Windows (PowerShell):
     - `python -m venv .venv; .\.venv\Scripts\Activate.ps1`
3. Install dependencies
   - `pip install --upgrade pip`
   - `pip install -r requirements.txt`
4. Run the app
   - `streamlit run app.py`
5. Open the URL printed in the terminal (usually `http://localhost:8501`).

On first run, the model weights will download automatically and be cached.

### Usage
1. Enter or paste text in the input area
2. Click "Summarize"
3. Read the generated summary below the button

### Configuration
- Change the model by editing `model_name` in `app.py`:
  - Example: `model_name = "sshleifer/distilbart-cnn-12-6"`
- You can also adjust generation parameters inside `app.py` (e.g., `max_length`, `min_length`, `do_sample`).

### Requirements
- Declared in `requirements.txt`:
  - `streamlit==1.26.0`
  - `transformers==4.33.2`
  - `torch>=1.9.0`

GPU is optional. If you have CUDA, install a CUDA-enabled PyTorch build from the official instructions.

### Project structure
```
app.py            # Streamlit app entry point
requirements.txt  # Python dependencies
LICENSE           # MIT License
README.md         # This file
```

### License
MIT — see `LICENSE` for details.

### Acknowledgments
- Hugging Face Transformers
- Facebook AI for `BART`