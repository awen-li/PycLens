# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_property

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Rect:

        @property
        def area(self):
            """Area of the rect"""
            return self.w * self.h
    self.assertEqual(self._get_summary_lines(Rect.area), '    Area of the rect\n')
    self.assertIn('\n |  area\n |      Area of the rect\n', pydoc.plain(pydoc.render_doc(Rect)))
