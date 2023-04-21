<<<<<<< HEAD
import os
import tkinter as tk
from tkinter import messagebox
from rdkit import Chem
from selenium import webdriver
import pandas as pd
=======
#!/bin/env python3

import pandas as pd
import tkinter as tk
import classes as cl
import threading
>>>>>>> origin/main
import time

def get_adme_data(smiles: str) -> pd.DataFrame:
    # SwissADMEからADMEデータを取得する
<<<<<<< HEAD
    # 1.5分待機する
    time.sleep(90)
    # ランダムにプロキシを選択する
    proxies = [ 
         { 'http' : '43.157.66.170:8080' }
        ,{ 'http' : '139.162.78.109:8080' }
        ,{ 'https' : '43.153.222.203:8080' }
        ,{ 'https' : '43.138.216.160:8080' }
        ,{ 'https' : '43.135.182.214:8080' }	

    ]
    proxy = random.choice(proxies)
    # プロキシを使用してSwissADMEにアクセスする
    r = requests.get('http://www.swissadme.ch/', params={'proxy': proxy, 'SMILES': smiles})
    # 結果を取得するまで30秒待機
    time.sleep(30)
adme_data ='SwissADME.csv'
return adme_data
=======
    adme = cl.SwissADME(smiles)
    return adme.get()

def get_ic50_data(adme_data: pd.DataFrame) -> dict[str, str]:
    # 各モノアミン受容体への半数阻害効果濃度を取得する
    IC50_data = {}
    IC50_data['DAT'] = adme_data.loc[adme_data['Target'] == 'DAT', 'Ki (nM)'].iloc[0]
    IC50_data['NAT'] = adme_data.loc[adme_data['Target'] == 'NET', 'Ki (nM)'].iloc[0]
    IC50_data['SERT'] = adme_data.loc[adme_data['Target'] == 'SERT', 'Ki (nM)'].iloc[0]
    return IC50_data
>>>>>>> origin/main

def get_ec50_data(adme_data: pd.DataFrame) -> dict[str, str]:
    # 各モノアミン受容体への半数効果濃度を取得する
    ec50_data = {}
    ec50_data['DAT'] = adme_data.loc[adme_data['Target'] == 'DAT', 'EC50 (nM)'].iloc[0]
    ec50_data['NAT'] = adme_data.loc[adme_data['Target'] == 'NET', 'EC50 (nM)'].iloc[0]
    ec50_data['SERT'] = adme_data.loc[adme_data['Target'] == 'SERT', 'EC50 (nM)'].iloc[0]
    return ec50_data

def button_click() -> None:
    # ボタンを無効化
    button.configure(state="disabled")

    # メイン処理
    thread = threading.Thread(target=execute_on_click)
    thread.start()

def execute_on_click() -> None:
    # ボタンの表示の切り替え
    button.configure(text="processing...")

    # IUPAC->SMILES->ADME Data
    iupac: str = iupac_entry.get()
    smiles: str = cl.SubstanceName(iupac=iupac).get()
    adme_data: pd.DataFrame = get_adme_data(smiles)

    # ki_data = get_ic50_data(adme_data)
    # ec50_data = get_ec50_data(adme_data)

    # 結果の表示
    result_text.configure(state='normal')
    result_text.delete(1.0, tk.END)
<<<<<<< HEAD
    result_text.insert(tk.END, {SMILES: {smiles} \Ki:\DAT: {ki_data["DAT"]}\NAT: {ki_data["NAT"]}\SERT: {ki_data["SERT"]}\EC50:\DAT: {ec50_data["DAT"]}\NAT: {ec50_data["NAT"]}\S\NAT: {ki_data["NAT"]}\SERT: {ki_data["SERT"]}EC50:DAT: {ec50_data["DAT"]NAT: {ec50_data["NAT"]}S_data["NAT"]}SERT: {ki_data["SERT"]}EC50:DAT: {ec50_data["DAT"]}NAT: {ec50_data["NAT"]}S
=======
    # result_text.insert(tk.END, f'SMILES: {smiles}\n\nDAT:\n  Ki: {ki_data["DAT"]} nM\n  EC50: {ec50_data["DAT"]} nM\n\nNAT:\n  Ki: {ki_data["NAT"]} nM\n  EC50: {ec50_data["NAT"]} nM\n\nSERT:\n  Ki: {ki_data["SERT"]} nM\n  EC50: {ec50_data["SERT"]} nM')
    text: str = ""
    for _, item in adme_data.iterrows():
        text = str(item)
    result_text.insert(tk.END, text)
    result_text.configure(state='disabled')

    # CSV出力
    # adme_data.to_csv("adme.csv", encoding="utf_8_sig")

    # ボタンを有効化する
    thread = threading.Thread(target=activate_button, args=[10])
    thread.start()

def activate_button(dulation: int) -> None:
    # dulationで指定された秒数でボタンを有効化する
    for i in range(dulation, 0, -1):
        button.configure(text=f"{i}")
        time.sleep(1)

    button.configure(text="Get ADME Data")
    button.configure(state="normal")

# GUIアプリケーションのウィンドウを作成する
root = tk.Tk()
root.title('ADME Data')

# IUPAC名を入力するためのテキストボックスを作成し、ウィンドウ上に配置する
iupac_entry = tk.Entry(root, width=40)
iupac_entry.pack(pady=10)

# ボタンを作成し、ウィンドウ上に配置する
button = tk.Button(root, text='Get ADME Data', command=button_click)
button.pack(pady=10)

# 結果を表示するためのテキストボックスを作成し、ウィンドウ上に配置する
result_text = tk.Text(root, width=80, height=20, state='disabled')
result_text.pack(pady=10)

# GUIアプリケーションを実行する
root.mainloop()
>>>>>>> origin/main
