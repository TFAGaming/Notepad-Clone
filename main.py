from tkinter import *
import tkinter
from tkinter import messagebox as msgbox, ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
import datetime

__AppName = 'Notepad Clone'
__AppVersion = 'v1.0.0'

print('[i] Started running the program.')
print('[i] Creating the app...')

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

    secondGui.title('Set font')
    secondGui.iconbitmap('icon.ico')
    secondGui.geometry('300x325')
    secondGui.resizable(0, 0)

    frameFirst = LabelFrame(secondGui, text='Set font size')
    frameFirst.pack()

    fontChangerScale = Scale(frameFirst, from_=1, to=100, orient=HORIZONTAL, length=265)
    fontChangerScale.set(15)
    fontChangerScale.pack()

    secondFrame = LabelFrame(secondGui, text='Set font family')
    secondFrame.pack()

    varFontFamily = StringVar(secondGui)

    fontFamilyEntry = Entry(secondFrame, textvariable=varFontFamily, width=45)
    fontFamilyEntry.pack()

    thirdFrame = LabelFrame(secondGui, text='Text tester')
    thirdFrame.pack()

    labelTester = Label(thirdFrame, text='AaBbCc', justify=LEFT)
    labelTester.pack()

    def __CheckData_setFont_Function(num):
        try:
            if (num == 1):
                editor.config(font=(varFontFamily.get(), fontChangerScale.get()))
                return secondGui.destroy()
            else:
                labelTester.config(font=(varFontFamily.get(), fontChangerScale.get()))

        except:
            _showErrorMsg('UnknownErrorSource: Something went wrong, please try again.')

    btnsFrame = Frame(secondGui)
    btnsFrame.pack(side=BOTTOM)

    buttonOK = Button(btnsFrame, text='OK & Exit', width=10, command=lambda: __CheckData_setFont_Function(1))
    buttonOK.pack(padx=5, pady=5, side=RIGHT)

    buttonTEST = Button(btnsFrame, text='Test', width=10, command=lambda: __CheckData_setFont_Function(0))
    buttonTEST.pack(padx=5, pady=5, side=LEFT)

# File menu
file_menu = tkinter.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open file', command=_openFile)
file_menu.add_separator()
file_menu.add_command(label='Save', command=_save)
file_menu.add_command(label='Save as', command=_saveAs)
menu_bar.add_cascade(label='File', menu=file_menu)

# Editor menu
editor_menu = tkinter.Menu(menu_bar, tearoff=0)
editor_menu.add_command(label='Undo', command=_undo, accelerator='(Ctrl + Z)')
editor_menu.add_command(label='Redo', command=_redo, accelerator='(Ctrl + Y)')
editor_menu.add_separator()
editor_menu.add_command(label='Clear', command=_editorClear)
editor_menu.add_command(label='Set font', command=_setFont, accelerator='(Ctrl + F)')
menu_bar.add_cascade(label='Edit', menu=editor_menu)

# Window menu
wind_menu = tkinter.Menu(menu_bar, tearoff=0)
wind_menu_args = tkinter.Menu(wind_menu, tearoff=0)

wind_menu_args.add_command(label='Dark', command=_setThemeDark)
wind_menu_args.add_command(label='Light', command=_setThemeLight)

wind_menu.add_cascade(label='Set theme', menu=wind_menu_args)

wind_menu_args_a = tkinter.Menu(wind_menu, tearoff=0)

wind_menu_args_a.add_command(label='New window', command=None, state="disabled")

wind_menu.add_cascade(label='Open', menu=wind_menu_args_a)
wind_menu.add_separator()
wind_menu.add_command(label='Exit', command=_checkToSaveAndQuit, accelerator='(Alt + F4)')
menu_bar.add_cascade(label='Window', menu=wind_menu)

# Help menu
help_menu = tkinter.Menu(menu_bar, tearoff=0)
help_menu.add_command(label='Website', command=None, state="disabled")
help_menu.add_command(label='Info', command=_guiInfo)
menu_bar.add_cascade(label='Help?', menu=help_menu)

# Adding the menus
gui.config(menu=menu_bar)

# Frame
frame = Frame(gui, width=gui.winfo_width(), height=gui.winfo_height())
frame.pack()

# Editor
editor = tkinter.Text(frame, width=gui.winfo_width(), height=gui.winfo_height(), undo=True, font=('Times New Roman', 15))
editor.pack(padx=5, pady=5)

# Editor commands
editor_cmds = Menu(frame, tearoff=0)
editor_cmds.add_command(label='Set font', command=_setFont, accelerator='(Ctrl + F)')
editor_cmds.add_separator()
editor_cmds.add_command(label='Undo', command=_undo, accelerator='(Ctrl + Z)')
editor_cmds.add_command(label='Redo', command=_redo, accelerator='(Ctrl + Y)')
editor_cmds.add_separator()
editor_cmds.add_command(label='Copy', command=_showEditCmdsCopyCmd, accelerator='(Ctrl + C)')
editor_cmds.add_command(label='Cut', command=_showEditCmdsCutCmd, accelerator='(Ctrl + X)')
editor_cmds.add_command(label='Paste', command=_showEditCmdsPasteCmd, accelerator='(Ctrl + V)')
editor_cmds.add_separator()
editor_cmds.add_command(label='Select all', command=_showEditCmdsSelectAllCmd)
editor_cmds.add_command(label='Delete', command=_showEditCmdsDeleteCmd, state='active')

# Key binds
editor.bind('<Button - 3>', _showEditorCmds)
editor.bind('<Control-Key-z>', lambda __uselessVarLoL: _undo())
editor.bind('<Control-Key-y>', lambda __uselessVarLoL: _redo())
editor.bind('<Control-Key-f>', lambda __uselessVarLoL: _setFont())

print('[i] App is now running.')

gui.mainloop()

# All credits to TFAGaming:
# https://github.com/TFAGaming
