from fasthtml.common import *
from components import header
app, rt = fast_app(
    hdrs=(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Title('Gustavo Navarro | Architectural Portfolio'),
        Style(":root {\r\n            --primary-color: #2c3e50;\r\n            --secondary-color: #34495e;\r\n            --accent-color: #3498db;\r\n            --light-grey: #ecf0f1;\r\n            --dark-grey: #7f8c8d;\r\n            --white: #ffffff;\r\n        }\r\n        body {\r\n            font-family: 'Arial', sans-serif;\r\n            line-height: 1.6;\r\n            color: var(--primary-color);\r\n            margin: 0;\r\n            padding: 0;\r\n            background-color: var(--light-grey);\r\n        }\r\n        .container {\r\n            max-width: 1200px;\r\n            margin: 0 auto;\r\n            padding: 0 1rem;\r\n        }\r\n        header {\r\n            background-color: var(--white);\r\n            box-shadow: 0 1px 3px rgba(0,0,0,0.1);\r\n        }\r\n        nav {\r\n            display: flex;\r\n            justify-content: space-between;\r\n            align-items: center;\r\n            padding: 1rem 0;\r\n        }\r\n        .logo {\r\n            font-size: 1.5rem;\r\n            font-weight: bold;\r\n            color: var(--accent-color);\r\n        }\r\n        nav ul {\r\n            display: flex;\r\n            list-style: none;\r\n            margin: 0;\r\n            padding: 0;\r\n        }\r\n        nav ul li {\r\n            margin-left: 1.5rem;\r\n        }\r\n        nav ul li a {\r\n            text-decoration: none;\r\n            color: var(--primary-color);\r\n            font-weight: bold;\r\n            transition: color 0.3s ease;\r\n        }\r\n        nav ul li a:hover {\r\n            color: var(--accent-color);\r\n        }\r\n        .hero {\r\n            position: relative;\r\n            height: 500px;\r\n            border-radius: 0.5rem;\r\n            overflow: hidden;\r\n            margin-bottom: 3rem;\r\n        }\r\n        .hero-bg {\r\n            position: absolute;\r\n            top: 0;\r\n            left: 0;\r\n            width: 100%;\r\n            height: 100%;\r\n            object-fit: cover;\r\n        }\r\n        .hero-content {\r\n            position: absolute;\r\n            top: 0;\r\n            left: 0;\r\n            width: 100%;\r\n            height: 100%;\r\n            background-color: rgba(0,0,0,0.5);\r\n            display: flex;\r\n            align-items: center;\r\n            justify-content: center;\r\n        }\r\n        .hero-text {\r\n            text-align: center;\r\n            color: var(--white);\r\n        }\r\n        .profile-pic {\r\n            width: 160px;\r\n            height: 160px;\r\n            border-radius: 50%;\r\n            border: 4px solid var(--white);\r\n            margin-bottom: 1rem;\r\n        }\r\n        .hero h1 {\r\n            font-size: 2.5rem;\r\n            margin-bottom: 0.5rem;\r\n        }\r\n        .hero p {\r\n            font-size: 1.25rem;\r\n            margin: 0;\r\n        }\r\n        .card {\r\n            background-color: var(--white);\r\n            border-radius: 0.5rem;\r\n            box-shadow: 0 2px 4px rgba(0,0,0,0.1);\r\n            padding: 2rem;\r\n            margin-bottom: 3rem;\r\n        }\r\n        h2 {\r\n            color: var(--accent-color);\r\n            margin-top: 0;\r\n        }\r\n        .projects {\r\n            display: grid;\r\n            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));\r\n            gap: 2rem;\r\n        }\r\n        .project {\r\n            background-color: var(--white);\r\n            border-radius: 0.5rem;\r\n            overflow: hidden;\r\n            box-shadow: 0 2px 4px rgba(0,0,0,0.1);\r\n            transition: transform 0.3s ease, box-shadow 0.3s ease;\r\n        }\r\n        .project:hover {\r\n            transform: translateY(-5px);\r\n            box-shadow: 0 4px 8px rgba(0,0,0,0.15);\r\n        }\r\n        .project img {\r\n            width: 100%;\r\n            height: 200px;\r\n            object-fit: cover;\r\n        }\r\n        .project-info {\r\n            padding: 1rem;\r\n        }\r\n        .project-info h3 {\r\n            margin-top: 0;\r\n            color: var(--primary-color);\r\n        }\r\n        footer {\r\n            background-color: var(--secondary-color);\r\n            color: var(--white);\r\n            text-align: center;\r\n            padding: 1rem 0;\r\n            margin-top: 3rem;\r\n        }")
    ),
    live=True)

