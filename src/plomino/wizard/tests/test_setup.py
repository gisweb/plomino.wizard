# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plomino.wizard.testing import PLOMINO_WIZARD_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that plomino.wizard is properly installed."""

    layer = PLOMINO_WIZARD_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plomino.wizard is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('plomino.wizard'))

    def test_browserlayer(self):
        """Test that IPlominoWizardLayer is registered."""
        from plomino.wizard.interfaces import IPlominoWizardLayer
        from plone.browserlayer import utils
        self.assertIn(IPlominoWizardLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLOMINO_WIZARD_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plomino.wizard'])

    def test_product_uninstalled(self):
        """Test if plomino.wizard is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('plomino.wizard'))
