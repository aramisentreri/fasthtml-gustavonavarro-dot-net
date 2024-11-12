from fasthtml.common import *
from components import header
from text_content import welcome_text, quick_bio, style_text

app, rt = fast_app(
    hdrs=(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Title('Gustavo Navarro | Personal Portfolio'),
        Link(rel="stylesheet", href="styles.css"),
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
                            cls='project',
                            onclick="window.open('https://bazaarofdragons.unicornplatform.page/', '_blank')",
                        ),
                        Div(
                            Img(src='hero_images/image-asset.jpeg?height=200&width=300&text=Urban%20Office%20Complex', alt='Particles'),
                            Div(
                                H3('Quantum Physics for Engineers'),
                                P('No advanced math - real applications - Deep understanding of quantum physics through code'),
                                cls='project-info'
                            ),
                            cls='project',
                            onclick="window.open('https://quantumphysicsforengineers.com/', '_blank')",
                        ), 
                        Div(
                            Img(src='hero_images/twitch.png?height=200&width=300&text=Eco-Friendly%20School', alt='Twitch'),
                            Div(
                                H3('Twitch stream'),
                                P('Advanced physics and math simplified through code and numerical computation.'),
                                cls='project-info'
                            ),
                            cls='project',
                            onclick="window.open('https://twitch.tv/aramisentreri', '_blank')",
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