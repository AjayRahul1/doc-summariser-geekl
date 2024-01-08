# Short & Sweet -  Document Summariser using Generative AI

## Version 0.3.0

- 🧑🏻‍💻 This application uses `OpenAI` - `Prompt Completion`, `Chat Completion` APIs and `Cohere` - `Co.summary` API and displays summary for the given input story or an essay provided with a hidden easter 🥚.
- 🖥️ This is a `responsive website` that gets adjusted according to screen size.

## Yet to be implemented

- [x] Use `HTMX` for great User Experience (UX) and faster loading times.
- [x] Responsive Website for Desktop and Mobile.
- [x] Connect with APIs that were being used.
- [x] Displaying Statistics & Metrics for the input and output.
- [ ] Translation for the summary (output)
- [ ] Word Cloud

## Views

| Desktop View of Summary Page | Mobile View of Summary Page |
| :---: | :---: |
| Cars Movie Summary Screenshot in Desktop View ![Cars Movie Summary Screenshot in Desktop View](/Screenshots/Cars_2006_story_summary_desktop.png) Desktop View of Summary Page ![Desktop View of Summary Page](/Screenshots/eg1_desktop_view_summary_page.png) | Mobile View of Summary Page ![Mobile View of Summary Page](/Screenshots/eg1_mobile_view_summary_page.png) |

## ♥ Developed by

- Ajay Rahul • [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=plastic&logo=github&logoColor=white)](https://github.com/AjayRahul1/)
- Rajesh Kuchhadia • [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=plastic&logo=github&logoColor=white)](https://github.com/Rajesh250822)
- Shaik Shaarikh • [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=plastic&logo=github&logoColor=white)](https://github.com/Ryuuichi-567)
- Hamsini Pulugurtha • [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=plastic&logo=github&logoColor=white)](https://github.com/hamsinipulugurtha)

## Steps to Clone, Install, `Run` the project

### Cloning the project locally

For HTTPS Method,

```sh
# Cloning the GitHub Repository
git clone https://github.com/AjayRahul1/doc-summariser-geekl.git

# Going into the directory
cd doc-summariser-geekl/
```

For SSH Method (Prefer this only if SSH Key was setup on your computer),

```sh
# Cloning the GitHub Repository
git clone git@github.com:AjayRahul1/doc-summariser-geekl.git

# Going into the directory
cd doc-summariser-geekl/
```

### For Windows

#### Create a virtual environment with Python 3.11.x version

##### Python Version 3.11 Installation

- Go to [Python Official Downloads](https://www.python.org/downloads/) Page (or) Click [here](https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe) to download Python 3.11.7 installer directly.
- Download 3.11.x version (x can be any number you find there)
- Run the installer file.
- Check tick the `Add Python to PATH`.
- During installation, make sure to select the option `Customize installation`.
- Choose a unique installation directory for Python 3.11.x to avoid overwriting your existing Python version 3.x.x installation.
- If 'Add Python to Path' is `not` checked, open PATH Environment Variables and edit PATH variable by adding Python 3.11 version.

- Verify Python Version
  - `py -3.11 --version`

##### Creation of Virtual Environment

- `py -3.11 -m venv venv`
- Activating Virtual Environment
  - In Windows 10, Open Powershell (or) In Windows 11, Windows Terminal. 
  - `venv\Scripts\Activate`
  - If you face any `error` with this command, it's because Microsoft disables Running Scripts by default.
  - To enable it temporarily, we run following command and try above command again.
    - `powershell -ExecutionPolicy bypass`

##### Installing Requirements

- Check whether you can see (venv) in the terminal that gives the sign of successful virtual environment activation
- `pip install -r requirements.txt`
- Take a moment of rest and comeback later while the requirements gets installed.

##### Setting Environment Variables
- Create an API KEY on [Cohere Dashboard](https://dashboard.cohere.com/api-keys) and copy it.
- `setx COHERE_API_KEY="your_api_key"`

##### Run the project on LocalHost

- `flask --app main run`
- Open [LocalHost](http://127.0.0.1:5000/) on your computer
- `Optional`: You can change the port number as per your wish.

> The Summarizer is at your feet now. Summarize whatever you need.

### For Linux (CLI Commands)

- First go to the folder where you want to clone using `cd your-directory-path/`
- Then copy below commands in your terminal in Linux. All done.

Ubuntu

```sh
# Installing Python 3.11.x
sudo apt install python3.11
# Verifying Python v3.11
python3.11 --version
# Create Virtual Environment with name 'venv'
python3.11 -m venv venv
# Activating Virtual Environment
source venv/bin/activate
# Installing Requirements
pip install -r requirements.txt
# Setting Environment Variables
export COHERE_API_KEY="your_key_here"
# Run the project on LocalHost
flask --app main run
```

Fedora

```sh
# Installing Python 3.11.x
sudo dnf install python3.11
# Verifying Python v3.11
python3.11 --version
# Create Virtual Environment with name 'venv'
python3.11 -m venv venv
# Activating Virtual Environment
source venv/bin/activate
# Installing Requirements
pip install -r requirements.txt
# Setting Environment Variables
export COHERE_API_KEY="your_key_here"
# Run the project on LocalHost
flask --app main run
```
