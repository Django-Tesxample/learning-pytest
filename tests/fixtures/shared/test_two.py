
def test_check_values(data_from_file):
    assert 'values' in data_from_file
    assert data_from_file.get('values') == [1, 2, 3]
