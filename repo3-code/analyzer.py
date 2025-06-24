import argparse
import fitz  # PyMuPDF
import re

# Define the skills you want to check for
key_skills = [
    "Python", "SQL", "Machine Learning", "Deep Learning", "Data Analysis",
    "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "NLP", "Git"
]

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
    return text

def count_skills(text, skills):
    skill_counts = {}
    for skill in skills:
        pattern = rf'\b{re.escape(skill)}\b'
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        skill_counts[skill] = len(matches)
    return skill_counts

def suggest_improvements(skill_counts):
    missing = [skill for skill, count in skill_counts.items() if count == 0]
    return missing

def main():
    parser = argparse.ArgumentParser(description="📄 Resume Skill Analyzer Tool")
    parser.add_argument("--file", type=str, required=True, help="Path to the resume PDF file")

    args = parser.parse_args()

    print(f"🔍 Analyzing: {args.file}")
    text = extract_text_from_pdf(args.file)

    if not text.strip():
        print("⚠️ No text extracted from the PDF. Check the file.")
        return

    skill_counts = count_skills(text, key_skills)

    print("\n✅ Skill Mentions Found:")
    for skill, count in skill_counts.items():
        print(f"- {skill}: {count}")

    suggestions = suggest_improvements(skill_counts)
    if suggestions:
        print("\n💡 Suggested Skills to Add or Highlight:")
        for skill in suggestions:
            print(f"- {skill}")
    else:
        print("\n🎉 Great! All key skills are present in your resume.")

if __name__ == "__main__":
    main()
