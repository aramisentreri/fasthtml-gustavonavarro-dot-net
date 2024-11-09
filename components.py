
from fasthtml.common import *

header = Header(
                Div(
                    Nav(
                        Div('Gustavo Navarro', cls='logo'),
                        Ul(
                            Li(
                                A('Projects', href='#projects')
                            ),
                            Li(
                                A('About', href='#about')
                            ),
                            Li(
                                A('Blog', href="/blog")
                            ),
                            Li(
                                A('Contact', href='#contact')
                            )
                        )
                    ),
                    cls='container'
                )
            )