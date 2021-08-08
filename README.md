# Dollar-Scraping

Web Scraping of dollar values

This application extracts economic data from different sources using web scraping with
Beautifilsoup, to later save them in an Excel file.

Main Pages:
* [Banco Nacion] (https://www.bna.com.ar/Personas)
* [Rofex] (https://www.matbarofex.com.ar/)
* [CME Group] (https://www.cmegroup.com/)
* [Bloomberg] (https://www.bloomberg.com)

For more information see the links of the file: "**scrap/resources/configuration.ini**"

# Pre Requirements 📋

* **Python 3**-**pipenv** / **Docker**

# Setup Python Virtual Environment 🔧 #
```cmd
pip install pipenv
```
**Windows** CMD:
```cmd
python -m venv venv
.\venv\Scripts\activate
pip install -e .
```
**Linux / MAC** command:
```cmd
python -m venv venv
source venv/bin/activate
python -m pip install -e .
```
# Running Python Script 🐼
```cmd
python main.py
```
# Running Docker 🐳
```cmd
docker build -t dollar-scraping .
docker run -it dollar-scraping
```
# Author 🖋

* Rodrigo Quispe - Developer - [RRodriQZ]
 
[RRodriQZ]: https://github.com/RRodriQZ