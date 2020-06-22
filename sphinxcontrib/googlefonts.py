# flake8: noqa
from typing import Any, List, Tuple
from urllib.parse import quote_plus, urlencode

if False:
    # For type annotation
    from sphinx.application import Sphinx


__version__ = "0.1.1"


def build_family_query(families: List[str]) -> List[Tuple[str, str]]:
    """Convert from font family information to query.

    :param families: Fornt family from sphinx config
    :returns: query context key-value pairs
    """
    return [("family", quote_plus(f)) for f in families]


def add_fonts_context(
    app: "Sphinx", pathname: str, templatename: str, context: dict, doctree: Any
) -> None:
    if len(app.config.googlefonts_families) == 0:
        return
    css_files = context.get("css_files", [])
    query = build_family_query(app.config.googlefonts_families)
    href = f"https://fonts.googleapis.com/css2?{urlencode(query)}"
    css_files.append(href)
    context["css_files"] = css_files


def setup(app: "Sphinx"):
    app.add_config_value("googlefonts_families", [], True)
    app.connect("html-page-context", add_fonts_context)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
