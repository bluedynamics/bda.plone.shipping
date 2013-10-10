from zope.interface import (
    Interface,
    Attribute,
)


class IShippingExtensionLayer(Interface):
    """Browser layer for bda.plone.shipping.
    """


class IShipping(Interface):
    """Single shipping method.
    """
    sid = Attribute(u"Unique shipping method id. Shipping method adapter is "
                    u"also registered under this name.")
    
    label = Attribute(u"Shipping method label")
    
    available = Attribute(u"Flag whether shipping method is available in "
                          u"recent payment cycle.")
    
    default = Attribute(u"Flag whether this shipping method is default.")
    
    def calculate(self, items):
        """Calculate shipping costs.

        @param items: items to calculate shipping costs.
        @return: shipping costs as float.
        """


class IShippingItem(Interface):
    """Provide shipping information for item.
    """

    weight = Attribute(u"Weight of shipping item. ``None`` means no weight")
