from datetime import datetime

from fasthtml.common import *

from components import site_footer, site_header
from posts import format_post_date, get_post, list_posts
from text_content import (
    bio_education,
    bio_publications,
    welcome_intro_company,
    welcome_intro_p1,
    welcome_intro_p1_tail,
    welcome_intro_p2,
)

DIVERGENT_URL = "https://divergenceai.xyz"

FONTS_LINK = (
    "https://fonts.googleapis.com/css2"
    "?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600"
    "&family=Inter:wght@400;500;600"
    "&family=IBM+Plex+Mono:wght@400;500"
    "&display=swap"
)

WORK_PROJECTS = [
    {
        "title": "Divergent Physics",
        "image": "hero_images/PXL_20240322_233906335~2.jpg",
        "url": DIVERGENT_URL,
        "blurb": (
            "AI-powered simulation automation for RF and antenna engineering "
            "teams. Sits on top of Ansys HFSS via official APIs — zero migration."
        ),
    },
    {
        "title": "Twitch — aramisentreri",
        "image": "hero_images/twitch.png",
        "url": "https://twitch.tv/aramisentreri",
        "blurb": (
            "Live computational physics: numerical simulation, scientific code, "
            "and math derivations on screen."
        ),
    },
]

FUN_PROJECTS = [
    {
        "title": "Quantum Physics for Engineers",
        "image": "hero_images/image-asset.jpeg",
        "url": "https://quantumphysicsforengineers.com/",
        "blurb": (
            "No advanced math, real applications — quantum physics built up "
            "from first principles through code."
        ),
    },
    {
        "title": "Bazaar of Dragons",
        "image": "hero_images/marketplace.jpg",
        "url": "https://bazaarofdragons.unicornplatform.page/",
        "blurb": "A marketplace for tabletop miniatures.",
    },
]

ARCHIVED_POSTS = [
    ("Covariant derivatives are hard",
     "2022-02-28",
     "https://aramisentreri.github.io/2022/02/28/covariant-derivatives-are-hard.html"),
    ("What the hell is a tensor anyways?",
     "2021-12-22",
     "https://aramisentreri.github.io/2021/12/22/what-the-hell-is-a-tensor-anyways.html"),
    ("Feynman's proof of the Maxwell equations",
     "2020-06-01",
     "https://aramisentreri.github.io/2020/06/01/feynman-maxwell-equations.html"),
]


app, rt = fast_app(
    pico=False,
    hdrs=(
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Meta(name="description",
             content="Gustavo Navarro — mathematician, physicist, software engineer. "
                     "Founder, Divergent Physics."),
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        Link(rel="stylesheet", href=FONTS_LINK),
        Link(rel="stylesheet", href="/styles.css"),
    ),
    live=True,
)


def project_card(project):
    return A(
        Img(src=project["image"], alt=project["title"]),
        Div(
            H3(project["title"]),
            P(project["blurb"]),
            Span("Visit →", cls="project-arrow"),
            cls="project-info",
        ),
        href=project["url"],
        target="_blank",
        rel="noopener noreferrer",
        cls="project-link",
    )


def hero_section():
    return Section(
        Div(
            H1("Gustavo Navarro"),
            P("Mathematician · Physicist · Software · Founder, Divergent Physics",
              cls="hero-tagline"),
        ),
        Img(src="profile_images/IMG_4033_compressed.jpg",
            alt="Gustavo Navarro",
            cls="hero-portrait"),
        cls="hero",
    )


def intro_section():
    return Section(
        Div(
            P(
                welcome_intro_p1,
                A(welcome_intro_company, href=DIVERGENT_URL,
                  target="_blank", rel="noopener noreferrer"),
                welcome_intro_p1_tail,
            ),
            P(welcome_intro_p2),
            cls="intro",
        ),
    )


def work_section():
    return Section(
        Span("01 — Work", cls="section-label"),
        H2("What I'm building"),
        Div(*[project_card(p) for p in WORK_PROJECTS], cls="projects"),
        id="work",
    )


def fun_section():
    return Section(
        Span("02 — For Fun", cls="section-label"),
        H2("Side projects"),
        Div(*[project_card(p) for p in FUN_PROJECTS], cls="projects"),
        id="fun",
    )


