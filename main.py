from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from core.login import login
from core.remove import removeSpecialCustomers, removeEventsInShippedBeginListPage, removeEventsInShippedEndListURL
from core.refresh import refreshSodamPage

import os

class HanncareBot:
    bot_name = "haancare bot.v1"
    
    main_window_size = "300x220"
    option_window_size = "300x325"

    event_names_file_path = "./eventnames.txt"
    
    def __init__(self) -> None:

        root = Tk()
        root.title(self.bot_name)
        root.geometry(self.main_window_size)
        
        # body
        image = PhotoImage(file="thumbnail.png")
        image_label = Label(root, image=image)
        image_label.pack(fill='x')

        id_label = Label(root, text="한케어 ID")
        id_label.pack()
        self.haancare_id = Entry(root)
        self.haancare_id.pack(fill='x', pady=5, padx=10)

        id_label = Label(root, text="한케어 Password")
        id_label.pack()
        self.haancare_pw = Entry(root, show='*')
        self.haancare_pw.pack(fill='x', pady=5, padx=10)

        login_btn = Button(root, text="시작하기", command=self.clickStart)
        login_btn.pack(fill='x', padx=10, pady=5)

        option_btn = Button(root, text="옵션", command=self.clickOption)
        option_btn.pack(fill='x', padx=10, pady=5)
        
        root.mainloop()

    def clickOption(self):
        self.eventNames = []
        if (os.path.isfile(self.event_names_file_path) == False):
            with open(self.event_names_file_path, 'w', encoding='UTF-8') as event_names_file:
                pass
        else:
            with open(self.event_names_file_path, 'r', encoding='UTF-8') as event_names_file:
                raw_eventNames = event_names_file.readlines()
                for raw_eventName in raw_eventNames:
                    self.eventNames.append(raw_eventName.replace('\n', ''))
        
        self.optionRoot = Tk()
        self.optionRoot.title("Option")
        self.optionRoot.geometry(self.option_window_size)
        
        self.eventNamesLen = len(self.eventNames)
        self.listbox = Listbox(self.optionRoot)

        for eventName in self.eventNames:
            self.listbox.insert(0, eventName)
        self.listbox.pack(fill='x', padx=5, pady=5)

        description_one_label = Label(self.optionRoot, text="붙여넣기는 CTRL+V를 이용해 주세요!")
        description_one_label.pack()
        description_two_label = Label(self.optionRoot, text="작업이 완료되면 반드시 저장 버튼을 눌러주세요!")
        description_two_label.pack()

        self.new_event_name = Entry(self.optionRoot)
        self.new_event_name.pack(fill='x', padx=5, pady=5)

        add_event_name_btn = Button(self.optionRoot, text="요소 추가", command=self.clickAddEventName)
        add_event_name_btn.pack(fill='x', padx=5, pady=5)

        delete_event_name_btn = Button(self.optionRoot, text='요소 삭제', command=self.clickDeleteEventName)
        delete_event_name_btn.pack(fill='x', padx=5, pady=5)

        self.optionRoot.mainloop()

    def clickAddEventName(self):
        self.listbox.insert(self.eventNamesLen, self.new_event_name.get())
        self.listbox.yview_moveto(1.0)
        self.eventNamesLen += 1
        self.new_event_name.delete(0, 'end')
        self.refreshEventNamesTxtFile()
        
    def clickDeleteEventName(self):
        try:
            index_delete_element = self.listbox.curselection()[0]
            self.listbox.delete(index_delete_element)
            self.eventNamesLen -= 1
            self.refreshEventNamesTxtFile()
        except:
            messagebox.showerror("error", "삭제할 요소를 선택해주세요")

    def refreshEventNamesTxtFile(self):
        total_event_names = [self.listbox.get(idx) for idx in range(self.listbox.size())]
        with open(self.event_names_file_path, 'w', encoding='UTF-8') as event_names_file:
            for total_event_name in total_event_names:
                event_names_file.write(total_event_name + '\n')

    def clickStart(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        haancare_id = self.haancare_id.get()
        haancare_pw = self.haancare_pw.get()
        bLogin = False

        fileOpen = open(self.event_names_file_path, 'r', encoding='UTF-8')
        eventAmountTitles = []

        rawEventAmountTitles = fileOpen.readlines()
        for rawEventAmountTitle in rawEventAmountTitles:
            eventAmountTitles.append(rawEventAmountTitle.replace('\n', ''))

        fileOpen.close()
        
        try:
            login(self.driver, haancare_id, haancare_pw)
            bLogin = True
        except:
            messagebox.showerror("error", "로그인 실패")
            bLogin = False
        
        if bLogin:
            while(True):
                removeSpecialCustomers(self.driver)
                for eventAmountTitle in eventAmountTitles:
                    removeEventsInShippedBeginListPage(self.driver, eventAmountTitle)
                    removeEventsInShippedEndListURL(self.driver, eventAmountTitle)
                refreshSodamPage(self.driver)
        self.driver.close()

hanncareBot = HanncareBot()