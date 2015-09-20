# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plomino.wizard


class PlominoWizardLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plomino.wizard)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plomino.wizard:default')


PLOMINO_WIZARD_FIXTURE = PlominoWizardLayer()


PLOMINO_WIZARD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLOMINO_WIZARD_FIXTURE,),
    name='PlominoWizardLayer:IntegrationTesting'
)


PLOMINO_WIZARD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLOMINO_WIZARD_FIXTURE,),
    name='PlominoWizardLayer:FunctionalTesting'
)


PLOMINO_WIZARD_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLOMINO_WIZARD_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlominoWizardLayer:AcceptanceTesting'
)
