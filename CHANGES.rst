
Changelog
=========

1.0a1 (unreleased)
------------------

- Replace unittest2 with untittest
  [llisa123]

- Add ``IShippingItem.free_shipping`` flag.
  [rnix]

- Plone 5 update
  [agitator]


0.4
---

- Add ``IShippingItem.shippable`` Attribute.
  [rnix]

- Implement ``available`` and ``default`` properties on
  ``bda.plone.shipping.Shipping`` using settings from
  ``bda.plone.shipping.interfaces.IShippingSettings``.
  [rnix]

- Introduce ``bda.plone.payment.interfaces.IShippingSettings``.
  [rnix]

- Deprecate ``IShipping.calculate``. Use ``IShipping.net`` and
  ``IShipping.vat`` instead.
  [rnix]

- Add ``description`` attribute to ``IShipping`` interface.
  [rnix]

- Remove ``FlatRate`` shipping.
  [rnix]


0.3
---

- Introduce ``IItemDelivery`` interface and corresponding base implementation.
  [rnix]

- Introduce ``IShippingItem`` interface.
  [rnix]


0.2
---

- Add tests.
  [thet]


0.1
---

- initial work.
  [rnix]
