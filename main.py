from tkinter import *
import tkinter
from tkinter import messagebox as msgbox, ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
import datetime
from tkinter.font import Font
import webbrowser

__AppName = 'MyNoteBook'
__AppVersion = '1.0.0'

print(f'{__AppName} [{__AppVersion}]\n(c) Copyright {__AppName}, all rights reserved.\n')
print('[i] Starting up the app...')

gui = tkinter.Tk()

gui.geometry("1000x600")
# gui.resizable(0, 0)
gui.title(f'[Noname] - {__AppName}')
gui.iconbitmap('icon.ico')

menu_bar = tkinter.Menu(gui)

file_path = ''
dataFile = ''

def _showInfoMsg(msg):
    msgbox.showinfo(f'{__AppName}', msg)

def _showWarnMsg(msg):
    msgbox.showwarning(f'{__AppName}', msg)

def _showErrorMsg(msg):
    msgbox.showerror(f'{__AppName}', msg)

def _setFilePath(path):
    global file_path
    file_path = path

def _openFile():
    if (editor.get('1.0', END) != dataFile):
        res = msgbox.askyesno(f'{__AppName}', 'The current opened file is not saved, are you sure that you want to open another file?')

        if (res == False):
            return

    path = askopenfilename(filetypes=[('Text Files', '*.txt')])

    if path == '': return

    try:
        with open(path, 'r') as file:
            text = file.read()

            editor.delete('1.0', END)
            editor.insert('1.0', text)

            file.close()

            splitted = path.split('/')
            chosen = splitted[len(splitted) - 1]

            gui.title(f'{chosen} - {__AppName}')

            _setFilePath(path)
    except:
        _showErrorMsg('ReadingFilesError: Couldn\'t read the path file or reading it.')

def _editorClear():
    editor.delete('1.0', END)

def _save():
    if (file_path == ''):
        _saveAs()
        return

    path = file_path

    try:
        with open(path, 'w') as file:
            text = editor.get('1.0', END)
            file.write(text)

            global dataFile
            dataFile = text

            file.close()

            _setFilePath(path)
    except:
        _showErrorMsg('ReadingFilesError: Couldn\'t read the path file or writing it.')


def _saveAs():
    path = asksaveasfilename(filetypes=[('Text Files', '*.txt')])

    if (path == ''): return 0

    try:
        with open(path, 'w') as file:
            text = editor.get('1.0', END)
            file.write(text)

            global dataFile
            dataFile = text

            file.close()

            _setFilePath(path)

        return 1
    except:
        _showErrorMsg('ReadingFilesError: Couldn\'t read the path file or writing it.')
        return 0

def _checkToSaveAndQuit():
    if (editor.get('1.0', END) == dataFile):
        gui.quit()
    else:
        res = msgbox.askyesno(f'{__AppName}', 'The current opened file is not saved, are you sure that you want to quit?')

        if (res == True):
            gui.quit()
        else: return

def _checkToSaveAndNew():
    def __CLEAR():
        editor.delete('1.0', END)
        gui.title(f'[Noname] - {__AppName}')
        global file_path
        global dataFile
        file_path = ''
        dataFile = ''

    if (editor.get('1.0', END) == dataFile):
        __CLEAR()
    else:
        res = msgbox.askyesno(f'{__AppName}', 'The current opened file is not saved, are you sure that you want to open new one?')

        if (res == True):
            __CLEAR()
        else: return

def _setThemeDark():
    editor.config(bg='#282c34', fg='#ffffff')
    gui.config(bg='#303434')

def _setThemeLight():
    editor.config(bg='#ffffff', fg='#000000')
    gui.config(bg='#303434')

def _showEditorCmds(event):
    editor_cmds.tk_popup(event.x_root, event.y_root)

def _showEditCmdsCopyCmd():
    editor.event_generate("<<Copy>>")

def _showEditCmdsCutCmd():
    editor.event_generate("<<Cut>>")

def _showEditCmdsPasteCmd():
    editor.event_generate("<<Paste>>")

def _showEditCmdsSelectAllCmd():
    editor.event_generate("<<SelectAll>>")

def _showEditCmdsDeleteCmd():
    editor.event_generate("<<Clear>>")

def _undo():
    try:
        editor.edit_undo()
        return
    except:
        _showWarnMsg('There is nothing to undo.')
        return

def _redo():
    try:
        editor.edit_redo()
        return
    except:
        _showWarnMsg('There is nothing to redo.')
        return

def _guiInfo():
    return _showInfoMsg(f'Developer: T.F.A#7524\nLast version: {__AppVersion}\n\n© {__AppName} - {datetime.date.today().year}, all rights reserved.')

