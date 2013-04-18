from zope import schema
from zope.interface import alsoProvides
from plone.autoform.interfaces import IFormFieldProvider
#from plone.autoform import directives as form
from plone.supermodel import model

from koodaamo.productbehaviors import MessageFactory as _mf


# physical dimensions

class IDimensioned(model.Schema):

    length = schema.Decimal(
        title=_mf(u'label_length', default=u'Length'),
        readonly=True
    )

    width = schema.Decimal(
        title=_mf(u'label_width', default=u'Width'),
        required=True
    )

    height = schema.Decimal(
        title=_mf(u'label_height', default=u'Height'),
        required=True
    )

    model.fieldset('physical',
            label=u"Physical attributes",
            fields=['length', 'height', 'width']
    )


# weight

class IWeighted(model.Schema):
    "anything with a weight"

    weight = schema.Decimal(
        title=_mf(u'label_weight', default=u'Weight'),
        required=True
    )

    # merged into IDimensioned
    model.fieldset('physical',
            label=u"Physical attributes",
            fields=['weight']
    )


class IBasicPhysicalInfo(IDimensioned, IWeighted):
    """Behavior interface to make a type support length, width, height and weight."""

alsoProvides(IBasicPhysicalInfo, IFormFieldProvider)

