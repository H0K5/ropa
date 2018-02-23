from PyQt4 import QtGui as qg, QtCore as qc, uic

from ropa.backend import architectures
from ropa.gui import UI_PATH


class DialogController:
    def file_dialog(self, title):
        dialog = qg.QFileDialog()
        dialog.setWindowTitle(title)
        dialog.setFileMode(qg.QFileDialog.AnyFile)
        filenames = qc.QStringList()
        if dialog.exec_():
            filenames = dialog.selectedFiles()
            return filenames[0]
        raise Exception('Failed to open dialog')

    def arch_dialog(self):
        dialog = uic.loadUi(UI_PATH + '/arch_dialog.ui')
        dialog.setWindowTitle('Select Architecture')
        arch_table = dialog.findChild(qg.QTableWidget, 'arch_table')
        row = -1  # idk why
        arch_table.setColumnCount(1)
        arch_table.setRowCount(len(architectures))
        arch_table.horizontalHeader().setResizeMode(0, qg.QHeaderView.Stretch)
        have_selected = False
        for archi in architectures:
            item = qg.QTableWidgetItem(archi)
            item.setFlags(qc.Qt.ItemIsSelectable | qc.Qt.ItemIsEnabled)
            if not have_selected:
                item.setSelected(True)
                have_selected = True
            arch_table.setItem(row, 1, item)
            row += 1
        dialog.show()
        if dialog.exec_():
            if arch_table.selectedItems() is not None:
                arch = str(arch_table.selectedItems()[0].text())
            else:
                arch = 'x86'
            return arch
        return Exception('Failed to open dialog')
