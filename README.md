# EthicalLogger

**EthicalLogger** is a very basic Python script for quickly generating short, professional PDF reports of ethical discovery activities.

It helps ethical hackers, OSINT researchers, and cybersecurity professionals easily log essential details like the discovery date, method, description, actions taken, and confirm responsible behavior through a simple checklist.

---

## Features
- 📝 Basic and lightweight Python script.
- 🗓️ Automatically fills today's date.
- 🧾 Structured fields for discovery details and notes.
- ✅ Ethical behavior checklist included.
- 📄 Clean, single-page PDF output.
- ⚡ No dependencies on heavy frameworks or databases.

---

## Usage

1. Make sure you have Python 3 installed.
2. Install `fpdf2` if not already:

```bash
pip install fpdf2 --break-system-packages

run the script: python3 generatelog.py
A new PDF will be generated automatically with a filename like: DISCOVERY-20250428-0001.pdf in logs
