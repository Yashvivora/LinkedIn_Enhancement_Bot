import requests
from bs4 import BeautifulSoup

def scrape_linkedin_profile(url):
    """
    Scrapes the LinkedIn profile data from the given URL.
    Returns a dictionary containing the profile sections such as 'about', 'experience', and 'education'.
    """
    headers = {
        'User-Agent': 'Your User Agent',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        profile_data = {}
        
        profile_data['about'] = soup.find('section', {'id': 'about'}).get_text(strip=True)
        profile_data['experience'] = soup.find('section', {'id': 'experience'}).get_text(strip=True)
        profile_data['education'] = soup.find('section', {'id': 'education'}).get_text(strip=True)
        return profile_data
    else:
        return None
'''
from bs4 import BeautifulSoup

def scrape_linkedin_profile(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        profile_data = {}
        
        profile_data['about'] = soup.find('section', {'id': 'about'}).get_text(strip=True)
        profile_data['experience'] = soup.find('section', {'id': 'experience'}).get_text(strip=True)
        profile_data['education'] = soup.find('section', {'id': 'education'}).get_text(strip=True)
        print(profile_data)
        return profile_data

scrape_linkedin_profile('site.html')

'''