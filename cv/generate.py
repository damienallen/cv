from pathlib import Path
from shutil import copytree, rmtree

import typer
from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML

from cv.contents import load_cv

ROOT_DIR = Path(__file__).parents[1]
TEMPLATES_DIR = ROOT_DIR / "templates"
CONTENTS_PATH = ROOT_DIR / "contents.yml"

DIST_DIR = ROOT_DIR / "dist"
HTML_PATH = DIST_DIR / "cv.html"
PDF_PATH = DIST_DIR / "damien_allen_cv.pdf"

jinja_env = Environment(
    loader=FileSystemLoader("templates"), autoescape=select_autoescape()
)


def main(
    contents_path: Path = CONTENTS_PATH,
):
    contents = load_cv(contents_path)
    print(f"Loading CV contents ({contents_path})")

    if DIST_DIR.exists():
        rmtree(DIST_DIR)
    DIST_DIR.mkdir(exist_ok=True)

    # Copy linked assets
    copytree(TEMPLATES_DIR / "assets", DIST_DIR / "assets")

    # Write HTML output
    print(f"Rendering HTML: {HTML_PATH}")
    template = jinja_env.get_template("cv_template.html")
    rendered_cv = template.render(
        bio=contents.bio,
        education=contents.education,
        language=contents.language,
        work=contents.work,
        skills=contents.skills,
    )

    with open(HTML_PATH, "w+") as f:
        f.write(rendered_cv)

    # Write rendered PDF
    print(f"Rendering PDF: {PDF_PATH}")
    with open(HTML_PATH) as f:
        HTML(f).write_pdf(PDF_PATH)


if __name__ == "__main__":
    typer.run(main)
