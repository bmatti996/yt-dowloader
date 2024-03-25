
from cProfile import label
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

window = tk.Tk()
window.title("Youtube Downloader")
window.geometry("1280x720")
window.config(bg="#123672")

def download_video():
    if input_url.get() == "":
        print("Inserisci l'URL nell'input!")
    else:
        bottone_download.config(state=tk.DISABLED)
        input_url.config(state=tk.DISABLED)
        download_directory = filedialog.askdirectory(title="Seleziona la cartella di destinazione:")
        youtube =  YouTube(input_url.get())
        video = youtube.streams.get_highest_resolution()
        label_titolo_video = tk.Label(window, text=("Titolo: "+youtube.title), font=("Youtube Sans Medium", 13), bg="#123672", fg="orange")
        label_titolo_video.grid(row=5, column=0, pady=20)
        if youtube.description == "":
            label_descrizione_video = tk.Label(window, text=("Nessuna descirizione"), font=("Youtube Sans Medium", 13), bg="#123672", fg="orange")
        else:
            label_descrizione_video = tk.Label(window, text=("Descrizione: "+youtube.description), font=("Youtube Sans Medium", 13), bg="#123672", fg="orange")
        label_descrizione_video.grid(row=6, column=0, pady=5)
        label_durata_video = tk.Label(window, text=("Durata: "+str(youtube.length)+"secondi"), font=("Youtube Sans Medium", 13), bg="#123672", fg="orange")
        label_durata_video.grid(row=7, column=0, pady=5)
        label_visualizzazioni_video = tk.Label(window, text=("visualizzazioni: "+str(youtube.views)), font=("Youtube Sans Medium", 13), bg="#123672", fg="orange")
        label_visualizzazioni_video.grid(row=8, column=0, pady=5)
        video.download(download_directory)
        label_downloaded = tk.Label(window, text=("Video scaricato in "+download_directory+"!"), font=("Youtube Sans Medium", 22), bg="#123672", fg="yellow")
        label_downloaded.grid(row=9, column=0, pady=20)



label_title = tk.Label(window, text="Youtube Downloader", font=("Youtube-Sans-Bold", 48), bg="#123672", fg="red")
label_title.grid(row=1, column=0, pady=30, padx=370)

label_indicazione = tk.Label(window, text="Inserisci L'URL del video qua sotto:", font=("Youtube Sans Medium", 17), bg="#123672", fg="Yellow")
label_indicazione.grid(row=2, column=0)

input_url = tk.Entry(window, font=("Youtube Sans Ligth", 13), bd=3, width=100 )
input_url.grid(row=3, column=0, pady=12)

bottone_download = tk.Button(window, text="Dowload video", font=("Youtube Sans Medium", 15), bd=3, bg="#234783", width=20, command=download_video)
bottone_download.grid(row=4, column=0, pady=20)



window.mainloop()