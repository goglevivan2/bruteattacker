import requests

sites=[
   'https://www.example.com/',
   'http://goglevivan.pythonanywhere.com/',
    'http://ivangoglev.pythonanywhere.com/',
    'http://site.com',
    'https://www.example.org/'
]
counter = 0
with open('log.txt','w') as f:
    for site in sites:
        for _ in range(100):
            try:
                response = requests.get(site)
                res=str(counter)+' Site: '+ site +'  -  Status code: '+str(response.status_code)+'\n'
                f.write(res)
                counter+=1
            except Exception as e:
                f.write(e)
                counter += 1


