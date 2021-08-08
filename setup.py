from setuptools import setup


dependencies = [
    "beautifulsoup4==4.9.3",
    "requests==2.25.0",
    "urllib3==1.26.2",
    "openpyxl==3.0.7",
]

package_data = {
    "scrap.resources": ["configuration.ini"],
    "sheets.resources": ["config.ini"],
}

packages = [
    "functions",
    "log",
    "scrap",
    "scrap.resources",
    "sheets",
    "sheets.resources",
]

platform = ["any"]

long_description = (
    "This application extracts economic data from different sources using web scraping with "
    "Beautifilsoup, to later save them in an Excel file "
)

manifest = dict(
    name="dollar-scraping",
    version="1.0.0",
    author="DobleRR - Rodrigo Quispe",
    author_email="rrquispezabala@gmail.com",
    description="Web Scraping of dollar values",
    url="https://github.com/RRodriQZ",
    license="MIT",
    python_requires=">=3.6, <4",
    keywords="dollar scraping argentine banks",
    install_requires=dependencies,
    package_data=package_data,
    packages=packages,
    platforms=platform,
    long_description=long_description,
    long_description_content_type="text/markdown",
)


if __name__ == "__main__":
    setup(**manifest)
