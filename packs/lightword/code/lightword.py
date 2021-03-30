#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import os
import sys
import uuid, baran

from libabr import Files, Control, Res, App, System

files = Files()
control = Control()
res = Res()
app = App()

FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]
IMAGE_EXTENSIONS = ['.jpg','.png','.bmp']
HTML_EXTENSIONS = ['.htm', '.html']
def getdata (name):
    return control.read_record (name,'/etc/gui')
def hexuuid():
    return uuid.uuid4().hex

def splitext(p):
    return os.path.splitext(p)[1].lower()

class TextEdit(baran.BTextEdit):

    def __init__(self,ports):
        super(TextEdit, self).__init__()

        self.Env = ports[1]

    def canInsertFromMimeData(self, source):

        if source.hasImage():
            return True
        else:
            return super(TextEdit, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source):

        cursor = self.textCursor()
        document = self.document()

        if source.hasUrls():

            for u in source.urls():
                file_ext = splitext(str(u.toLocalFile()))
                if u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
                    image = QImage(u.toLocalFile())
                    document.addResource(QTextDocument.ImageResource, u, image)
                    cursor.insertImage(u.toLocalFile())

                else:
                    # If we hit a non-image or non-local URL break the loop and fall out
                    # to the super call & let Qt handle it
                    break

            else:
                # If all were valid images, finish here.
                return


        elif source.hasImage():
            image = source.imageData()
            uuid = hexuuid()
            document.addResource(QTextDocument.ImageResource, uuid, image)
            cursor.insertImage(uuid)
            return

        super(TextEdit, self).insertFromMimeData(source)


