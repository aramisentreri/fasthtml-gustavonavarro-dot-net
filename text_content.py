

welcome_text = """
I am a repurposed math PhD, working in Algorithms and software leadership in the Bay Area. In the past I worked mainly in problems related to Fluid dynamics and Free boundary problems. My thesis was on the local and global well-posedness of the Two-Phase Stefan problem, which is a model for the interaction of two phases of a fluid, like ice and water, and the evolution of the interface that separates the two.

I am interested in anything related to mathematics, from numerical simulations of differential equations, to optimization, and lately Data Science. Any problem that can be modeled into a mathematical question, and that requires deep thinking and the development of new mathematical tools sparks my interest.
"""

quick_bio = """
Ph.D. Mathematics (2016) University of California Davis. Advisor: Steve Shkoller. Thesis: Local and Global well-posedness of the Two-phase Stefan problem.

BS Physics (2008) Physics department, U. Chile.

BS Mathematics (2008) Mathematics department, U. Chile.

Mathematical Civil Engineering (2009) Mathematics department, U. Chile. Advisor: Juan Diego Davila. Undergraduate Thesis: Singular Limits in Liouville type equations with exponential Neumann data.


Publications
M. Hadzic, G. Navarro, S. Shkoller, Local well-posedness and Global stability of the Two-phase Stefan problem. SIAM J. Math. Anal., 49(6), 4942–5006. (65 pages) SIAM, Arxiv
R. Granero-Belinchon, G. Navarro, A. Ortega, On the effect of boundaries in the two-phase porous flow. Nonlinearity 28 (2015) 435-461. IOPScience, Arxiv
"""

style_text = """
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

"""