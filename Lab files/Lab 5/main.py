import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    
    if isinstance(category, int):
        df = pd.read_sql(f"""
            SELECT
                title,
                language.name languge,
                category.name category
            FROM
                film
            INNER JOIN
                language USING(language_id)
            INNER JOIN
                film_category USING(film_id)
            INNER JOIN
                category USING(category_id)
            WHERE
                category.category_id = {category}
            ORDER BY
                title, languge ASC
            """, con=connection)
        return df
    elif isinstance(category, str):
        df = pd.read_sql(f"""
            SELECT
                title,
                language.name languge,
                category.name category
            FROM
                film
            INNER JOIN
                language USING(language_id)
            INNER JOIN
                film_category USING(film_id)
            INNER JOIN
                category USING(category_id)
            WHERE
                category.name like '{category}'
            ORDER BY
                title, languge ASC
            """, con=connection)
        return df
    else:
        return None


def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category, int):
        df = pd.read_sql(f"""
            SELECT
                title,
                language.name languge,
                category.name category
            FROM
                film
            INNER JOIN
                language USING(language_id)
            INNER JOIN
                film_category USING(film_id)
            INNER JOIN
                category USING(category_id)
            WHERE
                category.category_id = {category}
            ORDER BY
                title, languge ASC
            """, con=connection)
        return df
    elif isinstance(category, str):
        df = pd.read_sql(f"""
            SELECT
                title,
                language.name languge,
                category.name category
            FROM
                film
            INNER JOIN
                language USING(language_id)
            INNER JOIN
                film_category USING(film_id)
            INNER JOIN
                category USING(category_id)
            WHERE
                category.name ilike '{category}'
            ORDER BY
                title, languge ASC
            """, con=connection)
        return df
    else:
        return None
    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(title, str):
        df = pd.read_sql(f"""
            SELECT
                first_name,
                last_name
            FROM
                actor
            INNER JOIN
                film_actor USING(actor_id)
            INNER JOIN
                film USING(film_id)
            WHERE
                film.title like '{title}'
            ORDER BY
                last_name, first_name ASC
            """, con=connection)
        return df
    else:
        return None
    

def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(words, list):
        words_ = '|'.join(words)
        df = pd.read_sql(f"""
            SELECT
                title
            FROM
                film
            WHERE
                title ~* '(?:^| )({words_})"""+"""{1,}(?:$| )'
            ORDER BY
                title
            """, con=connection)
        return df
    else:
        return None