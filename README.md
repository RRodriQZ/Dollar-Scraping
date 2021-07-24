# Dollar-Scraping

Web Scraping of dollar values

Esta aplicacion extrae datos economicos de distintas fuentes utilizando web scraping con
Beautifilsoup, para posteriormente guardarlos en un archivo excel.

Paginas Principales:
* [Banco Nacion] (https://www.bna.com.ar/Personas)
* [Rofex] (https://www.matbarofex.com.ar/)
* [CME Group] (https://www.cmegroup.com/)
* [Bloomberg] (https://www.bloomberg.com)

Para más informacion ver los links del archivo: "**config.ini**".

# Pre Requirements 📋

* **Python 3** - **pipenv** / **Docker**

# Setup Python Virtual Environment 🔧 #
```cmd
pip install pipenv
```
**Windows** CMD:
```cmd
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
**Linux / MAC** command:
```cmd
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```
# Running Python Script 🐼
```cmd
python main.py
```
# Running Docker 🐳
```cmd
docker build -t scraping .
docker run -it scraping
```
# Author 🖋

* Rodrigo Quispe - Developer - [RRodriQZ]
 
[RRodriQZ]: https://github.com/RRodriQZ