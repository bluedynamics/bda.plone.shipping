from zope.interface import (
    implementer,
    Interface,
)
from zope.component import (
    adapter,
    getAdapter,
    getAdapters,
)
from zope.i18nmessageid import MessageFactory
from .interfaces import IShipping


_ = MessageFactory('bda.plone.shipping')


class Shippings(object):
    
    def __init__(self, context):
        self.context = context
    
    def get(self, name):
        return getAdapter(self.context, IShipping, name=name)
    
    @property
    def shippings(self):
        adapters = getAdapters((self.context,), IShipping)
        return [_[1] for _ in adapters]
    
    @property
    def vocab(self):
        adapters = getAdapters((self.context,), IShipping)
        return [(_[0], _[1].label) for _ in adapters if _[1].available]
    
    @property
    def default(self):
        adapters = getAdapters((self.context,), IShipping)
        for name, shipping in adapters:
            if shipping.default:
                return name
        if adapters:
            return adapters[0][0]


@implementer(IShipping)
@adapter(Interface)
class Shipping(object):
    sid = None
    label = None
    available = False
    default = False
    
    def __init__(self, context):
        self.context = context
    
    def calculate(self, items):
        raise NotImplementedError(u"Abstract ``Shipping`` does not implement "
                                  u"``calculate``")


class FlatRate(Shipping):
    sid = 'flat_rate'
    label = _('flat_rate', 'Flat Rate')
    available = True
    default = True
    
    def calculate(self, items):
        pass
