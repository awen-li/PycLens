# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_mlsd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    list(self.client.mlsd())
    list(self.client.mlsd(path='/'))
    list(self.client.mlsd(path='/', facts=['size', 'type']))
    ls = list(self.client.mlsd())
    for (name, facts) in ls:
        self.assertIsInstance(name, str)
        self.assertIsInstance(facts, dict)
        self.assertTrue(name)
        self.assertIn('type', facts)
        self.assertIn('perm', facts)
        self.assertIn('unique', facts)

    def set_data(data):
        self.server.handler_instance.next_data = data

    def test_entry(line, type=None, perm=None, unique=None, name=None):
        type = 'type' if type is None else type
        perm = 'perm' if perm is None else perm
        unique = 'unique' if unique is None else unique
        name = 'name' if name is None else name
        set_data(line)
        (_name, facts) = next(self.client.mlsd())
        self.assertEqual(_name, name)
        self.assertEqual(facts['type'], type)
        self.assertEqual(facts['perm'], perm)
        self.assertEqual(facts['unique'], unique)
    test_entry('type=type;perm=perm;unique=unique; name\r\n')
    test_entry('type=ty=pe;perm=perm;unique=unique; name\r\n', type='ty=pe')
    test_entry('type==type;perm=perm;unique=unique; name\r\n', type='=type')
    test_entry('type=t=y=pe;perm=perm;unique=unique; name\r\n', type='t=y=pe')
    test_entry('type=====;perm=perm;unique=unique; name\r\n', type='====')
    test_entry('type=type;perm=perm;unique=unique; na me\r\n', name='na me')
    test_entry('type=type;perm=perm;unique=unique; name \r\n', name='name ')
    test_entry('type=type;perm=perm;unique=unique;  name\r\n', name=' name')
    test_entry('type=type;perm=perm;unique=unique; n am  e\r\n', name='n am  e')
    test_entry('type=type;perm=perm;unique=unique; na;me\r\n', name='na;me')
    test_entry('type=type;perm=perm;unique=unique; ;name\r\n', name=';name')
    test_entry('type=type;perm=perm;unique=unique; ;name;\r\n', name=';name;')
    test_entry('type=type;perm=perm;unique=unique; ;;;;\r\n', name=';;;;')
    set_data('Type=type;TyPe=perm;UNIQUE=unique; name\r\n')
    (_name, facts) = next(self.client.mlsd())
    for x in facts:
        self.assertTrue(x.islower())
    set_data('')
    self.assertRaises(StopIteration, next, self.client.mlsd())
    set_data('')
    for x in self.client.mlsd():
        self.fail('unexpected data %s' % x)
