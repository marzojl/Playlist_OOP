from tkinter import filedialog, Tk
from datetime import datetime
import os


class PlaylistUtils:

    home_path = os.getenv('USERPROFILE')
    dict_filedialog = {"xlsx": '("XLSX files", "*.xlsx"), ("All files", "*.*")'}

    def __init__(self):
        self.desktop_path = self.home_path + '\\Desktop\\MCR_Programs_Output\\'

    def ask_filename(self, current_title, current_filetype):
        root = Tk()
        root.withdraw()
        current_filename = filedialog.askopenfilename(title=current_title,
                                                      filetypes=(self.dict_filedialog[current_filetype]))
        return current_filename

    def ask_filenames(self):
        pass

    def generate_header(self):
        pass

    def change_directory_desktop(self):
        pass

    def get_utc_time(self):
        pass

    def get_current_date_time(self):
        '''Generate current date and time.  Format is YYYY-MM-DD_HH-MM-SS.'''
        t = datetime.datetime.now()
        current_date = t.strftime('%Y-%m-%d_%H-%M-%S')

        return current_date

    def convert_xls_csv(self):
        pass

    def write_csv(self):
        pass
