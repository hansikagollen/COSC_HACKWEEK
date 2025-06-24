# 📄 Resume Analyzer CLI Tool

A Python-based command-line tool that:
- 🔍 Extracts text from a resume in PDF format
- 📊 Detects and counts mentions of key technical skills
- 💡 Suggests improvements based on missing or low-frequency skills

This project is built using `PyMuPDF` for text extraction and `argparse` for the command-line interface.

---

## 🚀 Features

✅ Extracts full resume text from PDF  
✅ Counts key skill mentions (e.g., Python, SQL, ML, etc.)  
✅ Highlights missing skills as suggestions  
✅ Clean CLI experience with `argparse`  
✅ Works offline, no API needed

---

## 🛠️ Technologies Used

- **Python 3.7+**
- **PyMuPDF** (`fitz`)
- `argparse`
- `re` (regular expressions)

---

## 📂 File Structure

resume-analyzer-cli/
├── analyzer.py # Main CLI script
├── README.md # Project documentation
└── output_screenshots/
└── sample_output.png # CLI result screenshot


---

## 🧠 Skills Checked

The tool currently checks for the following skills (can be extended easily):

- Python
- SQL
- Machine Learning
- Deep Learning
- Data Analysis
- Pandas
- NumPy
- Scikit-learn
- TensorFlow
- NLP
- Git

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install PyMuPDF

python analyzer.py --file "hansika gollen resume updated.pdf"


