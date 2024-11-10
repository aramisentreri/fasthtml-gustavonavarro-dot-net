from fasthtml.common import *
from components import header
from text_content import welcome_text, quick_bio

app, rt = fast_app(
    hdrs=(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Title('Gustavo Navarro | Personal Portfolio'),
        # Style(":root {\r\n            --primary-color: #2c3e50;\r\n            --secondary-color: #34495e;\r\n            --accent-color: #3498db;\r\n            --light-grey: #ecf0f1;\r\n            --dark-grey: #7f8c8d;\r\n            --white: #ffffff;\r\n        }\r\n        body {\r\n            font-family: 'Arial', sans-serif;\r\n            line-height: 1.6;\r\n            color: var(--primary-color);\r\n            margin: 0;\r\n            padding: 0;\r\n            background-color: var(--light-grey);\r\n        }\r\n        .container {\r\n            max-width: 1200px;\r\n            margin: 0 auto;\r\n            padding: 0 1rem;\r\n        }\r\n        header {\r\n            background-color: var(--white);\r\n            box-shadow: 0 1px 3px rgba(0,0,0,0.1);\r\n        }\r\n        nav {\r\n            display: flex;\r\n            justify-content: space-between;\r\n            align-items: center;\r\n            padding: 1rem 0;\r\n        }\r\n        .logo {\r\n            font-size: 1.5rem;\r\n            font-weight: bold;\r\n            color: var(--accent-color);\r\n        }\r\n        nav ul {\r\n            display: flex;\r\n            list-style: none;\r\n            margin: 0;\r\n            padding: 0;\r\n        }\r\n        nav ul li {\r\n            margin-left: 1.5rem;\r\n        }\r\n        nav ul li a {\r\n            text-decoration: none;\r\n            color: var(--primary-color);\r\n            font-weight: bold;\r\n            transition: color 0.3s ease;\r\n        }\r\n        nav ul li a:hover {\r\n            color: var(--accent-color);\r\n        }\r\n        .hero {\r\n            position: relative;\r\n            height: 500px;\r\n            border-radius: 0.5rem;\r\n            overflow: hidden;\r\n            margin-bottom: 3rem;\r\n        }\r\n        .hero-bg {\r\n            position: absolute;\r\n            top: 0;\r\n            left: 0;\r\n            width: 100%;\r\n            height: 100%;\r\n            object-fit: cover;\r\n        }\r\n        .hero-content {\r\n            position: absolute;\r\n            top: 0;\r\n            left: 0;\r\n            width: 100%;\r\n            height: 100%;\r\n            background-color: rgba(0,0,0,0.5);\r\n            display: flex;\r\n            align-items: center;\r\n            justify-content: center;\r\n        }\r\n        .hero-text {\r\n            text-align: center;\r\n            color: var(--white);\r\n        }\r\n        .profile-pic {\r\n            width: 250px;\r\n            height: 250px;\r\n            border-radius: 50%;\r\n            border: 4px solid var(--white);\r\n            margin-bottom: 1rem;\r\n        }\r\n        .hero h1 {\r\n            font-size: 2.5rem;\r\n            margin-bottom: 0.5rem;\r\n        }\r\n        .hero p {\r\n            font-size: 1.25rem;\r\n            margin: 0;\r\n        }\r\n        .card {\r\n            background-color: var(--white);\r\n            border-radius: 0.5rem;\r\n            box-shadow: 0 2px 4px rgba(0,0,0,0.1);\r\n            padding: 2rem;\r\n            margin-bottom: 3rem;\r\n        }\r\n        h2 {\r\n            color: var(--accent-color);\r\n            margin-top: 0;\r\n        }\r\n        .projects {\r\n            display: grid;\r\n            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));\r\n            gap: 2rem;\r\n        }\r\n        .project {\r\n            background-color: var(--white);\r\n            border-radius: 0.5rem;\r\n            overflow: hidden;\r\n            box-shadow: 0 2px 4px rgba(0,0,0,0.1);\r\n            transition: transform 0.3s ease, box-shadow 0.3s ease;\r\n        }\r\n        .project:hover {\r\n            transform: translateY(-5px);\r\n            box-shadow: 0 4px 8px rgba(0,0,0,0.15);\r\n        }\r\n        .project img {\r\n            width: 100%;\r\n            height: 200px;\r\n            object-fit: cover;\r\n        }\r\n        .project-info {\r\n            padding: 1rem;\r\n        }\r\n        .project-info h3 {\r\n            margin-top: 0;\r\n            color: var(--primary-color);\r\n        }\r\n        footer {\r\n            background-color: var(--secondary-color);\r\n            color: var(--white);\r\n            text-align: center;\r\n            padding: 1rem 0;\r\n            margin-top: 3rem;\r\n        }"),
        # Style(":root {\r\n            --primary-color: #2c3e50;\r\n            --secondary-color: #34495e;\r\n            --accent-color: #3498db;\r\n            --light-grey: #ecf0f1;\r\n            --dark-grey: #7f8c8d;\r\n            --white: #ffffff;\r\n        }\r\n        body {\r\n            font-family: 'Arial', sans-serif;\r\n            line-height: 1.6;\r\n            color: var(--primary-color);\r\n            margin: 0;\r\n            padding: 0;\r\n            background-color: var(--light-grey);\r\n        }\r\n        .container {\r\n            max-width: 1200px;\r\n            margin: 0 auto;\r\n            padding: 0 1rem;\r\n        }\r\n        header {\r\n            background-color: var(--white);\r\n            box-shadow: 0 1px 3px rgba(0,0,0,0.1);\r\n            padding: 1rem 0;\r\n        }\r\n        nav ul {\r\n            display: flex;\r\n            list-style: none;\r\n            padding: 0;\r\n            margin: 0;\r\n        }\r\n        nav ul li {\r\n            margin-right: 1rem;\r\n        }\r\n        nav ul li a {\r\n            text-decoration: none;\r\n            color: var(--primary-color);\r\n            font-weight: bold;\r\n            transition: color 0.3s ease;\r\n        }\r\n        nav ul li a:hover {\r\n            color: var(--accent-color);\r\n        }\r\n        main {\r\n            display: flex;\r\n            flex-wrap: wrap;\r\n            margin-top: 2rem;\r\n        }\r\n        .content {\r\n            flex: 2;\r\n            margin-right: 2rem;\r\n        }\r\n        .sidebar {\r\n            flex: 1;\r\n        }\r\n        .post {\r\n            background-color: var(--white);\r\n            border-radius: 5px;\r\n            padding: 1.5rem;\r\n            margin-bottom: 2rem;\r\n            box-shadow: 0 2px 4px rgba(0,0,0,0.1);\r\n        }\r\n        .post h2 {\r\n            color: var(--accent-color);\r\n            margin-top: 0;\r\n        }\r\n        .post-meta {\r\n            color: var(--dark-grey);\r\n            font-size: 0.9rem;\r\n            margin-bottom: 1rem;\r\n        }\r\n        .sidebar-section {\r\n            background-color: var(--white);\r\n            border-radius: 5px;\r\n            padding: 1.5rem;\r\n            margin-bottom: 2rem;\r\n            box-shadow: 0 2px 4px rgba(0,0,0,0.1);\r\n        }\r\n        .sidebar-section h3 {\r\n            color: var(--accent-color);\r\n            margin-top: 0;\r\n        }\r\n        .sidebar-section ul {\r\n            list-style: none;\r\n            padding: 0;\r\n        }\r\n        .sidebar-section ul li {\r\n            margin-bottom: 0.5rem;\r\n        }\r\n        .sidebar-section ul li a {\r\n            text-decoration: none;\r\n            color: var(--primary-color);\r\n            transition: color 0.3s ease;\r\n        }\r\n        .sidebar-section ul li a:hover {\r\n            color: var(--accent-color);\r\n        }\r\n        footer {\r\n            background-color: var(--secondary-color);\r\n            color: var(--white);\r\n            text-align: center;\r\n            padding: 1rem 0;\r\n            margin-top: 2rem;\r\n        }\r\n        @media (max-width: 768px) {\r\n            main {\r\n                flex-direction: column;\r\n            }\r\n            .content {\r\n                margin-right: 0;\r\n            }\r\n        }"),
        Style("""
              :root {
    --primary-color: #2c3e50;
    --secondary-color: #34495e;
    --accent-color: #3498db;
    --light-grey: #ecf0f1;
    --dark-grey: #7f8c8d;
    --white: #ffffff;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: var(--primary-color);
    margin: 0;
    padding: 0;
    background-color: var(--light-grey);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

/* Header Styling */
header {
    background-color: var(--white);
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

/* Navbar Styling */
nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 0;
}

.nav-list {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-list li {
    margin-right: 1.5rem;
}

.nav-list li a {
    text-decoration: none;
    color: var(--primary-color);
    font-weight: bold;
    transition: color 0.3s ease;
}

.nav-list li a:hover {
    color: var(--accent-color);
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--accent-color);
}

/* Hero Section */
.hero {
    position: relative;
    height: 500px;
    border-radius: 0.5rem;
    overflow: hidden;
    margin-bottom: 3rem;
}

.hero-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.hero-content {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero-text {
    text-align: center;
    color: var(--white);
}

.profile-pic {
    width: 250px;
    height: 250px;
    border-radius: 50%;
    border: 4px solid var(--white);
    margin-bottom: 1rem;
}

.hero h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

.hero p {
    font-size: 1.25rem;
    margin: 0;
}

/* Card Styling */
.card {
    background-color: var(--white);
    border-radius: 0.5rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    padding: 2rem;
    margin-bottom: 3rem;
}

h2 {
    color: var(--accent-color);
    margin-top: 0;
}

/* Projects Grid */
.projects {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.project {
    background-color: var(--white);
    border-radius: 0.5rem;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.project:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.project img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.project-info {
    padding: 1rem;
}

.project-info h3 {
    margin-top: 0;
    color: var(--primary-color);
}

/* Sidebar and Main Content */
.blog-main {
    display: flex;
    flex-wrap: wrap;
    margin-top: 2rem;
}

.blog-content {
    flex: 2;
    margin-right: 2rem;
}

.sidebar {
    flex: 1;
}

.post {
    background-color: var(--white);
    border-radius: 5px;
    padding: 1.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.post h2 {
    color: var(--accent-color);
    margin-top: 0;
}

.post-meta {
    color: var(--dark-grey);
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.sidebar-section {
    background-color: var(--white);
    border-radius: 5px;
    padding: 1.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.sidebar-section h3 {
    color: var(--accent-color);
    margin-top: 0;
}

.sidebar-section ul {
    list-style: none;
    padding: 0;
}

.sidebar-section ul li {
    margin-bottom: 0.5rem;
}

.sidebar-section ul li a {
    text-decoration: none;
    color: var(--primary-color);
    transition: color 0.3s ease;
}

.sidebar-section ul li a:hover {
    color: var(--accent-color);
}

/* Footer Styling */
footer {
    background-color: var(--secondary-color);
    color: var(--white);
    text-align: center;
    padding: 1rem 0;
    margin-top: 3rem;
}

/* Media Queries */
@media (max-width: 768px) {
    blog-main {
        flex-direction: column;
    }
    .blog-content {
        margin-right: 0;
    }
}

""")
    ),
    live=True)



