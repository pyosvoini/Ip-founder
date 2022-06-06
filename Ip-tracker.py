from urllib import response
import requests
from pyfiglet import Figlet
import folium

def get_ip_inf(ip):
    try:
        response = requests.get(url = f'http://ip-api.com/json/{ip}', verify=False).json()
        
        data = {
        'query':response.get('query'),
        'country':response.get('country'),
        'city':response.get('city'),
        'lat':response.get('lat'),
        'lon':response.get('lon'),
        'isp':response.get('isp')
        }

        for i, j in data.items():
            print(f'{i} : {j}')

        region = folium.Map(location=[response.get('lat'), response.get('lon')])
        
        region.save((f'{response.get("city")}_{response.get("org")}.html'))
        
        return data
    
    except requests.exceptions.ConnectionError:
        print('[!] Error for connection')

def main():
    preview = Figlet(font = 'slant')
    print(preview.renderText('By pyosvoini project'))
    ip = input('Input ip-address \n')
    return get_ip_inf(ip)

if __name__ == '__main__':
    main()