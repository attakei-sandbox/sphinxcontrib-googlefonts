from pathlib import Path
from typing import AnyStr

from bs4 import BeautifulSoup
from sphinx_testing import TestApp, with_app


def gen_app_conf(**kwargs: dict) -> dict:
    """Create TestApp configuration."""
    kwargs["buildername"] = "html"
    kwargs["srcdir"] = str(Path(__file__).parent / "testdoc")
    kwargs["copy_srcdir_to_tmpdir"] = True
    return kwargs


def soup_html(app: TestApp, path: str) -> BeautifulSoup:
    """Build application and parse content."""
    app.build()
    html: AnyStr = (app.outdir / path).read_text()
    return BeautifulSoup(html, "html.parser")


@with_app(**gen_app_conf(confoverrides={}))
def test_script_tags(app: TestApp, status, warning):  # noqa
    soup_html(app, "index.html")
