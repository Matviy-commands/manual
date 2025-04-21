from markdown2 import markdown
from weasyprint import HTML
from pathlib import Path

# === Налаштування шляхів ===
base_dir = Path("docs")                      # Папка з markdown і зображеннями
md_file = base_dir / "manual.md"            # Markdown-файл
output_pdf = Path("EduBot_Manual.pdf")      # PDF на виході

# === Зчитування Markdown ===
with open(md_file, "r", encoding="utf-8") as f:
    md_text = f.read()

# === Конвертація в HTML ===
html_content = markdown(md_text)

# === Створення PDF (WeasyPrint сам обробляє зображення з відносних шляхів) ===
HTML(string=html_content, base_url=base_dir).write_pdf(output_pdf)

print(f"✅ PDF успішно згенеровано: {output_pdf}")
