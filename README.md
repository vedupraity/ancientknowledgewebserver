# Ancient Knowledge

## Recollecting the lost knowledge

https://www.ancientknowledge.in

---

## About

Ancient Knowledge is an educational, open-source, and non-profit project to collect ancient Indian scriptures, books, texts based on history, mythology, philosophy, rituals, and spirituality.

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
│   ├── site/  # site routes and views
│   └── content/  # content routes and views
├── build/  # generated static html and assets
├── helpers/  # helper modules
├── static/  # css, images, js
├── templates/  # jinja templates
│   ├── generic/  # base templates
│   ├── site/  # site page templates
│   └── content/  # content page templates
├── .env.dev  # env vars (development)
├── .env.prod  # env vars (production)
├── app.py  # flask app
├── config.py  # app settings and constants
├── freeze.py  # static site generation script
└── run  # script to run flask server or generate static site
```

---

## Development Environment Setup

1. Clone content (database) repository

https://github.com/vedupraity/ancientknowledgedatabase

2. Start local database server

```sh
cd <ancientknowledgedatabase-repo-dir>
python3 -m http.server 5001
```

3. Clone flask app repository

https://github.com/vedupraity/ancientknowledgewebserver

4. Start flask server

```sh
cd <ancientknowledge-repo-dir>
pip install -r requirements.txt
./run server dev
```

5. Freeze app into static files (building in dev)

```sh
./run build dev
```

look into the `build` directory for generated static pages and assets

6. Building for production

```sh
./run build prod
```