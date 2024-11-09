Here's a sample README documentation for your project named **SleepForge**:

---

# SleepForge

**SleepForge** is a desktop Python application for processing actigraphy data from Condor `.txt` files and exporting results into a structured CSV format. It enables researchers, clinicians, and users interested in sleep and activity tracking to transform raw actigraphy data into a readable and analyzable format.

## Features

- **Data Processing**: Reads and processes actigraphy data from Condor `.txt` files.
- **CSV Export**: Exports processed data into a convenient CSV format for analysis.
- **Flexible Analysis**: Compatible with multiple actigraphy data points and customizable for varied study requirements.
- **User-Friendly Interface**: Easy-to-navigate interface with simple controls for importing and exporting data.

Here's the updated Installation section with steps to create a virtual environment and install dependencies:

---

## Installation

1. **Clone the Repository**:

```sh
git clone https://github.com/username/SleepForge.git
cd SleepForge
```

2. **Create a Virtual Environment**:

```sh
python -m venv venv
```

3. **Activate the Virtual Environment**:

On **Windows**:
```sh
venv\Scripts\activate
```

On **macOS/Linux**:
```sh
source venv/bin/activate
```

4. **Install Dependencies**:

With the virtual environment activated, install the required packages from `requirements.txt`:

```sh
pip install -r requirements.txt
```

5. **Run SleepForge**:

Once dependencies are installed, you can run the application:

```sh
python main.py
```

---

This setup will ensure you’re running SleepForge in an isolated environment with all necessary dependencies installed. Let me know if you need any further adjustments!-m venv venv