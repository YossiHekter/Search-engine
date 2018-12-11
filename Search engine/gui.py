# gui class
# That class create the gui for this app
import os
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    gui_support.set_Tk_var()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    root.iconbitmap(os.path.join(base_path, "Resources/icon.ico"))
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    gui_support.set_Tk_var()
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
    sys.exit(0)


# create the main window of the app
class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"

        top.geometry("600x450+423+141")
        top.title("Search&find")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.bind('<Button-1>',lambda e:gui_support.xxx(e))

        self.insert_btn = tk.Button(top)
        self.insert_btn.place(relx=0.083, rely=0.422, height=24, width=35)
        self.insert_btn.configure(activebackground="#ececec")
        self.insert_btn.configure(activeforeground="#000000")
        self.insert_btn.configure(background="#d9d9d9")
        self.insert_btn.configure(disabledforeground="#a3a3a3")
        self.insert_btn.configure(foreground="#000000")
        self.insert_btn.configure(highlightbackground="#d9d9d9")
        self.insert_btn.configure(highlightcolor="black")
        self.insert_btn.configure(pady="0")
        self.insert_btn.configure(text='''Start''')
        self.insert_btn.bind('<Button-1>',lambda e:gui_support.insertButton(e))

        self.resert_btn = tk.Button(top)
        self.resert_btn.place(relx=0.083, rely=0.733, height=24, width=39)
        self.resert_btn.configure(activebackground="#ececec")
        self.resert_btn.configure(activeforeground="#000000")
        self.resert_btn.configure(background="#d9d9d9")
        self.resert_btn.configure(disabledforeground="#a3a3a3")
        self.resert_btn.configure(foreground="#000000")
        self.resert_btn.configure(highlightbackground="#d9d9d9")
        self.resert_btn.configure(highlightcolor="black")
        self.resert_btn.configure(pady="0")
        self.resert_btn.configure(text='''Reset''')
        self.resert_btn.bind('<Button-1>',lambda e:gui_support.resetButton(e))

        self.show_btn = tk.Button(top)
        self.show_btn.place(relx=0.083, rely=0.622, height=24, width=96)
        self.show_btn.configure(activebackground="#ececec")
        self.show_btn.configure(activeforeground="#000000")
        self.show_btn.configure(background="#d9d9d9")
        self.show_btn.configure(disabledforeground="#a3a3a3")
        self.show_btn.configure(foreground="#000000")
        self.show_btn.configure(highlightbackground="#d9d9d9")
        self.show_btn.configure(highlightcolor="black")
        self.show_btn.configure(pady="0")
        self.show_btn.configure(text='''Show dictionary''')
        self.show_btn.bind('<Button-1>',lambda e:gui_support.showButton(e))

        self.upload_btn = tk.Button(top)
        self.upload_btn.place(relx=0.083, rely=0.511, height=24, width=105)
        self.upload_btn.configure(activebackground="#ececec")
        self.upload_btn.configure(activeforeground="#000000")
        self.upload_btn.configure(background="#d9d9d9")
        self.upload_btn.configure(disabledforeground="#a3a3a3")
        self.upload_btn.configure(foreground="#000000")
        self.upload_btn.configure(highlightbackground="#d9d9d9")
        self.upload_btn.configure(highlightcolor="black")
        self.upload_btn.configure(pady="0")
        self.upload_btn.configure(text='''Upload dictionary''')
        self.upload_btn.bind('<Button-1>',lambda e:gui_support.uploadButton(e))

        self.stem_cbox = tk.Checkbutton(top)
        self.stem_cbox.place(relx=0.4, rely=0.378, relheight=0.056
                , relwidth=0.138)
        self.stem_cbox.configure(activebackground="#ececec")
        self.stem_cbox.configure(activeforeground="#000000")
        self.stem_cbox.configure(background="#d9d9d9")
        self.stem_cbox.configure(disabledforeground="#a3a3a3")
        self.stem_cbox.configure(foreground="#000000")
        self.stem_cbox.configure(highlightbackground="#d9d9d9")
        self.stem_cbox.configure(highlightcolor="black")
        self.stem_cbox.configure(justify='left')
        self.stem_cbox.configure(state='normal')
        self.stem_cbox.configure(text='''Stemming''')
        self.stem_cbox.configure(underline="0")
        self.stem_cbox.configure(variable=tk.IntVar())
        self.stem_cbox.bind('<Button-1>',lambda e:gui_support.stemCbox(e))

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.533, rely=0.556, relheight=0.16
                , relwidth=0.14)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=10)
        self.Listbox1.bind('<Button-1>',lambda e:gui_support.listBox(e))

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.083, rely=0.244, height=21, width=101)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Insert corpus path''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.083, rely=0.311, height=21, width=126)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Insert path to save files''')

        self.corpus_btn = tk.Button(top)
        self.corpus_btn.place(relx=0.7, rely=0.244, height=24, width=49)
        self.corpus_btn.configure(activebackground="#ececec")
        self.corpus_btn.configure(activeforeground="#000000")
        self.corpus_btn.configure(background="#d9d9d9")
        self.corpus_btn.configure(disabledforeground="#a3a3a3")
        self.corpus_btn.configure(foreground="#000000")
        self.corpus_btn.configure(highlightbackground="#d9d9d9")
        self.corpus_btn.configure(highlightcolor="black")
        self.corpus_btn.configure(pady="0")
        self.corpus_btn.configure(text='''Browse''')
        self.corpus_btn.bind('<Button-1>',lambda e:gui_support.browseCorpuse(e))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.7, rely=0.311, height=24, width=49)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Browse''')
        self.Button2.bind('<Button-1>',lambda e:gui_support.browseDestination(e))

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.517, rely=0.511, height=21, width=98)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Choose language''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.283, rely=0.067, height=51, width=224)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font10)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#501fef")
        self.Label5.configure(highlightcolor="#1f1863")
        self.Label5.configure(text='''Search Engine''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.35, rely=0.244, height=20, relwidth=0.307)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=184)
        self.Entry1.configure(x=tk.StringVar())

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.35, rely=0.311, height=20, relwidth=0.307)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=184)

if __name__ == '__main__':
    vp_start_gui()





