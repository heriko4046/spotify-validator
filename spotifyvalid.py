import requests as r, os
from fake_useragent import UserAgent
from colorama import Fore, Style

class Spotify:
    def __init__(self):
        self.api = r.Session()
        self.ua = UserAgent().random 
        self.green = Fore.GREEN
        self.reset = Style.RESET_ALL
        self.red = Fore.RED

    def valid(self, email):
        # Post
        headers = {
            'User-Agent': self.ua,
        }

        data = {
            'validate': '1',
            'email': email
        }

        try:
            resp = self.api.get('https://spclient.wg.spotify.com/signup/public/v1/account', headers=headers, params=data)

            # Json 
            data = resp.json()
            country = data['country']

            # Validator
            if 'is already registered to an account' in resp.text:
                print(f'[> Email: {email} | {self.green}Valid{self.reset}')        
            else:
                print(f'[> Email: {email} | {self.red}Invalid{self.reset}')

            with open('spotifyvalid.txt', 'a') as file:
                file.write(f'[> Email: {email} | Valid | {country}' + '\n')
        except KeyboardInterrupt:
            print('[!] Process Interrupted!')
        except Exception as e:
            print(f'[!] Error: {e}')

if __name__ == "__main__":
    try:
        bot = Spotify()
        os.system('cls')
        print('<[ Spotify Email Validator ]>')
        email = input('[> File Path: ')  
        with open(email, 'r') as file:  
            for email in file:
                bot.valid(email.strip())
        print('\n[!] Result Saved: spotifyvalid.txt') 
    except KeyboardInterrupt:
        print('[!] Process Interrupted!')