@app.get("/")
def home():

    # return Html(
    #     Head(
    #         Meta(charset='UTF-8'),
    #         Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
    #         Title('Gustavo Navarro | Architectural Portfolio'),
    #         Style(":root {\r\n            --primary-color: #2c3e50;\r\n            --secondary-color: #34495e;\r\n            --accent-color: #3498db;\r\n            --light-grey: #ecf0f1;\r\n            --dark-grey: #7f8c8d;\r\n            --white: #ffffff;\r\n        }\r\n        body {\r\n            font-family: 'Arial', sans-serif;\r\n            line-height: 1.6;\r\n            color: var(--primary-color);\r\n            margin: 0;\r\n            padding: 0;\r\n            background-color: var(--light-grey);\r\n        }\r\n        .container {\r\n            max-width: 1200px;\r\n            margin: 0 auto;\r\n            padding: 0 1rem;\r\n        }\r\n        header {\r\n            background-color: var(--white);\r\n            box-shadow: 0 1px 3px rgba(0,0,0,0.1);\r\n        }\r\n        nav {\r\n            display: flex;\r\n            justify-content: space-between;\r\n            align-items: center;\r\n            padding: 1rem 0;\r\n        }\r\n        .logo {\r\n            font-size: 1.5rem;\r\n            font-weight: bold;\r\n            color: var(--accent-color);\r\n        }\r\n        nav ul {\r\n            display: flex;\r\n            list-style: none;\r\n            margin: 0;\r\n            padding: 0;\r\n        }\r\n        nav ul li {\r\n            margin-left: 1.5rem;\r\n        }\r\n        nav ul li a {\r\n            text-decoration: none;\r\n            color: var(--primary-color);\r\n            font-weight: bold;\r\n            transition: color 0.3s ease;\r\n        }\r\n        nav ul li a:hover {\r\n            color: var(--accent-color);\r\n        }\r\n        .hero {\r\n            position: relative;\r\n            height: 500px;\r\n            border-radius: 0.5rem;\r\n            overflow: hidden;\r\n            margin-bottom: 3rem;\r\n        }\r\n        .hero-bg {\r\n            position: absolute;\r\n            top: 0;\r\n            left: 0;\r\n            width: 100%;\r\n            height: 100%;\r\n            object-fit: cover;\r\n        }\r\n        .hero-content {\r\n            position: absolute;\r\n            top: 0;\r\n            left: 0;\r\n            width: 100%;\r\n            height: 100%;\r\n            background-color: rgba(0,0,0,0.5);\r\n            display: flex;\r\n            align-items: center;\r\n            justify-content: center;\r\n        }\r\n        .hero-text {\r\n            text-align: center;\r\n            color: var(--white);\r\n        }\r\n        .profile-pic {\r\n            width: 160px;\r\n            height: 160px;\r\n            border-radius: 50%;\r\n            border: 4px solid var(--white);\r\n            margin-bottom: 1rem;\r\n        }\r\n        .hero h1 {\r\n            font-size: 2.5rem;\r\n            margin-bottom: 0.5rem;\r\n        }\r\n        .hero p {\r\n            font-size: 1.25rem;\r\n            margin: 0;\r\n        }\r\n        .card {\r\n            background-color: var(--white);\r\n            border-radius: 0.5rem;\r\n            box-shadow: 0 2px 4px rgba(0,0,0,0.1);\r\n            padding: 2rem;\r\n            margin-bottom: 3rem;\r\n        }\r\n        h2 {\r\n            color: var(--accent-color);\r\n            margin-top: 0;\r\n        }\r\n        .projects {\r\n            display: grid;\r\n            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));\r\n            gap: 2rem;\r\n        }\r\n        .project {\r\n            background-color: var(--white);\r\n            border-radius: 0.5rem;\r\n            overflow: hidden;\r\n            box-shadow: 0 2px 4px rgba(0,0,0,0.1);\r\n            transition: transform 0.3s ease, box-shadow 0.3s ease;\r\n        }\r\n        .project:hover {\r\n            transform: translateY(-5px);\r\n            box-shadow: 0 4px 8px rgba(0,0,0,0.15);\r\n        }\r\n        .project img {\r\n            width: 100%;\r\n            height: 200px;\r\n            object-fit: cover;\r\n        }\r\n        .project-info {\r\n            padding: 1rem;\r\n        }\r\n        .project-info h3 {\r\n            margin-top: 0;\r\n            color: var(--primary-color);\r\n        }\r\n        footer {\r\n            background-color: var(--secondary-color);\r\n            color: var(--white);\r\n            text-align: center;\r\n            padding: 1rem 0;\r\n            margin-top: 3rem;\r\n        }")
    #     ),
    #     Body(
    #         Header(
    return (Title('Gustavo Navarro | Architectural Portfolio'),
            header,
            Main(
                Section(
                    Img(src='/placeholder.svg?height=500&width=1200', alt='Architectural background', cls='hero-bg'),
                    Div(
                        Div(
                            Img(src='/placeholder.svg?height=160&width=160', alt='Gustavo Navarro profile picture', cls='profile-pic'),
                            H1('Gustavo Navarro'),
                            P('Innovative Architectural Design Solutions'),
                            cls='hero-text'
                        ),
                        cls='hero-content'
                    ),
                    cls='hero'
                ),
                Section(
                    H2('Welcome to My Portfolio'),
                    P("I'm Gustavo Navarro, an award-winning architect with over 15 years of experience in creating sustainable, innovative, and aesthetically pleasing designs. My work spans residential, commercial, and public spaces, always with a focus on harmonizing form and function. Through my designs, I strive to create environments that inspire, endure, and positively impact the lives of those who inhabit them."),
                    cls='card'
                ),
                Section(
                    H2('Featured Projects'),
                    Div(
                        Div(
                            Img(src='/placeholder.svg?height=200&width=300&text=Modern%20Residence', alt='Modern Residence'),
                            Div(
                                H3('Modern Residence'),
                                P('A sleek, minimalist home design focusing on open spaces and natural light.'),
                                cls='project-info'
                            ),
                            cls='project'
                        ),
                        Div(
                            Img(src='/placeholder.svg?height=200&width=300&text=Urban%20Office%20Complex', alt='Urban Office Complex'),
                            Div(
                                H3('Urban Office Complex'),
                                P('A sustainable, multi-use office building designed for the heart of the city.'),
                                cls='project-info'
                            ),
                            cls='project'
                        ),
                        Div(
                            Img(src='/placeholder.svg?height=200&width=300&text=Eco-Friendly%20School', alt='Eco-Friendly School'),
                            Div(
                                H3('Eco-Friendly School'),
                                P('An innovative educational facility that harmonizes with its natural surroundings.'),
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
                    P('With over a decade of experience in architectural design, I specialize in creating spaces that blend functionality with aesthetic appeal. My approach focuses on sustainable practices and innovative solutions that push the boundaries of modern architecture.'),
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
                P('© 2023 Gustavo Navarro Architectural Design. All rights reserved.')
            )
        )

@app.get("/blog")
def blog():
    return Html(
    Head(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Title("John Doe's Personal Blog"),
        Style(":root {\r\n            --primary-color: #2c3e50;\r\n            --secondary-color: #34495e;\r\n            --accent-color: #3498db;\r\n            --light-grey: #ecf0f1;\r\n            --dark-grey: #7f8c8d;\r\n            --white: #ffffff;\r\n        }\r\n        body {\r\n            font-family: 'Arial', sans-serif;\r\n            line-height: 1.6;\r\n            color: var(--primary-color);\r\n            margin: 0;\r\n            padding: 0;\r\n            background-color: var(--light-grey);\r\n        }\r\n        .container {\r\n            max-width: 1200px;\r\n            margin: 0 auto;\r\n            padding: 0 1rem;\r\n        }\r\n        header {\r\n            background-color: var(--white);\r\n            box-shadow: 0 1px 3px rgba(0,0,0,0.1);\r\n            padding: 1rem 0;\r\n        }\r\n        nav ul {\r\n            display: flex;\r\n            list-style: none;\r\n            padding: 0;\r\n            margin: 0;\r\n        }\r\n        nav ul li {\r\n            margin-right: 1rem;\r\n        }\r\n        nav ul li a {\r\n            text-decoration: none;\r\n            color: var(--primary-color);\r\n            font-weight: bold;\r\n            transition: color 0.3s ease;\r\n        }\r\n        nav ul li a:hover {\r\n            color: var(--accent-color);\r\n        }\r\n        main {\r\n            display: flex;\r\n            flex-wrap: wrap;\r\n            margin-top: 2rem;\r\n        }\r\n        .content {\r\n            flex: 2;\r\n            margin-right: 2rem;\r\n        }\r\n        .sidebar {\r\n            flex: 1;\r\n        }\r\n        .post {\r\n            background-color: var(--white);\r\n            border-radius: 5px;\r\n            padding: 1.5rem;\r\n            margin-bottom: 2rem;\r\n            box-shadow: 0 2px 4px rgba(0,0,0,0.1);\r\n        }\r\n        .post h2 {\r\n            color: var(--accent-color);\r\n            margin-top: 0;\r\n        }\r\n        .post-meta {\r\n            color: var(--dark-grey);\r\n            font-size: 0.9rem;\r\n            margin-bottom: 1rem;\r\n        }\r\n        .sidebar-section {\r\n            background-color: var(--white);\r\n            border-radius: 5px;\r\n            padding: 1.5rem;\r\n            margin-bottom: 2rem;\r\n            box-shadow: 0 2px 4px rgba(0,0,0,0.1);\r\n        }\r\n        .sidebar-section h3 {\r\n            color: var(--accent-color);\r\n            margin-top: 0;\r\n        }\r\n        .sidebar-section ul {\r\n            list-style: none;\r\n            padding: 0;\r\n        }\r\n        .sidebar-section ul li {\r\n            margin-bottom: 0.5rem;\r\n        }\r\n        .sidebar-section ul li a {\r\n            text-decoration: none;\r\n            color: var(--primary-color);\r\n            transition: color 0.3s ease;\r\n        }\r\n        .sidebar-section ul li a:hover {\r\n            color: var(--accent-color);\r\n        }\r\n        footer {\r\n            background-color: var(--secondary-color);\r\n            color: var(--white);\r\n            text-align: center;\r\n            padding: 1rem 0;\r\n            margin-top: 2rem;\r\n        }\r\n        @media (max-width: 768px) {\r\n            main {\r\n                flex-direction: column;\r\n            }\r\n            .content {\r\n                margin-right: 0;\r\n            }\r\n        }")
    ),
    Body(
        header,
        Div(
            Main(
                Section(
                    Article(
                        H2('The Future of Web Development: What to Expect in 2024'),
                        Div('Posted on May 15, 2023 by John Doe', cls='post-meta'),
                        P("As we approach 2024, the landscape of web development continues to evolve at a rapid pace. From new frameworks to innovative design trends, developers need to stay ahead of the curve. In this post, we'll explore the technologies and methodologies that are set to shape the future of web development."),
                        P("We'll dive into topics such as AI-assisted coding, the rise of Web Assembly, and the increasing importance of accessibility in web design. Whether you're a seasoned developer or just starting out, this post will give you valuable insights into the direction our field is heading."),
                        A('Read more...', href='#', style='color: var(--accent-color);'),
                        cls='post'
                    ),
                    Article(
                        H2("My Journey Through Southeast Asia: A Developer's Perspective"),
                        Div('Posted on April 28, 2023 by John Doe', cls='post-meta'),
                        P('Last month, I embarked on a thrilling journey through Southeast Asia, exploring the vibrant tech scenes in cities like Singapore, Bangkok, and Ho Chi Minh City. As a developer, I was fascinated by the unique challenges and innovations I encountered in each location.'),
                        P("From co-working spaces in Bali to startup incubators in Singapore, I'll share my experiences and the lessons I learned about the global nature of our industry. Join me as I recount the highlights of my trip and the insights I gained about the future of tech in this dynamic region."),
                        A('Read more...', href='#', style='color: var(--accent-color);'),
                        cls='post'
                    ),
                    cls='content'
                ),
                Aside(
                    Div(
                        H3('About Me'),
                        P("Hi, I'm John Doe, a full-stack developer with a passion for creating innovative web solutions. This blog is where I share my thoughts on tech, my travels, and life as a developer."),
                        cls='sidebar-section'
                    ),
                    Div(
                        H3('Recent Posts'),
                        Ul(
                            Li(
                                A('The Future of Web Development: What to Expect in 2024', href='#')
                            ),
                            Li(
                                A("My Journey Through Southeast Asia: A Developer's Perspective", href='#')
                            ),
                            Li(
                                A('5 VS Code Extensions Every Developer Should Know', href='#')
                            ),
                            Li(
                                A('The Art of Balancing Work and Life as a Remote Developer', href='#')
                            )
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
                )
            ),
            cls='container'
        ),
        Footer(
            P("© 2023 John Doe's Personal Blog. All rights reserved.")
        )
    ),
    lang='en'
)


serve()