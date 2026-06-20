# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: RequestHdrsTests_test_password_manager_default_port

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mgr = urllib.request.HTTPPasswordMgr()
    add = mgr.add_password
    find_user_pass = mgr.find_user_password
    add('f', 'http://g.example.com:80', '10', 'j')
    add('g', 'http://h.example.com', '11', 'k')
    add('h', 'i.example.com:80', '12', 'l')
    add('i', 'j.example.com', '13', 'm')
    self.assertEqual(find_user_pass('f', 'g.example.com:100'), (None, None))
    self.assertEqual(find_user_pass('f', 'g.example.com:80'), ('10', 'j'))
    self.assertEqual(find_user_pass('f', 'g.example.com'), (None, None))
    self.assertEqual(find_user_pass('f', 'http://g.example.com:100'), (None, None))
    self.assertEqual(find_user_pass('f', 'http://g.example.com:80'), ('10', 'j'))
    self.assertEqual(find_user_pass('f', 'http://g.example.com'), ('10', 'j'))
    self.assertEqual(find_user_pass('g', 'h.example.com'), ('11', 'k'))
    self.assertEqual(find_user_pass('g', 'h.example.com:80'), ('11', 'k'))
    self.assertEqual(find_user_pass('g', 'http://h.example.com:80'), ('11', 'k'))
    self.assertEqual(find_user_pass('h', 'i.example.com'), (None, None))
    self.assertEqual(find_user_pass('h', 'i.example.com:80'), ('12', 'l'))
    self.assertEqual(find_user_pass('h', 'http://i.example.com:80'), ('12', 'l'))
    self.assertEqual(find_user_pass('i', 'j.example.com'), ('13', 'm'))
    self.assertEqual(find_user_pass('i', 'j.example.com:80'), (None, None))
    self.assertEqual(find_user_pass('i', 'http://j.example.com'), ('13', 'm'))
    self.assertEqual(find_user_pass('i', 'http://j.example.com:80'), (None, None))
