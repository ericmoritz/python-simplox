from simplox.multirequest import *
import time
import requests

def serial(urls):
    for url in urls:
        resp = requests.get(url)
    
def uncached(endpoint, urls):
    mr = multirequest(*[get(url) for url in urls])
    for data in fetch(endpoint, mr):
        pass
    
def cached(endpoint, urls):
    mr = multirequest(*[get(url, cache=cache(url, 10)) for url in urls])
    for data in fetch(endpoint, mr):
        pass

def tc(f):
    start = time.time()
    ret = f()
    end = time.time()
    return end-start, ret

def report(name, (time, _)):
    print "{name}: {time:.2f} ms".format(name=name,
                                         time=time*1000.0)

if __name__ == '__main__':
    endpoint = sys.argv[1]
    urls = sys.argv[2:]
    
    report("Serial", tc(lambda: serial(urls)))
    report("Uncached", tc(lambda: uncached(endpoint, urls)))
    report("Cached", tc(lambda: cached(endpoint, urls)))


