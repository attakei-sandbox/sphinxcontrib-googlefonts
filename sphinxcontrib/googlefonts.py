# flake8: noqa
from typing import Any


__version__ = "0.1.0"


def add_fonts_context(
    app: "Sphinx", pathname: str, templatename: str, context: dict, doctree: Any
) -> None:
    if len(app.config.googlefonts_families) == 0:
        return
    css_files = context.get("css_files", [])
    for family in app.config.googlefonts_families:
        href = f"https://fonts.googleapis.com/css2?family={family}"
        css_files.append(href)
    context["css_files"] = css_files


def setup(app):
    app.add_config_value("googlefonts_families", [], "html")
    app.connect("html-page-context", add_fonts_context)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