@app.get("/")
def home():
    return (Title('Gustavo Navarro | Personal Portfolio'),
            header,
            Main(
                Section(
                    Img(src='hero_images/PXL_20240322_233906335~2.jpg', alt='Math background', cls='hero-bg'),
                    Div(
                        Div(
                            Img(src='profile_images/IMG_4033_compressed.jpg', alt='Gustavo Navarro profile picture', cls='profile-pic'),
                            H1('Gustavo Navarro'),
                            P('Math, Physics, Software and Leadership'),
                            cls='hero-text'
                        ),
                        cls='hero-content'
                    ),
                    cls='hero'
                ),
                Section(
                    H2('Welcome to My Portfolio'),
                    P(welcome_text),
                    cls='card'
                ),
                Section(
                    H2('Featured Projects'),
                    Div(
                        Div(
                            Img(src='hero_images/marketplace.jpg?height=200&width=300&text=Modern%20Residence', alt='Bazaar of Dragons'),
                            Div(
                                H3('Bazaar of Dragons'),
                                P('A marketplace for table top miniatures'),
                                cls='project-info'
                            ),
                            cls='project'
                        ),
                        Div(
                            Img(src='hero_images/image-asset.jpeg?height=200&width=300&text=Urban%20Office%20Complex', alt='Particles'),
                            Div(
                                H3('Quantum Physics for Engineers'),
                                P('No advanced math - real applications - Deep understanding of quantum physics through code'),
                                cls='project-info'
                            ),
                            cls='project'
                        ),
                        Div(
                            Img(src='hero_images/twitch.png?height=200&width=300&text=Eco-Friendly%20School', alt='Twitch'),
                            Div(
                                H3('Twitch stream'),
                                P('Advanced physics and math simplified through code and numerical computation.'),
                                cls='project-info'
                            ),
                            cls='project'
                        ),
                        cls='projects'
                    ),
                    id='projects'
                ),
                Section(
                    H2('About Me'),
                    P(quick_bio),
                    id='about',
                    cls='card'
                ),
                Section(
                    H2('Get in Touch'),
                    P('Interested in collaborating on a project? Feel free to reach out:'),
                    P('Email: john.doe@example.com'),
                    P('Phone: (123) 456-7890'),
                    id='contact',
                    cls='card'
                ),
                cls='container'
            ),
            Footer(
                P('© 2023 Gustavo Navarro. All rights reserved.')
            )
        )

