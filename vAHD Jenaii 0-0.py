import requests
import json
from typing import Dict

class Detective:
    def login(self, username: str, password: str, login_url: str) -> Dict[str, str]:

        payload = {
            'username': username,
            'password': password
        }
        response = requests.post(login_url, data=payload)

        if response.status_code == 200:
            data = response.json()
            full_name = f"{data['first_name']} {data['last_name']}"
            return {
                'full_name': full_name,
                'email': data['email']
            }
        else:
            raise Exception(f"[{response.status_code}]: Unable to log in with provided credentials.")

    def upload_clues(self, upload_url: str, file_addresses: list) -> str:

        files = [(f'uploaded_files', open(file_address, 'rb')) for file_address in file_addresses]
        response = requests.put(upload_url, files=files)
        return response.json()['detail']

    def html_scraper(self, page_url: str) -> Dict[str, str]:

        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        links = {}
        for link in soup.find_all('a'):
            title = link.get_text().strip()
            if title:
                links[title] = link.get('href')

        return links

       # pip install -r python_requirements.txt
       #Lucifer 
