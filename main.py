import csv
from bs4 import BeautifulSoup
import html2text
import re

def clean_text(text):
    # Remove superscripts and extra spaces
    text = re.sub(r'\{\^[^\}]+\}', '', text).strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def extract_data(soup):
    # Extract author name
    author_name_tag = soup.find('span', class_='ltx_personname')
    author_name = ' '.join(author_name_tag.stripped_strings) if author_name_tag else 'N/A'
    author_name = clean_text(author_name)

    # Extract author email
    author_email_tag = soup.find('span', class_="ltx_contact ltx_role_email")
    author_email = author_email_tag.text.strip() if author_email_tag else 'N/A'

    # Extract author address
    author_address_tag = soup.find('span', class_='ltx_contact ltx_role_address')
    author_address = '\n'.join([line.strip() for line in author_address_tag.stripped_strings]) if author_address_tag else 'N/A'
    author_address = clean_text(author_address)

    # Extract abstract text
    abstract_html = soup.find('p', class_='ltx_p')
    abstract_text = '\n'.join([line.strip() for line in html2text.html2text(str(abstract_html)).splitlines() if line.strip()]) if abstract_html else 'N/A'

    # Extract keywords
    keywords_tag = soup.find('div', class_='ltx_classification')
    keywords = keywords_tag.text.strip() if keywords_tag else 'N/A'

    return [author_name, author_email, author_address, abstract_text, keywords]

def main():
    # Start file number
    start_file_number = 10000

    # Number of files to process
    num_files = 10

    # TSV file name where the data is saved
    tsv_file_name = 'info.tsv'

    # Opening the TSV file for writing
    with open(tsv_file_name, 'w', newline='', encoding='utf-8') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter='\t')

        # Iterating through the file numbers
        for file_number in range(start_file_number, start_file_number + num_files):
            file_name = f'papers\\01\\2101.{file_number}.html'

            # Opening the HTML file
            with open(file_name, 'r', encoding='utf-8') as html_file:
                content = html_file.read()

            # Creating a BeautifulSoup object
            soup = BeautifulSoup(content, 'lxml')

            # Extract data
            data = extract_data(soup)

            # Writing the extracted information to the TSV file
            tsv_writer.writerow(data)

    print(f"Data is saved to {tsv_file_name}")

if __name__ == "__main__":
    main()
