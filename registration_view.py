# -*- coding: utf-8 -*-

"""
Module implementing RegistrationView.
"""
from qgis.PyQt import uic
from qgis.PyQt.QtCore import pyqtSlot
from qgis.PyQt.QtWidgets import QDialog
import os

    
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'registration_view.ui'))


class RegistrationView(QDialog, FORM_CLASS):
    """
    Class documentation goes here.
    """
    def __init__(self, link,  parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(RegistrationView, self).__init__(parent)
        self.setupUi(self)
        self.link = link
    
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_buttonBox_rejected(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError