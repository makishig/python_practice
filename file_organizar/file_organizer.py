import json
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil

#exeが置いてあるフォルダと現在の作業フォルダが同じとは限らない
#このexeが置かれてる場所のcategories.jsonを開く、という書き方にする
base_dir = Path(__file__).resolve().parent  #__file__は現在実行しているpythonファイルの場所　.resolveは絶対パスとして扱える形にする

with open(base_dir / "categories.json", "r", encoding="utf-8") as f:
    categories = json.load(f)
    
def organize_files(folder, categories): 
        
    move_list = []
    for file in folder.iterdir():
        
        if file.is_file():
            suffix = file.suffix.lower()
         
            for category, extensions in categories.items():
                
                if suffix in extensions:
                    
                    move_list.append((file, category))
                    
                    break
            else:
                category = 'その他'
                move_list.append((file, category))
                
    return move_list

def select_folder():
    folder = filedialog.askdirectory()
    
    if not folder:
        return
    
    folder_var.set(folder)
    move_list.clear()
    text_box.delete('1.0', tk.END)

def organize_selected_folder():
    
    global move_list
    
    if not folder_var.get():   
        messagebox.showwarning('警告', '先にフォルダを選択してください')
        return
    
    folder = Path(folder_var.get())
    move_list = organize_files(folder, categories)
    
    text_box.delete('1.0', tk.END) 
    
    if not move_list:
        text_box.insert(tk.END, 'ファイルが存在しません')
        return
    
    text_box.insert(tk.END, '===移動予定===\n\n')
    for file, category in move_list:
        text_box.insert(tk.END, f'{file.name} -> {category}\n')
    
def execute_move():
    if not move_list:
        messagebox.showinfo('確認', '移動するファイルがありません')
        return
    
    answer = messagebox.askyesno('確認', '表示されている内容でファイルを移動しますか？')
    
    if not answer:
        return
        
    for file, category in move_list:
        destination_folder = file.parent/category
        
        if not file.exists(): 
            text_box.insert(tk.END, f'ファイルが見つからないためスキップ:{file.name}\n')
            continue
        
        destination_folder.mkdir(exist_ok=True)
        
        destination = destination_folder/file.name
        if destination.exists():
            text_box.insert(tk.END, '同じ名前のファイルがあるためスキップ:', file.name, '\n')
        else:
            try:
                shutil.move(file, destination)
            except PermissionError:
                text_box.insert(tk.END, '移動できませんでした;', file.name, '\n')
    
    move_list.clear()
    messagebox.showinfo('完了', 'ファイルの整理が完了しました')
        

root = tk.Tk()

move_list =[]

root.title('ファイル整理ツール')
root.geometry('500x300')

folder_var = tk.StringVar()

label = tk.Label(root, textvariable=folder_var) 
label.pack()

select_button = tk.Button(root, text='フォルダを選択', command=select_folder)
select_button.pack()

text_box = tk.Text(root, width=70, height=15)
text_box.pack()

organize_button = tk.Button(root, text='移動予定を確認', command=organize_selected_folder)
organize_button.pack()

execute_button = tk.Button(root, text='実行', command=execute_move) #実行ボタン
execute_button.pack()

root.mainloop()