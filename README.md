This Python program is designed to extract structured data from HTML files and save it into a TSV (Tab-Separated Values) file. It utilizes the BeautifulSoup library for HTML parsing and some custom functions for data cleaning and extraction. Below are the key components and usage instructions for this script.

**Extracting the files**
To extract the ArXiV papers that I have used, unzip the papers.zip

**Script Components
Libraries Used**
BeautifulSoup: A Python library for parsing HTML and XML documents.
html2text: A library for converting HTML content to plain text.
re: The regular expressions module for text pattern matching.

**Functions**
clean_text(text): This function cleans the input text by removing superscripts and extra spaces.

extract_data(soup): This function extracts structured data from the HTML content using BeautifulSoup. It specifically extracts author name, author email, author address, abstract text, and keywords.

main(): The main function of the script. It specifies the start file number, the number of files to process, and the TSV file name. It then iterates through HTML files, extracts data, and writes it to the TSV file.

**Installing requirements** 
Install the necessary Python libraries (BeautifulSoup, html2text, and re). You can install them using pip:
pip install beautifulsoup4 html2text
Run the script using the following command:
python main.py

**Data Extraction**
The extracted data will be saved in a TSV file with named info.tsv
Once the script finishes processing, it will display a message indicating data is saved at info.tsv
