# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_webbrowser.py
# case: ImportTest_test_register

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    webbrowser = import_helper.import_fresh_module('webbrowser')
    self.assertIsNone(webbrowser._tryorder)
    self.assertFalse(webbrowser._browsers)

    class ExampleBrowser:
        pass
    webbrowser.register('Example1', ExampleBrowser)
    self.assertTrue(webbrowser._tryorder)
    self.assertEqual(webbrowser._tryorder[-1], 'Example1')
    self.assertTrue(webbrowser._browsers)
    self.assertIn('example1', webbrowser._browsers)
    self.assertEqual(webbrowser._browsers['example1'], [ExampleBrowser, None])
