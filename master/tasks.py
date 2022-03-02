import requests
from bs4 import BeautifulSoup
from master.models import Cluster, ClusterTen, ClusterSixty
from celery import shared_task

from temp import time_limiter

"""
0 is monday and other days depends on that
"""
@shared_task
@time_limiter
def add():


    url = "http://tsetmc.com/Loader.aspx?Partree=151315&Type=MostVisited&Flow=1"

    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'lxml')

    all_tr = soup.find_all('tr')

    for i in range(1,len(all_tr)):
        all_td = all_tr[i].find_all('td')

        Cluster.objects.create(
            name = all_td[0].text, propagate_date =all_td[1].text,
            last_value = all_td[2].text, change = all_td[3].text,
            precent = all_td[4].text, max_value = all_td[5].text,
            min_value = all_td[6].text)
    
    return "ok 1"







@shared_task
@time_limiter
def add_ten():

    url = "http://tsetmc.com/Loader.aspx?Partree=151315&Type=MostVisited&Flow=1"

    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'lxml')

    all_tr = soup.find_all('tr')

    for i in range(1,len(all_tr)):
        all_td = all_tr[i].find_all('td')

        ClusterTen.objects.create(
            name = all_td[0].text, propagate_date =all_td[1].text,
            last_value = all_td[2].text, change = all_td[3].text,
            precent = all_td[4].text, max_value = all_td[5].text,
            min_value = all_td[6].text)


    return "ok 10"






@shared_task
def add_sixty():
    url="http://tsetmc.com/Loader.aspx?Partree=151315&Type=MostVisited&Flow=1"

    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'lxml')

    all_tr = soup.find_all('tr')

    for i in range(1,len(all_tr)):
        all_td = all_tr[i].find_all('td')

        ClusterSixty.objects.create(
            name = all_td[0].text, propagate_date =all_td[1].text,
            last_value = all_td[2].text, change = all_td[3].text,
            precent = all_td[4].text, max_value = all_td[5].text,
            min_value = all_td[6].text)
    
    return "ok 60"