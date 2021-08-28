import requests
import pytest
import data_test


def test_total_count():
    response = requests.get(data_test.url)
    response = response.json()
    assert response['total'] == 22


def test_default_page_size():
    response = requests.get(data_test.url)
    response = response.json()
    assert len(response['items']) == 15


@pytest.mark.parametrize('value, expected_result', data_test.positive_page_size_list)
def test_positive_page_size(value, expected_result):
    params = {'page_size': value}
    response = requests.get(data_test.url, params=params)
    response = response.json()
    assert len(response['items']) == expected_result


@pytest.mark.parametrize('value', data_test.negative_page_size_list)
def test_negative_page_size(value):
    with pytest.raises(KeyError):
        params = {'page_size': value}
        response = requests.get(data_test.url, params=params)
        response = response.json()
        len(response['items'])


def test_positive_substr_search():
    params = {'q': 'рск'}
    response = requests.get(data_test.url, params=params)
    response = response.json()
    query = len(response['items'])
    assert query > 0


def test_negative_substr_search():
    with pytest.raises(KeyError):
        params = {'q': 'ск'}
        response = requests.get(data_test.url, params=params)
        response = response.json()
        query = len(response['items'])


@pytest.mark.parametrize('search, expected_result', data_test.full_name_data_list)
def test_register(search, expected_result):
    params = {'q': search}
    response = requests.get(data_test.url, params=params)
    response = response.json()
    for item in response['items']:
        assert item.get('name') == expected_result


@pytest.mark.parametrize('query, value, expected_result', data_test.ignore_query_param)
def test_ignoring_other_parameters(query, value, expected_result):
    params = {'q': 'москва', query: value}
    response = requests.get(data_test.url, params=params)
    response = response.json()
    response = response['items']
    if len(response) == 1:
        for item in response:
            assert expected_result in item.get('name')


@pytest.mark.parametrize('value', data_test.country_code)
def test_ignoring_other_parameters_substr(value):
    params = {'q': 'рск', 'country_code': value}
    response = requests.get(data_test.url, params=params)
    response = response.json()
    items = response['items']
    for item in items:
        assert item['country']['code'] in data_test.country_code


@pytest.mark.parametrize('value, expected_result', data_test.list_country_code)
def test_search_country_code(value, expected_result):
    param = {'country_code': value}
    response = requests.get(data_test.url, params=param)
    response = response.json()
    items = response['items']
    for item in items:
        assert item['country']['code'] == expected_result
