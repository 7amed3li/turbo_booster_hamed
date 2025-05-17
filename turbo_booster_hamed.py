
from tkinter import Tk, Button, Label, messagebox, StringVar, OptionMenu
import os
import subprocess
import threading

language = "Arabic"

labels = {
    "Arabic": {
        "title": "Turbo Booster by Hamed",
        "start": "🚀 ابدأ التنظيف",
        "working": "⏳ جاري التنظيف والفحص... انتظر لحظات",
        "done": "✅ تم التنظيف بنجاح! الجهاز جاهز 🚀",
        "restart_msg": "هل ترغب في إعادة تشغيل الجهاز الآن؟",
        "later": "تمام! هنفكرك لاحقًا 😉",
        "shutdown_option": "هل ترغب في إيقاف تشغيل الجهاز؟"
    },
    "English": {
        "title": "Turbo Booster by Hamed",
        "start": "🚀 Start Cleaning",
        "working": "⏳ Cleaning and scanning... Please wait",
        "done": "✅ Cleaning complete! Your system is ready 🚀",
        "restart_msg": "Would you like to restart your computer now?",
        "later": "Okay! I'll remind you later 😉",
        "shutdown_option": "Would you like to shut down your computer?"
    },
    "Turkish": {
        "title": "Turbo Booster by Hamed",
        "start": "🚀 Temizlemeye Başla",
        "working": "⏳ Temizleniyor ve taranıyor... Lütfen bekleyin",
        "done": "✅ Temizlik tamamlandı! Sistem hazır 🚀",
        "restart_msg": "Bilgisayarınızı şimdi yeniden başlatmak ister misiniz?",
        "later": "Tamam! Daha sonra hatırlatırım 😉",
        "shutdown_option": "Bilgisayarı kapatmak ister misiniz?"
    }
}

def translate(key):
    return labels[language][key]

def clean_temp_files():
    os.system('del /s /f /q "%TEMP%\*"')
    os.system('rd /s /q "%TEMP%"')
    os.system('del /s /f /q "C:\\Windows\\Temp\\*"')
    os.system('rd /s /q "C:\\Windows\\Temp"')
    os.system('del /s /f /q "C:\\Windows\\Prefetch\\*"')
    os.system('PowerShell -NoProfile -Command "Clear-RecycleBin -Force"')

def run_system_scan():
    subprocess.call('sfc /scannow', shell=True)
    subprocess.call('DISM /Online /Cleanup-Image /RestoreHealth', shell=True)

def free_memory():
    os.system('%windir%\\system32\\rundll32.exe advapi32.dll,ProcessIdleTasks')

def boost_system():
    label.config(text=translate("working"))
    threading.Thread(target=execute_boost).start()

def execute_boost():
    clean_temp_files()
    free_memory()
    run_system_scan()
    label.config(text=translate("done"))
    ask_restart()

def ask_restart():
    response = messagebox.askyesnocancel(translate("title"), translate("restart_msg"))
    if response:
        os.system("shutdown /r /t 5")
    elif response is None:
        response2 = messagebox.askyesno(translate("title"), translate("shutdown_option"))
        if response2:
            os.system("shutdown /s /t 5")
        else:
            messagebox.showinfo(translate("title"), translate("later"))

def change_language(value):
    global language
    language = value
    app.title(translate("title"))
    label.config(text=translate("start"))
    start_button.config(text=translate("start"))

app = Tk()
language = "Arabic"
app.title(translate("title"))
app.geometry("460x260")

label = Label(app, text=translate("start"), font=("Arial", 12))
label.pack(pady=20)

start_button = Button(app, text=translate("start"), font=("Arial", 14), bg="green", fg="white", command=boost_system)
start_button.pack(pady=10)

lang_var = StringVar(app)
lang_var.set("Arabic")
lang_menu = OptionMenu(app, lang_var, *labels.keys(), command=change_language)
lang_menu.pack(pady=10)

app.mainloop()
