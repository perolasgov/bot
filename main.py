from os import read, write
import tweepy
import time
import random

api_key = 'mhLHPEJiBRYa0laznFhom4PLi'
api_secret_key = 'GQufLwynbAiI2vaPVeaAB5yGFMnpttXPK2bVMVr9SwjgbVHt9s'
acess_key = '1404917255100637195-5Zr4XIRCtR3o4JKxYEgQYyuH0T5pKI'
acess_secret = 'XkoymFrpPx84dzh0xBhaPoL1EWhmrtk6nAjYr7mi5FVEf'
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r+')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w+')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def random_phrase():
    p1 = ['O confinamento', 'A Ciência', 'A OMS', 'A Universidade', 'A democracia', 'A vacina', 'O isolamento social', 'A Pfizer', 'O facismo', 'O Trump', 'O Ouro', 'A universidade pública', 'A CPI']
    p2 = [' é uma invenção', ' é uma estratégia', ' é um plano', ' é uma conspiração', ' é uma mentira', ' é uma investida', ' é uma tentativa', ' é um delírio']
    p3 = [' da esquerda', ' da China', ' das FARC ',' do PT', ' do feminismo', ' da globo', ' dos gays', ' da foice de São Paulo', ' do Queiroz', ' do Dória', ' do Putin', ' do Elon Musk', ' da SpaceX', ' da Tesla INC.', ' do comunismo']
    p4 = [' para desmobilizar', ' para legimitar', ' para esconder', ' para destruir', ' para confundir', ' para intimidar', ' para ridicularizar', ' para atingir']
    p5 = [' o Bolsonaro', ' o mito', ' a elite', ' as sociedades secretas', ' o elixir da vida', ' os repitilianos', ' a Terra Plana', ' o patriotismo', ' os evangélicos', ' a Bíblia', ' a mansão do Flávio', ' a motociata de 1,3mi', ' os emails da Pfizer', ' a pandemia', ' a Butanvac', ' a UFSCar']
    genius_phrase = random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4) + random.choice(p5)
    return genius_phrase 

def _main_():
    read_last_seen_str = str(read_last_seen(FILE_NAME))
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
    print('Ultimo ID pesquisado:' + read_last_seen_str)
    for tweet in reversed(tweets):
        store_last_seen(FILE_NAME, tweet.id)
        genius_phrase = random_phrase()
        api.update_status('@'+ tweet.user.screen_name + ' ' + genius_phrase, in_reply_to_status_id=tweet.id)
        print(f'Resposta enviada a {tweet.user.screen_name}')

while True:
    _main_()
    time.sleep(30)