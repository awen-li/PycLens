# Source Generated with Decompyle++
# File: cpython-310-b89e5b6e146f.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    values = [
        ((0, 0, 0), (0, 0, 0)),
        ((0, 0, 1), (0.666667, 1, 1)),
        ((0, 1, 0), (0.333333, 1, 1)),
        ((0, 1, 1), (0.5, 1, 1)),
        ((1, 0, 0), (0, 1, 1)),
        ((1, 0, 1), (0.833333, 1, 1)),
        ((1, 1, 0), (0.166667, 1, 1)),
        ((1, 1, 1), (0, 0, 1)),
        ((0.5, 0.5, 0.5), (0, 0, 0.5))]
    for rgb, hsv in f'''''':
        self.assertTripleEqual(hsv, colorsys.rgb_to_hsv(rgb))
        self.assertTripleEqual(rgb, colorsys.hsv_to_rgb(hsv))

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
