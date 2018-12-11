# The modol of the GUI
# That class control the logic of the GUI and is association with the system
# The function in this class are the "on action" function of any button of the gui
import datetime
import os
import pickle
import threading
from tkinter.messagebox import showinfo, showwarning
import Indexer
from tkinter import filedialog

import Parse
import ReadFile

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


corpus_path = ""  # the path of the corpus
dist_path = ""  # the path to save the output
list_of_language = []  # the language in the corpus
stemmer = False  # boolean that represent if the user ask for stemming
term_dictionary = {}  # all the terms in the corpus and there frequency
in_process = False  # boolean that represent if the system still in progress



def set_Tk_var():
    global che47
    che47 = tk.StringVar()


def browseCorpuse(p1):
    global corpus_path
    global in_process
    global w

    if not in_process:
        corpus_path = filedialog.askdirectory(title="Choose dir")
        w.Entry1.insert(0, corpus_path)

def browseDestination(p1):
    global dist_path
    global in_process
    global w

    if not in_process:
        dist_path = filedialog.askdirectory(title="Choose dir")
        w.Entry2.insert(0, dist_path)

def insertButton(p1, easygui=None):
    global stemmer
    global dist_path
    global corpus_path
    global list_of_language
    global w
    global in_process

    if not in_process:
        corpus_path = w.Entry1.get()
        dist_path = w.Entry2.get()
        if corpus_path =="" or dist_path == "":
            showwarning('Warning', 'Please insert Path to corpus and to save files.')
        else:
            in_process = True
            w.Listbox1.delete(0, tk.END)
            def callback():
                global stemmer
                global dist_path
                global corpus_path
                global root
                global w
                global in_process

                total = datetime.datetime.now()
                term_dictionary = {}
                num_of_post = Indexer.start_read(corpus_path, dist_path, term_dictionary, stemmer)
                num_of_doc = Indexer.merge_document_dictionary(dist_path, num_of_post, stemmer)
                t = threading.Thread(target=fill_list)
                t.start()
                Indexer.new_merge(dist_path, term_dictionary, num_of_post, stemmer)
                sort_key = sorted(term_dictionary)
                sort_term_dictionary = {}
                for key in sort_key:
                    sort_term_dictionary[key] = term_dictionary[key]
                if stemmer:
                    file = open(dist_path + "/term_dictionary_stemmer.pkl", "wb+")
                else:
                    file = open(dist_path + "/term_dictionary.pkl", "wb+")
                pickle.dump(sort_term_dictionary, file, pickle.HIGHEST_PROTOCOL)
                file.close()
                num_of_terms = len(sort_term_dictionary)
                total_time = str(datetime.datetime.now() - total)
                showinfo('info', 'The number of documents in corpus: ' + str(num_of_doc) + '\r\n' +
                         'The number of terms in the corpus: ' + str(num_of_terms) + '\r\n' +
                         'The total time: ' + str(total_time))
                w.insert_btn.configure(state='normal')
                w.resert_btn.configure(state='normal')
                w.show_btn.configure(state='normal')
                w.upload_btn.configure(state='normal')
                w.stem_cbox.configure(state='normal')
                w.corpus_btn.configure(state='normal')
                w.Button2.configure(state='normal')
                in_process = False

            t = threading.Thread(target=callback)
            t.start()
            w.insert_btn.configure(state='disable')
            w.resert_btn.configure(state='disable')
            w.show_btn.configure(state='disable')
            w.upload_btn.configure(state='disable')
            w.stem_cbox.configure(state='disable')
            w.corpus_btn.configure(state='disable')
            w.Button2.configure(state='disable')
            showinfo('info', 'Build the engine will take about 25 minutes.' + '\r\n' +
                     'When the process is finished the window keys will be released.' + '\r\n' +
                     'You can go make a cup of coffee in the meantime.')

def listBox(p1):
    global in_process

    if not in_process:
        print('gui_support.listBox')
        print('p1 = {0}'.format(p1))

def fill_list():
    global list_of_language
    global w

    if stemmer:
        file = open(dist_path + "/document_dictionary_stemmer.pkl", "rb+")
    else:
        file = open(dist_path + "/document_dictionary.pkl", "rb+")
    document_dictionary = pickle.load(file)
    file.close()
    for key in document_dictionary:
        language = document_dictionary[key].language
        if not language in list_of_language:
            if not language.isnumeric() and not language == "":
                list_of_language.append(language)
    list_of_language = sorted(list_of_language)
    i = 0
    for language in list_of_language:
        w.Listbox1.insert(i, language)
        i += 1

