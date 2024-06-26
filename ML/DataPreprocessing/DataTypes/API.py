import finnhub
def API_access():
    stock_symbol = 'AMZN'
    finnhub_client = finnhub.Client(api_key="cptqjo9r01qnga5ilcigcptqjo9r01qnga5ilcj0")

    print(finnhub_client.quote(stock_symbol))
    # soup = BeautifulSoup(r.text, features = 'html.parser')
    # with codecs.open("amazon.txt","w",encoding = 'utf-8') as f:
    #     f.write(soup.prettify())

if __name__ == '__main__':
    API_access()