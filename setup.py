from setuptools import setup, find_packages

setup(
    name="YTDownLoad",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "blinker==1.9.0",
        "click==8.2.1",
        "colorama==0.4.6",
        "ffmpeg==1.4",
        "Flask==3.1.2",
        "Flask-SQLAlchemy==3.1.1",
        "flask-utils==0.1.1",
        "greenlet==3.2.4",
        "itsdangerous==2.2.0",
        "Jinja2==3.1.6",
        "MarkupSafe==3.0.2",
        "pytube==15.0.0",
        "SQLAlchemy==2.0.43",
        "typing_extensions==4.15.0",
        "utils==1.0.2",
        "Werkzeug==3.1.3",
        "yt-dlp==2025.9.5"
    ],
)