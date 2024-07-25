import customtkinter as ctk

def button_call():
    print("button pressed")

app = ctk.CTk()
app.title("my app")
app.geometry("400x150")

button = ctk.CTkButton(app,text = "click me", command = button_call,corner_radius = 32, hover_color ="#FFA500",border_color = "#FFD280")
button.grid(row = 0, column=0, padx = 20, pady = 20 )

app.mainloop()
