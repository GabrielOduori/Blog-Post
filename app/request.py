# app/request.py


import urllib.request, json
from .models import Quote


# Getting News urls
base_url =None 

def configure_request(app):
    global base_url
    base_url = app.config['QUOTES_URL']
    base_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    print(base_url)



def get_quote():
    '''
    Function that gets the 
    '''
    get_quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)
        
        quote_result = None
        # quote_results = []
        
        if get_quote_response:
            quote = get_quote_response
            quote_result = process_results(quote)
            
    return quote_result



def process_results(quote_results):
    '''
    '''
    
    the_quote = []

    id =quote_results
    quote = quote_results
    author = quote_results
    permalink  = quote_results


    quote_object = Quote(id,quote,author,permalink)
    the_quote.append(quote_object.quote)
    
    return the_quote
