from fasthtml.common import *


def site_header():
    return Header(
        Div(
            Nav(
                Div(A("Gustavo Navarro", href="/"), cls="logo"),
                Ul(
                    Li(A("Work", href="/#work")),
                    Li(A("About", href="/#about")),
                    Li(A("Writing", href="/blog")),
                    Li(A("Contact", href="/#contact")),
                    cls="nav-list",
                ),
            ),
            cls="container",
        )
    )


def site_footer(year):
    return Footer(
        Div(
            P(f"© {year} Gustavo Navarro"),
            cls="container",
        )
    )
