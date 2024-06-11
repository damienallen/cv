import typer
from contents import load_cv
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from shutil import copy

ROOT_DIR = Path(__file__).parent
TEMPLATES_DIR = ROOT_DIR / "templates"
CONTENTS_PATH = ROOT_DIR / "contents.yml"

DIST_DIR = ROOT_DIR / "dist"
DIST_DIR.mkdir(exist_ok=True)
OUTPUT_PATH = DIST_DIR / "cv.html"


def main(
    contents_path: Path = CONTENTS_PATH,
    output_path: Path = OUTPUT_PATH,
):
    jinja_env = Environment(
        loader=FileSystemLoader("templates"), autoescape=select_autoescape()
    )

    print("Loading CV template")
    template = jinja_env.get_template("cv_template.html")

    contents = load_cv(contents_path)
    print(f"Loading CV contents: {contents_path}")

    print("Rendering HTML output")
    rendered_cv = template.render()

    print(f"Saved to: {output_path}")
    copy(TEMPLATES_DIR / "cv.css", DIST_DIR / "cv.css")
    with open(output_path, "w") as f:
        f.write(rendered_cv)


if __name__ == "__main__":
    typer.run(main)
