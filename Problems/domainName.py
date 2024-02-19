# print the domain name without printing www.


websites = ['www.youtube.com',
            'www.google.com',
            'www.wikipedia.com']
def domain(item):
    domains = [n.split('w.')[1] for n in item]
    print(domains)

domain(websites)