@app.get("/blog")
def blog():
   return (
        header,
        Div(
            Main(
                Section(
                    Article(
                        H2('Covariant derivatives are hard'),
                        Div('Posted on February 28th, 2022 by Gustavo Navarro', cls='post-meta'),
                        P("This last weekend I had a super good time with a friend, just spending a few hours figuring out some math from the physics behemoth “Gravity” by Misner, Wheeler and Thorne. I have some experience with general relativity and differential geometry, but I’ve never made it very far into the field, so we just opened the textbook, somewhere in Chapter 2, and looked in for entertainment:"),
                        A('Read more...', href='https://aramisentreri.github.io/2022/02/28/covariant-derivatives-are-hard.html', style='color: var(--accent-color);'),
                        cls='post'
                    ),
                    Article(
                        H2("What the hell is a tensor anyways?"),
                        Div('Posted on December 22nd, 2021 by Gustavo Navarro', cls='post-meta'),
                        P('As I’m studying more and more differential geometry and general relativity (and being the noob that I am), I have to go back to this definition over and over again, so I thought that writing it down for good can help me (and hopefully others) get a quick refresher into what is a Tensor anyways.'),
                        A('Read more...', href='https://aramisentreri.github.io/2021/12/22/what-the-hell-is-a-tensor-anyways.html', style='color: var(--accent-color);'),
                        cls='post'
                    ),
                    cls='blog-content'
                ),
                Aside(
                    Div(
                        H3('About Me'),
                        P("Hi, I'm Gustavo Navarro, I am a repurposed math PhD, working in Algorithms and software leadership in the Bay Area. This blog is where I write about whatever with a random frequency. Mostly math and physics though."),
                        cls='sidebar-section'
                    ),
                    Div(
                        H3('Recent Posts'),
                        Ul(
                            Li(
                                A('Feynman’s proof of the Maxwell equations - 6/1/2020', href='https://aramisentreri.github.io/2020/06/01/feynman-maxwell-equations.html')
                            ),
                            Li(
                                A("What the hell is a Tensor anyways? - 12/22/2021", href='https://aramisentreri.github.io/2021/12/22/what-the-hell-is-a-tensor-anyways.html')
                            ),
                            Li(
                                A('Covariant derivatives are hard - 02/28/2022', href='https://aramisentreri.github.io/2022/02/28/covariant-derivatives-are-hard.html')
                            ),
                        ),
                        cls='sidebar-section'
                    ),
                    Div(
                        H3('Categories'),
                        Ul(
                            Li(
                                A('Tech (15)', href='#')
                            ),
                            Li(
                                A('Lifestyle (8)', href='#')
                            ),
                            Li(
                                A('Travel (6)', href='#')
                            ),
                            Li(
                                A('Career (10)', href='#')
                            )
                        ),
                        cls='sidebar-section'
                    ),
                    cls='sidebar'
                ),
            cls='blog-main'),
            cls='container'
        ),
        Footer(
            P("© 2023 Gustavo Navarro's Personal Blog. All rights reserved.")
        )
    )


serve()