# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_modify_unregister

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.SELECTOR.__name__ == 'EpollSelector':
        patch = unittest.mock.patch('selectors.EpollSelector._selector_cls')
    elif self.SELECTOR.__name__ == 'PollSelector':
        patch = unittest.mock.patch('selectors.PollSelector._selector_cls')
    elif self.SELECTOR.__name__ == 'DevpollSelector':
        patch = unittest.mock.patch('selectors.DevpollSelector._selector_cls')
    else:
        raise self.skipTest('')
    with patch as m:
        m.return_value.modify = unittest.mock.Mock(side_effect=ZeroDivisionError)
        s = self.SELECTOR()
        self.addCleanup(s.close)
        (rd, wr) = self.make_socketpair()
        s.register(rd, selectors.EVENT_READ)
        self.assertEqual(len(s._map), 1)
        with self.assertRaises(ZeroDivisionError):
            s.modify(rd, selectors.EVENT_WRITE)
        self.assertEqual(len(s._map), 0)
