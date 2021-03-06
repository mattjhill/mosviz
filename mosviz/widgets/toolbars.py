import os

from glue.viewers.common.qt.toolbar import BasicToolbar
from glue.viewers.common.qt.tool import CheckableTool, Tool

from qtpy.QtWidgets import QAction, QComboBox, QSpacerItem, QMenu, QToolButton, QWidgetAction
from qtpy.QtGui import QIcon
from qtpy.QtCore import Qt

__all__ = ['CyclePreviousTool', 'CycleForwardTool', 'MOSViewerToolbar']

class CyclePreviousTool(Tool):
    def __init__(self, viewer, toolbar=None):
        super(CyclePreviousTool, self).__init__(viewer=viewer)
        self.tool_id = 'mv:previous'
        self.action_text = "Previous"
        self.tool_tip = "Previous source in selection"
        self.shortcut = "P"
        self.checkable = False
        self.toolbar = toolbar

    def activate(self):
        pass


class CycleForwardTool(Tool):
    def __init__(self, viewer, toolbar=None):
        super(CycleForwardTool, self).__init__(viewer=viewer)
        self.tool_id = 'mv:next'
        self.action_text = "Next"
        self.tool_tip = "Next source in selection"
        self.shortcut = "N"
        self.checkable = False
        self.toolbar = toolbar

    def activate(self):
        pass


class MOSViewerToolbar(BasicToolbar):
    def __init__(self, *args, **kwargs):
        super(MOSViewerToolbar, self).__init__(*args, **kwargs)
        # self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # Define icon path
        icon_path = os.path.join(os.path.dirname(__file__),
                                 'ui', 'icons')

        # Define the toolbar actions
        self.cycle_previous_action = QAction(
            QIcon(os.path.join(icon_path, "Previous-96.png")),
            "Previous", self)
        self.cycle_next_action = QAction(
            QIcon(os.path.join(icon_path, "Next-96.png")),
            "Next", self)

        # Include the dropdown widget
        self.source_select = QComboBox()

        # Add the items to the toolbar
        self.addAction(self.cycle_previous_action)
        self.addAction(self.cycle_next_action)
        self.addWidget(self.source_select)

        # Include a button to open spectrum in specviz
        self.open_specviz = QAction(
            QIcon(os.path.join(icon_path, "External-96.png")),
            "Open in SpecViz", self)

        # Create a tool button to hold the lock axes menu object
        tool_button = QToolButton(self)
        tool_button.setText("Axes Settings")
        tool_button.setIcon(QIcon(os.path.join(icon_path, "Settings-96.png")))
        tool_button.setPopupMode(QToolButton.MenuButtonPopup)

        # Create a menu for the axes settings drop down
        self.settings_menu = QMenu(self)

        # Add lock x axis action
        self.lock_x_action = QAction("Lock X Axis",
                                     self.settings_menu)
        self.lock_x_action.setCheckable(True)

        # Add lock y axis action
        self.lock_y_action = QAction("Lock Y Axis",
                                     self.settings_menu)
        self.lock_y_action.setCheckable(True)

        # Add the actions to the menu
        self.settings_menu.addAction(self.lock_x_action)
        self.settings_menu.addAction(self.lock_y_action)

        # Set the menu object on the tool button
        tool_button.setMenu(self.settings_menu)

        # Create a widget action object to hold the tool button, this way the
        # toolbar behaves the way it's expected to
        tool_button_action = QWidgetAction(self)
        tool_button_action.setDefaultWidget(tool_button)

        self.addAction(tool_button_action)
        self.addSeparator()
        self.addAction(self.open_specviz)
