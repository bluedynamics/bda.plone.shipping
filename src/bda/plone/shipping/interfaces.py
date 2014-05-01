from zope.interface import Interface
from zope.interface import Attribute


class IShippingExtensionLayer(Interface):
    """Browser layer for bda.plone.shipping.
    """


class IShippingSettings(Interface):
    """Shipping availability and default settings.
    """
    available = Attribute(u"List of available shipping method ids")

    default = Attribute(u"Default shipping method")


class IShipping(Interface):
    """Single shipping method.
    """
    sid = Attribute(u"Unique shipping method id. Shipping method adapter is "
                    u"also registered under this name.")

    label = Attribute(u"Shipping method label")

    description = Attribute(u"Shipping method description")

    available = Attribute(u"Flag whether shipping method is available in "
                          u"recent payment cycle.")

    default = Attribute(u"Flag whether this shipping method is default.")

    def net(items):
        """Calculate shipping costs net value for items and return as Decimal.

        :param items: items in the cart
        :param type: list of 3-tuples containing ``(uid, count, comment)``
        """

    def vat(items):
        """Calculate shipping costs vat value for items and return as Decimal.

        :param items: items in the cart
        :param type: list of 3-tuples containing ``(uid, count, comment)``
        """

    def calculate(items):
        """Calculate shipping costs for items and return as Decimal.

        NOTE: This function is kept for B/C reasons and gets removed as of
        ``bda.plone.shipping`` 1.0.

        :param items: items in the cart
        :param type: list of 3-tuples containing ``(uid, count, comment)``
        """


class IShippingItem(Interface):
    """Provide shipping information for item.
    """

    shippable = Attribute(u"Flag whether item is shippable, i.e. downloads "
                          u"are not.")

    weight = Attribute(u"Weight of shipping item. ``None`` means no weight.")


class IItemDelivery(Interface):
    """Delivery information for item.
    """

    delivery_duration = Attribute(u"Duration in which item can be delivered "
                                  u"as string.")