def _setFont():
    secondGui = Toplevel()

    secondGui.title('Set editor font')
    secondGui.iconbitmap('icon.ico')
    secondGui.geometry('300x400')
    secondGui.resizable(0, 0)

    # Font size
    frameFirst = LabelFrame(secondGui, text='Set font size')
    frameFirst.pack()

    fontChangerScale = Scale(frameFirst, from_=1, to=100, orient=HORIZONTAL, length=265)
    fontChangerScale.set(15)
    fontChangerScale.pack()

    # Font family & Color
    idkFrame = Frame(secondGui)
    idkFrame.pack()

    aFrame = LabelFrame(idkFrame, text='Set font family')
    aFrame.pack(side=LEFT, padx=5)

    varFontFamily = StringVar(secondGui)

    fontFamilyEntry = Entry(aFrame, textvariable=varFontFamily)
    fontFamilyEntry.pack(padx=5, pady=5)

    bFrame = LabelFrame(idkFrame, text='Set font color')
    bFrame.pack(side=RIGHT, padx=5)

    varColor = StringVar(secondGui)

    fontColor = ttk.OptionMenu(bFrame, varColor, 'Black', 'Red', 'Orange', 'Yellow', 'Lime', 'Green', 'Cyan', 'Blue', 'Aqua', 'Purple', 'Magenta', 'Pink', 'Brown', 'Gray', 'Black', 'White')
    fontColor.config(width=15)
    fontColor.pack(padx=5, pady=5)

    # Font config
    thirdFrame = LabelFrame(secondGui, text='Other font config')
    thirdFrame.pack()

    boldVar = IntVar(secondGui)
    boldCheck = Checkbutton(thirdFrame, text='Bold', variable=boldVar)
    boldCheck.pack(side=LEFT)

    underlinedVar = IntVar(secondGui)
    underlinedCheck = Checkbutton(thirdFrame, text='Underlined', variable=underlinedVar)
    underlinedCheck.pack(side=RIGHT)

    overstrickedVar = IntVar(secondGui)
    overstrickedCheck = Checkbutton(thirdFrame, text='Oversticked', variable=overstrickedVar)
    overstrickedCheck.pack(side=RIGHT)

    italicVar = IntVar(secondGui)
    italicCheck = Checkbutton(thirdFrame, text='Italic', variable=italicVar)
    italicCheck.pack(side=LEFT)

    fourthFrame = LabelFrame(secondGui, text='Text tester')
    fourthFrame.pack()
    
    labelTester = Label(fourthFrame, text='AaBbZzYy', justify=LEFT)
    labelTester.pack(padx=5, pady=5)

    def __CheckData_setFont_Function(num):
        try:
            booleanUnderlined = False
            booleanOverstricked = False
            weightBold = 'normal'
            slantItalic = 'roman'
            color = 'black'

            if (underlinedVar.get() == 1):
                booleanUnderlined = True

            if (boldVar.get() == 1):
                weightBold = 'bold'

            if (overstrickedVar.get() == 1):
                booleanOverstricked = True

            if (italicVar.get() == 1):
                slantItalic = 'italic'

            if (len(varColor.get()) >= 1):
                color = varColor.get()

            nowFont = Font(
                family=varFontFamily.get(),
                size=fontChangerScale.get(),
                underline=booleanUnderlined,
                weight=weightBold,
                overstrike=booleanOverstricked,
                slant=slantItalic,
            )

            if (num == 1):
                editor.config(font=nowFont, fg=color)
                return secondGui.destroy()
            elif (num == 0):
                labelTester.config(font=nowFont, fg=color)
            else: # 2
                labelTester.config(font=('Monospace', 15), fg='black')
                fontChangerScale.set(15)
                varFontFamily.set('Monospace')
                varColor.set('Black')
                boldCheck.deselect()
                underlinedCheck.deselect()
                overstrickedCheck.deselect()
                italicCheck.deselect()
        except:
            _showErrorMsg('UnknownErrorSource: Something went wrong, please try again.')

    btnsFrame = Frame(secondGui)
    btnsFrame.pack(side=BOTTOM)

    buttonOK = Button(btnsFrame, text='OK & Exit', width=10, command=lambda: __CheckData_setFont_Function(1))
    buttonOK.pack(padx=5, pady=5, side=RIGHT)

    buttonSETDEFAULT = Button(btnsFrame, text='Set default', width=10, command=lambda: __CheckData_setFont_Function(2))
    buttonSETDEFAULT.pack(padx=5, pady=5, side=RIGHT)

    buttonTEST = Button(btnsFrame, text='Test font', width=10, command=lambda: __CheckData_setFont_Function(0))
    buttonTEST.pack(padx=5, pady=5, side=LEFT)

