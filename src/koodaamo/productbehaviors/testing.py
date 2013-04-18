from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class KoodaamoproductbehaviorsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import koodaamo.productbehaviors
        xmlconfig.file(
            'configure.zcml',
            koodaamo.productbehaviors,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'koodaamo.productbehaviors:default')

KOODAAMO_PRODUCTBEHAVIORS_FIXTURE = KoodaamoproductbehaviorsLayer()
KOODAAMO_PRODUCTBEHAVIORS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(KOODAAMO_PRODUCTBEHAVIORS_FIXTURE,),
    name="KoodaamoproductbehaviorsLayer:Integration"
)
KOODAAMO_PRODUCTBEHAVIORS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(KOODAAMO_PRODUCTBEHAVIORS_FIXTURE, z2.ZSERVER_FIXTURE),
    name="KoodaamoproductbehaviorsLayer:Functional"
)
