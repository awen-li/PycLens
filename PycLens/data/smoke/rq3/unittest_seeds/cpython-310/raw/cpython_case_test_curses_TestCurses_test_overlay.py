# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_overlay

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    srcwin = curses.newwin(5, 18, 3, 4)
    lorem_ipsum(srcwin)
    dstwin = curses.newwin(7, 17, 5, 7)
    for i in range(6):
        dstwin.addstr(i, 0, '_' * 17)
    srcwin.overlay(dstwin)
    self.assertEqual(dstwin.instr(0, 0), b'sectetur_________')
    self.assertEqual(dstwin.instr(1, 0), b'piscing_elit,____')
    self.assertEqual(dstwin.instr(2, 0), b'_do_eiusmod______')
    self.assertEqual(dstwin.instr(3, 0), b'_________________')
    srcwin.overwrite(dstwin)
    self.assertEqual(dstwin.instr(0, 0), b'sectetur       __')
    self.assertEqual(dstwin.instr(1, 0), b'piscing elit,  __')
    self.assertEqual(dstwin.instr(2, 0), b' do eiusmod    __')
    self.assertEqual(dstwin.instr(3, 0), b'_________________')
    srcwin.overlay(dstwin, 1, 4, 3, 2, 4, 11)
    self.assertEqual(dstwin.instr(3, 0), b'__r_sit_amet_____')
    self.assertEqual(dstwin.instr(4, 0), b'__ectetur________')
    self.assertEqual(dstwin.instr(5, 0), b'_________________')
    srcwin.overwrite(dstwin, 1, 4, 3, 2, 4, 11)
    self.assertEqual(dstwin.instr(3, 0), b'__r sit amet_____')
    self.assertEqual(dstwin.instr(4, 0), b'__ectetur   _____')
    self.assertEqual(dstwin.instr(5, 0), b'_________________')
