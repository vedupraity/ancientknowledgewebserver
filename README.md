# Ancient Knowledge

“Our mission is to allow everyone to learn about Vedic Culture and the Sanātana Dharma.”

https://www.ancientknowledge.in

---

## About

This is Python (Flask) web server project for the website: https://www.ancientknowledge.in

---

## Technology stack

1. [Python 3](https://www.python.org/downloads/) - *general-purpose programming language*
2. [Flask](https://palletsprojects.com/p/flask/) -  *micro web framework written in Python*
3. [Jinja](https://palletsprojects.com/p/jinja/) - *web template engine for Python*
4. [Bulma](https://bulma.io/) - *lightweight responsive CSS framework*
5. [JQuery](https://jquery.com/) - *feature-rich JavaScript library*
6. [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) - *freezes a Flask application into a set of static files*

---

## What's here

```sh
ancient_knowledge_site/  # project root
├── blueprints/  # flask blueprints
├── helpers/  # helper modules
├── static/  # css, images, js
├── templates/  # jinja templates
├── .env.dev  # env vars (for development)
├── .env.prod  # env vars (for production)
├── app.py  # flask app
├── config.py  # app settings and constants
├── freeze.py  # static site generation script
└── run  # script to run flask server or generate static site
```

---

## Development Environment Setup

1. Clone database repository

https://github.com/vedupraity/ancientknowledgedatabase

2. Start database server

```sh
cd ancientknowledgedatabase
python3 server.py
```

3. Clone flask web server repository

https://github.com/vedupraity/ancientknowledgewebserver

4. Start flask web server

```sh
cd ancientknowledgewebserver
pip install -r requirements.txt
./run server dev
```

5. Generate static files

This will build artifacts and store under `build` directory

```sh
./run build dev
```

## Contact

contact@ancientknowledge.in
