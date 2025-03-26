import traceback
import requests

def catch_response():
    urls = [
        'httpss://google.com',
        'google.com',
        'https://google.coms',
        'https://google.com'
    ]
    exceptions = []
    for url in urls:
        try:
            r = requests.get(url)
        except Exception as e:
            e.add_note(f'url = {url}')
            exceptions.append(e)

    if len(exceptions) > 0:
        raise ExceptionGroup('例外発生', exceptions)
    

try:
    catch_response()
except ExceptionGroup as eg:
    traceback.print_exception(eg)