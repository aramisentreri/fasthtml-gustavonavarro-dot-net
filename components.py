
from fasthtml.common import *

header = Header(
                Div(
                    Nav(
                        Div(A('Gustavo Navarro', href="/", style="text-decoration: none"), cls='logo'),
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