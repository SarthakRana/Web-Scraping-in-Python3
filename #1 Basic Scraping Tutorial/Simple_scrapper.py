from bs4 import BeautifulSoup
import requests
import lxml

#pass html into beautifulsoup so that we can get a beautifulsoup object
with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# Let's print the soup object contents. Prettify method indents the html code making it more readable.
print(soup.prettify())

# To access the text of <title> tag of webpage, we use soup object followed by .<tagname> followed by .text
print(soup.title.text)
# To access the <div> tag of webpage
print(soup.div)

# But this returns only the first occurrence of <title> tag or <div> tag.Therefore, we use the find() method.
# find() allows us to pass arguments to allow us to access the exact thing we are looking for.
# For eg: I want the <div> tag which has an attribute => class = 'footer'.
print(soup.find('div', class_='footer'))

# Coming back to our html file...Now we the headline of articles
articles = soup.find('div', class_='article')
print(articles)
headline = articles.h2.a.text
summary = articles.p.text
print(headline)
print(summary)

# Now, there can be many articles on a single web page and we have to access all of them
# We use find_all() method to do this.
# find_all() method returns a list of all tags that were searched(along with arguments (if passed)).
articles = soup.find_all('div', class_='article')
for i, article in enumerate(articles):
    print("Headline {} : ".format(i+1) + article.h2.a.text)
    print("Summary {} : ".format(i+1) + article.p.text)
    print() # Empty line