class MainApp(QMainWindow):
    def onCloseProcess (self):
        if not app.check(self.AppName):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)
    def __init__(self,ports, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        layout = QVBoxLayout()
        self.editor = TextEdit(ports)
        self.editor.setStyleSheet("""
                       QScrollBar
                       {
                       background : white;
                       }
                       QScrollBar::handle
                       {
                       background : #123456;
                       border-radius: 6% 6%;
                       }
                       QScrollBar::handle::pressed
                       {
                       background : #ABCDEF;
                       border-radius: 6% 6%;
                       }""".replace('white', getdata("menu.scroll.bgcolor")).replace('#123456',
                                                                                     getdata(
                                                                                         "menu.scroll.color")).replace(
            '6',
            getdata(
                "menu.scroll.round-size")).replace(
            '#ABCDEF', getdata("menu.scroll.color-hover")))

        # Setup the QTextEdit editor configuration
        self.editor.setAutoFormatting(QTextEdit.AutoAll)
        self.editor.selectionChanged.connect(self.update_format)
        # Initialize default font size.
        self.editor.setFont(self.Env.font())
        # We need to repeat the size to init the current format.
        self.editor.setFontPointSize(12)

        # If none, we haven't got a file open yet (or creating new).
        self.Widget.SetWindowTitle(res.get('@string/untitled'))

        layout.addWidget(self.editor)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.Widget.SetWindowIcon(QIcon(res.get(res.etc(self.AppName,"logo"))))

        self.setFont(self.Env.font())

        file_toolbar = QToolBar("File")
        file_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(file_toolbar)

        self.menuBar = QMenuBar()
        self.setMenuBar(self.menuBar)
        self.menuBar.setFont(self.Env.font())
        if getdata('submenu.direction')=='ltr':
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)
        file_menu = self.menuBar.addMenu(res.get('@string/file'))
        file_menu.setFont(self.Env.font())
        img = res.get('@icon/blue-fileopen')
        open_file_action = QAction(QIcon(img), res.get('@string/of'), self)
        open_file_action.setFont(self.Env.font())
        open_file_action.setStatusTip(res.get('@string/of'))
        open_file_action.triggered.connect(self.file_open)
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)
        img = res.get('@icon/document-save')
        save_file_action = QAction(QIcon(img), res.get('@string/sv'), self)
        save_file_action.setFont(self.Env.font())
        save_file_action.setStatusTip(res.get('@string/sv'))
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)
        img = res.get('@icon/document-save-as')
        saveas_file_action = QAction(QIcon(img), res.get('@string/sa'), self)
        saveas_file_action.setFont(self.Env.font())
        saveas_file_action.setStatusTip(res.get('@string/sa'))
        saveas_file_action.triggered.connect(self.file_saveas)
        file_menu.addAction(saveas_file_action)
        file_toolbar.addAction(saveas_file_action)

        edit_toolbar = QToolBar(res.get('@string/ed'))
        edit_toolbar.setFont(self.Env.font())
        edit_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar.addMenu(res.get('@string/ed'))
        edit_menu.setFont(self.Env.font())
        img = res.get('@icon/arrow-curve-180-left')
        undo_action = QAction(QIcon(img), res.get('@string/un'), self)
        undo_action.setFont(self.Env.font())
        undo_action.setStatusTip(res.get('@string/un'))
        undo_action.triggered.connect(self.editor.undo)
        edit_menu.addAction(undo_action)
        img = res.get('@icon/arrow-curve')
        redo_action = QAction(QIcon(img), res.get('@string/rd'), self)
        redo_action.setFont(self.Env.font())
        redo_action.setStatusTip(res.get('@string/rd'))
        redo_action.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()
        img = res.get('@icon/scissors')
        cut_action = QAction(QIcon(img), res.get('@string/ct'), self)
        cut_action.setFont(self.Env.font())
        cut_action.setStatusTip(res.get('@string/ct'))
        cut_action.setShortcut(QKeySequence.Cut)
        cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)
        edit_menu.addAction(cut_action)
        img = res.get('@icon/document-copy')
        copy_action = QAction(QIcon(img), res.get('@string/cp'), self)
        copy_action.setFont(self.Env.font())
        copy_action.setStatusTip(res.get('@string/cp'))
        cut_action.setShortcut(QKeySequence.Copy)
        copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)
        img = res.get('@icon/clipboard-paste-document-text')
        paste_action = QAction(QIcon(img), res.get('@string/pa'), self)
        paste_action.setFont(self.Env.font())
        paste_action.setStatusTip(res.get('@string/pa'))
        cut_action.setShortcut(QKeySequence.Paste)
        paste_action.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(paste_action)
        edit_menu.addAction(paste_action)
        img = res.get('@icon/selection-input')
        select_action = QAction(QIcon(img), res.get('@string/sll'), self)
        select_action.setStatusTip(res.get('@string/sll'))
        select_action.setFont(self.Env.font())
        cut_action.setShortcut(QKeySequence.SelectAll)
        select_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_action)

        edit_menu.addSeparator()
        img = res.get('@icon/arrow-continue')
        wrap_action = QAction(QIcon(img), res.get('@string/wtw'), self)
        wrap_action.setFont(self.Env.font())
        wrap_action.setStatusTip(res.get('@string/ttw'))
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.triggered.connect(self.edit_toggle_wrap)
        edit_menu.addAction(wrap_action)

        format_toolbar = QToolBar(res.get('@string/fm'))
        format_toolbar.setFont(self.Env.font())
        format_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(format_toolbar)
        format_menu = self.menuBar.addMenu(res.get('@string/fm'))
        format_menu.setFont(self.Env.font())

        # We need references to these actions/settings to update as selection changes, so attach to self.
        self.fonts = QFontComboBox()
        self.fonts.currentFontChanged.connect(self.editor.setCurrentFont)
        format_toolbar.addWidget(self.fonts)

        self.fontsize = QComboBox()
        self.fontsize.addItems([str(s) for s in FONT_SIZES])

        # Connect to the signal producing the text of the current selection. Convert the string to float
        # and set as the pointsize. We could also use the index + retrieve from FONT_SIZES.
        self.fontsize.currentIndexChanged[str].connect(lambda s: self.editor.setFontPointSize(float(s)) )
        format_toolbar.addWidget(self.fontsize)
        img = res.get('@icon/edit-bold')
        self.bold_action = QAction(QIcon(img), res.get('@string/bl'), self)
        self.bold_action.setStatusTip(res.get('@string/bl'))
        self.bold_action.setFont(self.Env.font())
        self.bold_action.setShortcut(QKeySequence.Bold)
        self.bold_action.setCheckable(True)
        self.bold_action.toggled.connect(lambda x: self.editor.setFontWeight(QFont.Bold if x else QFont.Normal))
        format_toolbar.addAction(self.bold_action)
        format_menu.addAction(self.bold_action)

        img = res.get('@icon/edit-italic')
        self.italic_action = QAction(QIcon(img), res.get('@string/it'), self)
        self.italic_action.setStatusTip(res.get('@string/it'))
        self.italic_action.setFont(self.Env.font())
        self.italic_action.setShortcut(QKeySequence.Italic)
        self.italic_action.setCheckable(True)
        self.italic_action.toggled.connect(self.editor.setFontItalic)
        format_toolbar.addAction(self.italic_action)
        format_menu.addAction(self.italic_action)

        img = res.get('@icon/edit-underline')
        self.underline_action = QAction(QIcon(img), res.get('@string/un'), self)
        self.underline_action.setFont(self.Env.font())
        self.underline_action.setStatusTip(res.get('@string/un'))
        self.underline_action.setShortcut(QKeySequence.Underline)
        self.underline_action.setCheckable(True)
        self.underline_action.toggled.connect(self.editor.setFontUnderline)
        format_toolbar.addAction(self.underline_action)
        format_menu.addAction(self.underline_action)

        format_menu.addSeparator()

        img = res.get('@icon/edit-alignment')
        self.alignl_action = QAction(QIcon(img), res.get('@string/al'), self)
        self.alignl_action.setStatusTip(res.get('@string/al'))
        self.alignl_action.setFont(self.Env.font())
        self.alignl_action.setCheckable(True)
        self.alignl_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignLeft))
        format_toolbar.addAction(self.alignl_action)
        format_menu.addAction(self.alignl_action)

        img = res.get('@icon/edit-alignment-center')
        self.alignc_action = QAction(QIcon(img), res.get('@string/ac'), self)
        self.alignc_action.setFont(self.Env.font())
        self.alignc_action.setStatusTip(res.get('@string/ac'))
        self.alignc_action.setCheckable(True)
        self.alignc_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignCenter))
        format_toolbar.addAction(self.alignc_action)
        format_menu.addAction(self.alignc_action)

        img = res.get('@icon/edit-alignment-right')
        self.alignr_action = QAction(QIcon(img), res.get('@string/ar'), self)
        self.alignr_action.setStatusTip(res.get('@string/ar'))
        self.alignr_action.setCheckable(True)
        self.alignl_action.setFont(self.Env.font())
        self.alignr_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignRight))
        format_toolbar.addAction(self.alignr_action)
        format_menu.addAction(self.alignr_action)

        img = res.get('@icon/edit-alignment-justify')
        self.alignj_action = QAction(QIcon(img), res.get('@string/jf'), self)
        self.alignj_action.setFont(self.Env.font())

        self.alignj_action.setStatusTip(res.get('@string/jf'))
        self.alignj_action.setFont(self.Env.font())
        self.alignj_action.setCheckable(True)
        self.alignj_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignJustify))
        format_toolbar.addAction(self.alignj_action)
        format_menu.addAction(self.alignj_action)

        format_group = QActionGroup(self)
        format_group.setExclusive(True)
        format_group.addAction(self.alignl_action)
        format_group.addAction(self.alignc_action)
        format_group.addAction(self.alignr_action)
        format_group.addAction(self.alignj_action)

        format_menu.addSeparator()

        # A list of all format-related widgets/actions, so we can disable/enable signals when updating.
        self._format_actions = [
            self.fonts,
            self.fontsize,
            self.bold_action,
            self.italic_action,
            self.underline_action,
            # We don't need to disable signals for alignment, as they are paragraph-wide.
        ]

        # Initialize.
        self.update_format()
        self.show()

    def block_signals(self, objects, b):
        for o in objects:
            o.blockSignals(b)

    def update_format(self):
        """
        Update the font format toolbar/actions when a new text selection is made. This is neccessary to keep
        toolbars/etc. in sync with the current edit state.
        :return:
        """
        # Disable signals for all format widgets, so changing values here does not trigger further formatting.
        self.block_signals(self._format_actions, True)

        self.fonts.setCurrentFont(self.editor.currentFont())
        # Nasty, but we get the font-size as a float but want it was an int
        self.fontsize.setCurrentText(str(int(self.editor.fontPointSize())))

        self.italic_action.setChecked(self.editor.fontItalic())
        self.underline_action.setChecked(self.editor.fontUnderline())
        self.bold_action.setChecked(self.editor.fontWeight() == QFont.Bold)

        self.alignl_action.setChecked(self.editor.alignment() == Qt.AlignLeft)
        self.alignc_action.setChecked(self.editor.alignment() == Qt.AlignCenter)
        self.alignr_action.setChecked(self.editor.alignment() == Qt.AlignRight)
        self.alignj_action.setChecked(self.editor.alignment() == Qt.AlignJustify)

        self.block_signals(self._format_actions, False)

    def file_open(self):
        app.switch('lightword')
        self.Env.RunApp('select', [res.get('@string/od'), 'open', self.file_open_])
        app.switch('lightword')

    def file_open_(self,filename):
        self.editor.setText(files.readall(filename))
        self.Widget.SetWindowTitle(files.output(filename))

        if self.Widget.WindowTitle() == '': self.Widget.SetWindowTitle(res.get('@string/untitled'))

    def file_save(self):
        if not self.Widget.WindowTitle() == res.get('@string/untitled'):
            files.write(files.output(self.Widget.WindowTitle()), self.editor.toHtml())
        else:
            app.switch('lightword')
            self.Env.RunApp('select', [res.get('@string/sd'), 'save', self.file_saveas_])
            app.switch('lightword')

    def file_save_(self,filename):
        text = self.editor.toHtml()
        files.write(filename, text)
        self.Widget.SetWindowTitle(filename)

    def file_saveas(self):
        app.switch('lightword')
        self.Env.RunApp('select', [res.get('@string/sad'), 'save-as', self.file_saveas_])
        app.switch('lightword')

    def file_saveas_(self,filename):
        files.write(filename, self.editor.toHtml())
        self.Widget.SetWindowTitle(files.output(filename))

    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode( 1 if self.editor.lineWrapMode() == 0 else 0 )