def about_section():
    edu_rows = []
    for label, body in bio_education:
        edu_rows.extend([Dt(label), Dd(P(body))])
    pub_rows = []
    for authors, citation in bio_publications:
        pub_rows.extend([Dt(authors), Dd(P(citation))])

    return Section(
        Span("03 — About", cls="section-label"),
        H2("Background"),
        Dl(*edu_rows, cls="about-grid"),
        H2("Publications", style="margin-top: 3rem;"),
        Dl(*pub_rows, cls="about-grid"),
        id="about",
    )


def contact_section():
    return Section(
        Span("04 — Contact", cls="section-label"),
        H2("Get in touch"),
        P("Open to collaboration, advising, and interesting problems."),
        Ul(
            Li(Span("Email", cls="label"),
               A("gustavo@divergenceai.xyz",
                 href="mailto:gustavo@divergenceai.xyz")),
            Li(Span("Company", cls="label"),
               A("divergenceai.xyz", href=DIVERGENT_URL,
                 target="_blank", rel="noopener noreferrer")),
            Li(Span("GitHub", cls="label"),
               A("@aramisentreri",
                 href="https://github.com/aramisentreri",
                 target="_blank", rel="noopener noreferrer")),
            cls="contact-list",
        ),
        id="contact",
    )


@app.get("/")
def home():
    year = datetime.now().year
    return (
        Title("Gustavo Navarro"),
        site_header(),
        Main(
            hero_section(),
            intro_section(),
            work_section(),
            fun_section(),
            about_section(),
            contact_section(),
            cls="container",
        ),
        site_footer(year),
    )


@app.get("/blog")
def blog():
    year = datetime.now().year
    posts = list_posts()

    if posts:
        post_items = [
            Li(
                A(
                    Span(format_post_date(p["date"]), cls="post-date"),
                    Div(
                        H2(p["title"]),
                        P(p["summary"], cls="post-summary") if p["summary"] else "",
                    ),
                    href=f"/blog/{p['slug']}",
                ),
                cls="post-list-item",
            )
            for p in posts
        ]
    else:
        post_items = [
            Li(
                P("No posts yet — porting things over from old notes.",
                  cls="post-summary"),
                cls="post-list-item",
                style="padding: 1.75rem 0;",
            )
        ]

    archived_items = [
        Li(
            A(Span(d, cls="archived-date"), title, href=url,
              target="_blank", rel="noopener noreferrer"),
        )
        for title, d, url in ARCHIVED_POSTS
    ]

    return (
        Title("Writing | Gustavo Navarro"),
        site_header(),
        Main(
            Section(
                Span("Writing", cls="section-label"),
                H1("Notes, drafts, and small explorations"),
                P("Mostly math, physics, and the occasional thing about teams "
                  "and software.", style="color: var(--ink-muted); max-width: 60ch;"),
                cls="blog-header",
            ),
            Ul(*post_items, cls="post-list"),
            Section(
                Span("Archive", cls="section-label"),
                H2("Older posts (external)"),
                P("These live on the old site at aramisentreri.github.io.",
                  style="color: var(--ink-muted);"),
                Ul(*archived_items, cls="archived-list"),
            ),
            cls="container",
        ),
        site_footer(year),
    )


@app.get("/blog/{slug}")
def blog_post(slug: str):
    year = datetime.now().year
    post = get_post(slug)
    if post is None:
        return (
            Title("Not found"),
            site_header(),
            Main(
                Section(
                    H1("Not found"),
                    P("That post doesn't exist."),
                    A("← Back to writing", href="/blog", cls="post-back"),
                    cls="post-article",
                ),
                cls="container",
            ),
            site_footer(year),
        )

    return (
        Title(f"{post['title']} | Gustavo Navarro"),
        site_header(),
        Main(
            Article(
                A("← Back to writing", href="/blog", cls="post-back"),
                Div(format_post_date(post["date"]), cls="post-meta"),
                H1(post["title"]),
                NotStr(post["html"]),
                cls="post-article",
            ),
            cls="container",
        ),
        site_footer(year),
    )


serve()
