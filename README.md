# Dollar-Scraping

Web Scraping of dollar values

Esta aplicacion extrae datos economicos de distintas fuentes utilizando web scraping con
Beautifilsoup, para posteriormente guardarlos en un archivo excel.

Paginas Principales:
* [Banco Nacion] (https://www.bna.com.ar/Personas)
* [Rofex] (https://www.matbarofex.com.ar/)
* [CME Group] (https://www.cmegroup.com/)
* [Bloomberg] (https://www.bloomberg.com)

Para mas informacion ver los links del archivo: "**config.ini**".

# Pre Requirements 📋

* **Python3** / **Docker**

# Setup Python Virtual Environment 🔧
Windows cmd / Ubuntu command:

1) **python -m venv venv**

2) **cd venv\Scripts & .\activate**

3) **cd .. & cd .. & pip install -r requirements.txt**

# Running Python Script 🐼

4) **python main.py**

# Running Docker 🐳

1) **docker build -t scraping .**
2) **docker run -it scraping**

# Author 🖋

* Rodrigo Quispe - Developer - [RRodriQZ]
 
[RRodriQZ]: https://github.com/RRodriQZ