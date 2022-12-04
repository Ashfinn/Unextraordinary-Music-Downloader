import customtkinter
import mudopy

customtkinter.set_appearance_mode("Dark")
customtkinter.set_appearance_mode("Blue")

root = customtkinter.CTk()
root.geometry("500x300")

mudopy.Path("chromedriver/chromedriver.exe") 
mudopy.download_path(r"songs/") 


def download():
    track = entryTrack.get()
    artist = entryArtist.get()
    return mudopy.download(str(track),str(artist))

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Download Your Desired Music", font=("Roboto", 24))
label.pack(pady=12,padx=10)

description = customtkinter.CTkLabel(master=frame, text="Just write the name of the song and see the magic")
description.pack(pady=12,padx=10)

entryTrack = customtkinter.CTkEntry(master=frame, placeholder_text="Track Name")
entryTrack.pack(pady=6, padx=10)

entryArtist = customtkinter.CTkEntry(master=frame, placeholder_text="Artist Name")
entryArtist.pack(pady=6, padx=10)

button = customtkinter.CTkButton(master=frame, text="Download", command=download)
button.pack(pady=12,padx=10)

root.mainloop()