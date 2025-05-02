# K-Agent

K-Agent is an intelligent assistant powered by advanced AI technology, built with Streamlit.

## Features

- 🧠 Intelligent conversation
- 📝 Task automation
- 🔍 Information retrieval
- 🛠️ Tool integration

## Installation

1. Clone the repository:
```bash
git clone https://github.com/krackn88/K-Agent.git
cd K-Agent
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your configuration:
```env
OPENAI_API_KEY=your-api-key
APP_DEBUG=false
DATABASE_URL=sqlite:///app.db
```

5. Run the application:
```bash
streamlit run main_app.py
```

## Project Structure

- `main_app.py`: Main Streamlit application
- `requirements.txt`: Project dependencies
- `.gitignore`: Git ignore rules
- `.env`: Environment variables (not tracked in git)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.