def _openWebsite():
    _showInfoMsg('You are going to be redirected to a website.')

    webbrowser.open('www.google.com')
    return

# File menu
file_menu = tkinter.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', command=_checkToSaveAndNew, accelerator='Ctrl + N')
file_menu.add_separator()
file_menu.add_command(label='Open file', command=_openFile, accelerator='Ctrl + O')
file_menu.add_separator()
file_menu.add_command(label='Save', command=_save, accelerator='Ctrl + S')
file_menu.add_command(label='Save as', command=_saveAs)
menu_bar.add_cascade(label='File', menu=file_menu)

# Editor menu
editor_menu = tkinter.Menu(menu_bar, tearoff=0)
editor_menu.add_command(label='Undo', command=_undo, accelerator='Ctrl + Z')
editor_menu.add_command(label='Redo', command=_redo, accelerator='Ctrl + Y')
editor_menu.add_separator()
editor_menu.add_command(label='Set font', command=_setFont, accelerator='Ctrl + F')
editor_menu.add_command(label='Clear all text', command=_editorClear)
menu_bar.add_cascade(label='Edit', menu=editor_menu)

# Window menu
wind_menu = tkinter.Menu(menu_bar, tearoff=0)
wind_menu_args = tkinter.Menu(wind_menu, tearoff=0)

wind_menu_args.add_command(label='Dark', command=_setThemeDark)
wind_menu_args.add_command(label='Light', command=_setThemeLight)

wind_menu.add_cascade(label='Set theme', menu=wind_menu_args)

wind_menu.add_separator()
wind_menu.add_command(label='Exit', command=_checkToSaveAndQuit, accelerator='Alt + F4')
menu_bar.add_cascade(label='Window', menu=wind_menu)

# Help menu
help_menu = tkinter.Menu(menu_bar, tearoff=0)
help_menu.add_command(label='Website', command=_openWebsite)
help_menu.add_command(label='Info', command=_guiInfo)
menu_bar.add_cascade(label='Help?', menu=help_menu)

# Adding the menus
gui.config(menu=menu_bar)

# Frame
frame = Frame(gui, width=gui.winfo_width(), height=gui.winfo_height())
frame.pack()

# Scroll bar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Editor
editor = tkinter.Text(frame, width=gui.winfo_width(), height=gui.winfo_height(), undo=True, font=('Monospace', 15), yscrollcommand=scrollbar)
editor.pack(padx=5, pady=5)

# Config the scroll bar
scrollbar.config(command=editor.yview)

# Editor commands
editor_cmds = Menu(frame, tearoff=0)
editor_cmds.add_command(label='Set font', command=_setFont, accelerator='Ctrl + F')
editor_cmds.add_separator()
editor_cmds.add_command(label='Undo', command=_undo, accelerator='Ctrl + Z')
editor_cmds.add_command(label='Redo', command=_redo, accelerator='Ctrl + Y')
editor_cmds.add_separator()
editor_cmds.add_command(label='Copy', command=_showEditCmdsCopyCmd, accelerator='Ctrl + C')
editor_cmds.add_command(label='Cut', command=_showEditCmdsCutCmd, accelerator='Ctrl + X')
editor_cmds.add_command(label='Paste', command=_showEditCmdsPasteCmd, accelerator='Ctrl + V')
editor_cmds.add_separator()
editor_cmds.add_command(label='Select all', command=_showEditCmdsSelectAllCmd)
editor_cmds.add_command(label='Delete', command=_showEditCmdsDeleteCmd, state='active')

# Key binds
editor.bind('<Button-3>', _showEditorCmds)
editor.bind('<Control-Key-z>', lambda __uselessVarLoL: _undo())
editor.bind('<Control-Key-y>', lambda __uselessVarLoL: _redo())
editor.bind('<Control-Key-f>', lambda __uselessVarLoL: _setFont())
editor.bind('<Control-Key-s>', lambda __uselessVarLoL: _save())
editor.bind('<Control-Key-o>', lambda __uselessVarLoL: _openFile())
editor.bind('<Control-Key-n>', lambda __uselessVarLoL: _checkToSaveAndNew())
editor.bind('<Alt-F4>', lambda __uselessVarLoL: _checkToSaveAndQuit())

print('[i] App is now running.')

gui.mainloop()

# All credits to TFAGaming:
# https://github.com/TFAGaming
