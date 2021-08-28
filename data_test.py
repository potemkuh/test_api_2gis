url = 'https://regions-test.2gis.com/1.0/regions'

full_name_data_list = [
    ('новосибирск', 'Новосибирск'),
    ('МосквА', 'Москва'),
    ('дНеПр', 'Днепр'),
    ('АКТОБЕ', 'Актобе')
]

positive_page_size_list = [
    (5, 5),
    (10, 10),
    (15, 15)
]

negative_page_size_list = [
    (" ",),
    ('',),
    (4,),
    (8,),
    (13,),
    (16,)
]

ignore_query_param = [
    ('country_code', 'kz', 'Москва'),
    ('page', '2', 'Москва'),
    ('page_size', '5', 'Москва')
]

country_code = ['ru', 'ua', 'kz', 'kg', 'cz']

list_country_code = [
    ('ru', 'ru'),
    ('ua', 'ua'),
    ('kz', 'kz'),
    ('kg', 'kg'),
    ('cz', 'cz')
]