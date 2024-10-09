# News Web Scraper
This Python project allows you to scrape the title and content of a news article from a given URL. It uses the ```requests``` library to fetch the webpage and ```BeautifulSoup``` from bs4 to parse the HTML content and extract the relevant information.

## Features
- Fetches HTML content from news articles.
- Parses and extracts the article's title and body content.
- Saves the scraped content into a text file (```text.txt```).
- Displays the article title and content in the console.
## Requirements
- Python 3.x
- ```requests``` library
- BeautifulSoup (from the ```bs4``` library)
## Installation
1. Clone the repository:
```
git clone https://github.com/Mouadkeddis/web-scraping.git
cd web-scraping
```
2. Install the required dependencies:
```
pip install requests beautifulsoup4
```
## Usage
1. Run the Python script:
```python scraper.py```
2. You will be prompted to input the URL of a CNN news article:
```Enter the link of the CNN news: <your-article-url>```
3. The script will scrape the title and content of the article, print it to the console, and save the result to a file called ```text.txt```.

## Sample Output:
The content is saved in text.txt in the following format:
```
Title: [The title of the news article]
[The content of the article]
```
## File Structure
The project includes the following files:
```
web-scraping/
│
├── scrape_cnn.py           # Main Python script for scraping
├── text.txt                # Content of the news page
└── README.md               # Documentation (this file)
```
## Example
Given the CNN news article URL:
```
https://www.cnn.com/2024/10/09/article/example-news-title/index.html
```
After running the script, you will see the title and content of the article printed to the console and saved in ```text.txt```.

## Error Handling
- Invalid URL: If the user enters an invalid URL or if there is a connection error, the script will print an error message.
- Non-200 HTTP Status Code: If the server returns an HTTP error (like 404 or 500), the script will notify the user with the specific status code.
- Missing Elements: If the article doesn't contain an <```h1```> tag for the title or <```sp```> tags for the content, the script will handle the issue gracefully and notify the user.

## Contributing
If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch (```git checkout -b feature/YourFeature```).
3. Commit your changes (```git commit -am 'Add a new feature'```).
4. Push to the branch (```git push origin feature/YourFeature```).
5. Open a pull request.
