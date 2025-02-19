import FreeSimpleGUI as gui

label1 = gui.Text('Select file to compress')
input1 = gui.Input()
choose_button1 = gui.FileBrowse("Choose", key="files")

label2 = gui.Text('Select destionation folder')
input2 = gui.Input()
choose_button2 = gui.FolderBrowse("Choose", key="folder")

compress_button = gui.Button('Compress')

window = gui.Window('File Compressor',
                    layout=[[label1, input1, choose_button1],
                                               [label2, input2, choose_button2],
                                               [compress_button]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    break

window.read()
window.close()