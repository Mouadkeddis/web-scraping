from bs4 import BeautifulSoup  # Library to parse HTML and XML documents
import requests  # Library to send HTTP requests

# Prompt the user to input the URL of a CNN news article
url = str(input("Enter the link of the cnn news: "))

# Function to fetch the HTML content of the page from the given URL
def fetch_html(url):
    try:
        respond = requests.get(url)
        if respond.status_code == 200:
            return respond.text
        else:
            print(f"Error: received status code  {respond.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request faild : {e}")

# Function to parse the content of the HTML and extract the title and article content
def parsing_content(respond):
    soup = BeautifulSoup(respond, 'html.parser')  # Parse the HTML response
    title = soup.find('h1')  # Find the title (usually inside an <h1> tag)
    if not title:
        print('Error: no title found')
        return
    # Find all <p> tags (paragraphs) and join their text content
    content = ' '.join([p.text for p in soup.find_all('p')])
    if not content:
        print("Error: no content found")
        return
    
    # Write the title and content to a text file
    with open('text.txt', 'w') as f:  # Using 'with' is better practice for file handling
        f.write("Title: " + title.text + content)

    
    # Print the title and content to the console
    return print(title.text, content)

# Fetch the HTML content from the given URL
respond = fetch_html(url)

# Parse and extract the relevant content from the HTML
parsing_content(respond)
