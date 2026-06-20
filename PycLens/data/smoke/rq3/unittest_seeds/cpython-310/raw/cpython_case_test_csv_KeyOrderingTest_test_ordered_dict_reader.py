# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: KeyOrderingTest_test_ordered_dict_reader

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = dedent('            FirstName,LastName\n            Eric,Idle\n            Graham,Chapman,Over1,Over2\n\n            Under1\n            John,Cleese\n        ').splitlines()
    self.assertEqual(list(csv.DictReader(data)), [OrderedDict([('FirstName', 'Eric'), ('LastName', 'Idle')]), OrderedDict([('FirstName', 'Graham'), ('LastName', 'Chapman'), (None, ['Over1', 'Over2'])]), OrderedDict([('FirstName', 'Under1'), ('LastName', None)]), OrderedDict([('FirstName', 'John'), ('LastName', 'Cleese')])])
    self.assertEqual(list(csv.DictReader(data, restkey='OtherInfo')), [OrderedDict([('FirstName', 'Eric'), ('LastName', 'Idle')]), OrderedDict([('FirstName', 'Graham'), ('LastName', 'Chapman'), ('OtherInfo', ['Over1', 'Over2'])]), OrderedDict([('FirstName', 'Under1'), ('LastName', None)]), OrderedDict([('FirstName', 'John'), ('LastName', 'Cleese')])])
    del data[0]
    self.assertEqual(list(csv.DictReader(data, fieldnames=['fname', 'lname'])), [OrderedDict([('fname', 'Eric'), ('lname', 'Idle')]), OrderedDict([('fname', 'Graham'), ('lname', 'Chapman'), (None, ['Over1', 'Over2'])]), OrderedDict([('fname', 'Under1'), ('lname', None)]), OrderedDict([('fname', 'John'), ('lname', 'Cleese')])])
