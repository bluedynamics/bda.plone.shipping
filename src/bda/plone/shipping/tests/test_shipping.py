import unittest2 as unittest
from bda.plone.shipping.tests import (
    Shipping_INTEGRATION_TESTING,
    set_browserlayer,
)
from bda.plone.shipping import FlatRate, Shipping
from zope.component import provideAdapter
from zope.interface import Interface
from bda.plone.shipping.interfaces import IShipping


class MockShipping(Shipping):
    sid = 'mock_shipping'
    label = 'Mock Shipping'
    available = True
    default = False

    def calculate(self, items):
        return 10


class TestShipping(unittest.TestCase):
    layer = Shipping_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        set_browserlayer(self.request)
        provideAdapter(MockShipping)
        self.shipping = IShipping(self.portal)

    def test_shipping(self):
        mock = self.shipping
        self.assertEquals(mock.sid, "mock_shipping")
        self.assertEquals(mock.label, "Mock Shipping")
        self.assertEquals(mock.available, True)
        self.assertEquals(mock.default, False)
        self.assertEquals(mock.calculate([]), 10)