def resetButton(p1, easygui=None):
    global corpus_path
    global dist_path
    global list_of_language
    global stemmer
    global term_dictionary
    global w
    global in_process

    if not in_process:
        if dist_path == "":
            showwarning('Warning', 'Please insert Path to save files.')
        else:
            file_list = os.listdir(dist_path)
            if stemmer:
                for file in file_list:
                    if "stemmer" in file:
                        os.remove(dist_path + "/" + file)
            else:
                for file in file_list:
                    if not "stemmer" in file:
                        os.remove(dist_path + "/" + file)
            ReadFile.path = ""
            ReadFile.docNumList.clear()
            ReadFile.docCityList.clear()
            ReadFile.docLanguageList.clear()
            ReadFile.docTitleList.clear()
            ReadFile.docDateList.clear()
            ReadFile.textList.clear()
            ReadFile.textDic.clear()
            ReadFile.docDictionary.clear()
            ReadFile.length = 0
            ReadFile.fileName = ""
            ReadFile.index = 0
            ReadFile.corpus_city_dictionary.clear()
            ReadFile.world_city_dictionary.clear()
            Parse.__stop_words = ''
            Parse.__stemmer = False
            Parse.stemmer_dictionary.clear()
            corpus_path = ""
            dist_path = ""
            list_of_language.clear()
            term_dictionary.clear()
            w.Listbox1.delete(0,tk.END)
            w.Entry1.delete (0, tk.END)
            w.Entry2.delete (0, tk.END)
            showinfo('info', 'Reset completed successfully')


def showButton(p1):
    global in_process
    global in_process

    if not in_process:
        if not in_process:
            if stemmer:
                file = dist_path + "/term_dictionary_stemmer.pkl"
            else:
                file = dist_path + "/term_dictionary.pkl"
            if dist_path == "":
                showwarning('Warning', 'Please insert Path to save files.')
            elif dist_path == "" or not os.path.isfile(file):
                showwarning('Warning', 'Terms dictionary is not exists.')
            else:
                if stemmer:
                    file = open(dist_path + "/term_dictionary_stemmer.pkl", "rb+")
                else:
                    file = open(dist_path + "/term_dictionary.pkl", "rb+")
                term_dictionary_to_show = pickle.load(file)
                file.close()
                toplevel = tk.Toplevel()
                toplevel.title('Term dictionary')
                toplevel.geometry('800x400')
                scrollbar = tk.Scrollbar(toplevel)
                scrollbar.pack(side='right', fill='y')
                treeview = ttk.Treeview(toplevel, yscrollcommand = scrollbar.set, show="tree")
                treeview.pack(fill="both", expand=True)
                treeview['show'] = 'headings'
                treeview['columns'] = ('Term', 'Frequency')
                treeview.heading('Term', text='Term')
                treeview.heading('Frequency', text='Frequency')
                for term in term_dictionary_to_show:
                    treeview.insert('', 'end', text='Term', values=(str(term), str(term_dictionary_to_show[term][0])))
                treeview.pack(side='left', fill = 'both')
                scrollbar.config(command = treeview.yview())
                #treeview.configure(yscroll=scrollbar.set)

def stemCbox(p1):
    global stemmer
    global in_process
    if not in_process:
        if stemmer == True:
            stemmer = False
        else:
            stemmer = True


def uploadButton(p1):
    global term_dictionary
    global in_process

    if not in_process:
        if stemmer:
            file = dist_path + "/term_dictionary_stemmer.pkl"
        else:
            file = dist_path + "/term_dictionary.pkl"
        if dist_path == "":
            showwarning('Warning', 'Please insert Path to save files.')
        elif dist_path == "" or not os.path.isfile(file):
            showwarning('Warning', 'Terms dictionary is not exists.')
        else:
            if stemmer:
                file = open(dist_path + "/term_dictionary_stemmer.pkl", "rb+")
            else:
                file = open(dist_path + "/term_dictionary.pkl", "rb+")
            term_dictionary = pickle.load(file)
            file.close()
            fill_list()
            showinfo('info', 'Terms dictionary upload successfully')

def xxx(p1):
    s=""

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    global in_process

    if not in_process:
        top_level.destroy()
        top_level = None

if __name__ == '__main__':
    import gui
    gui.vp_start_gui()
