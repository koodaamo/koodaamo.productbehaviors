from zope import schema
from zope.interface import alsoProvides, implementer
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives as form
from plone.supermodel import model

from koodaamo.productbehaviors import MessageFactory as _mf


class IBasicBrandInfo(model.Schema):
    """Behavior interface to make a type support brand and model."""

    brand = schema.TextLine(
        title=_mf(u'label_brand', default=u'Brand'),
        required=True
    )

    model = schema.TextLine(
        title=_mf(u'label_model', default=u'Model'),
        required=True
    )

form.order_before(model='*')
form.order_before(brand='*')

alsoProvides(IBasicBrandInfo, IFormFieldProvider)


@implementer(IBasicBrandInfo)
class BasicBrandInfo(object):
    ""

    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        ""
        return self.context.brand + ' ' + self.context.model

    def Title(self):
        "get the title"
        return self.title

    def setTitle(self, title):
        ""
        return
