# Ancient Knowledge Webserver: Python Flask Service for Enhanced Navigation of Centralized Open Source Database of Ancient Scriptures

Welcome to the Ancient Knowledge repository, a hub for Vedic Culture and the Sanātana Dharma. Our mission is to foster a platform that enables everyone to explore and learn from the profound wisdom contained within ancient scriptures.

Visit our website at [https://www.ancientknowledge.in](https://www.ancientknowledge.in) to access the comprehensive tool we've created for Sanskrit scholars and researchers. This website serves as an invaluable resource, utilizing the website templates and navigation tools maintained in this repository to provide a centralized location for studying and researching ancient scriptures.

## About

This repository contains the Python/Flask web server project that powers the Ancient Knowledge website. By leveraging this codebase, we enhance the readability and accessibility of the content sourced from the [vedupraity/ancientknowledgedatabase](https://github.com/vedupraity/ancientknowledgedatabase) repository.

## Technology Stack

To bring an optimal user experience, we utilize the following technologies:

1. [Python 3](https://www.python.org/downloads/): Python is a powerful general-purpose programming language that serves as the foundation for this project.
2. [Flask](https://palletsprojects.com/p/flask/): Flask is a lightweight micro web framework written in Python. It provides the necessary tools and features to build and serve web applications.
3. [Jinja](https://palletsprojects.com/p/jinja/): Jinja is a web template engine for Python, enabling dynamic rendering of content and seamless integration with Flask.
4. [Bulma](https://bulma.io/): Bulma is a responsive CSS framework that ensures the website's layout and design are optimized for various devices and screen sizes.
5. [jQuery](https://jquery.com/): jQuery is a feature-rich JavaScript library that simplifies HTML document traversal, event handling, and animation, improving the interactive elements on the website.
6. [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/): Frozen-Flask allows us to generate static files from the Flask application, enabling easy deployment and improved performance.

## Project Structure

The project structure is as follows:

```sh
ancientknowledgewebserver
├── blueprints/  # Flask blueprints
├── helpers/  # Helper modules
├── static/  # CSS, images, JS
├── templates/  # Jinja templates
├── .env.dev  # Environment variables (for development)
├── .env.prod  # Environment variables (for production)
├── app.py  # Flask app main script
├── config.py  # App settings and constants
├── freeze.py  # Static site generation script
└── run  # Script to run the Flask server or generate the static site
```

## Development Environment Setup

To set up your development environment, please follow these steps:

1. Clone the [vedupraity/ancientknowledgedatabase](https://github.com/vedupraity/ancientknowledgedatabase) to obtain the required database for the web server.

```sh
git clone https://github.com/vedupraity/ancientknowledgedatabase
```

2. Start the database server by navigating to the cloned `ancientknowledgedatabase` directory and executing the following command:

```sh
cd ancientknowledgedatabase
python3 server.py
```

3. Clone this `ancientknowledgewebserver` repository to obtain the Flask web server code.

```sh
git clone https://github.com/vedupraity/ancientknowledgewebserver
```

4. Start the Flask web server by navigating to the cloned `ancientknowledgewebserver` directory, installing the required dependencies, and running the server using the following commands:

```sh
cd ancientknowledgewebserver
pip install -r requirements.txt
./run server dev
```

5. Generate static files by running the following command. This will build the artifacts and store them under the `build` directory.

```sh
./run build dev
```

## Get in Touch

We value your contributions and feedback. If you have any questions, suggestions, or would like to collaborate, please don't hesitate to reach out to us at [contact@ancientknowledge.in](mailto:contact@ancientknowledge.in). We are excited to engage with fellow enthusiasts and researchers alike!

Thank you for joining us on this remarkable journey of unraveling the ancient wisdom and embracing the richness of Vedic Culture. Together, let us delve into the depths of these scriptures, fostering a broader understanding and appreciation of the Sanātana Dharma.
