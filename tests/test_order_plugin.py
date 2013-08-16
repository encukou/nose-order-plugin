from nose_order_plugin import ordered

@ordered
class TestOrderedPlugin(object):
    value = 1

    def test_z_first(self):
        type(self).value += 1
        assert self.value == 2

    def test_a_second(self):
        type(self).value += 1
        assert self.value == 3
