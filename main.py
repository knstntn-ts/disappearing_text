from tkinter import *

BACKGROUND_COLOR = "#53BF9D"
DANGER_COLORS = ['#F94C66', '#BD4291', '#FFC54D', "white", "white"]
timer_id = None


def start_writing():

    def danger_counter():
        start_danger_counter()

    def start_danger_counter(counter=5):
        global timer_id

        if timer_id is not None:
            window.after_cancel(timer_id)

        if counter > 0:
            timer_id = window.after(1000, start_danger_counter, counter - 1)
            timer_display.configure(text='Danger Counter\n'+str(counter))
            input_text_field.configure(background=DANGER_COLORS[counter-1])
        else:
            input_text_field.delete('1.0', 'end')
            timer_display.configure(text="Sorry, but you waited for too long.")

    canvas.destroy()
    load_image_but.destroy()
    instruction_text_label = Label(window, text="Let your fantasy unfold in the field below",
                                   font=('Arial', 25, 'bold'), wraplength=500, pady=50, background=BACKGROUND_COLOR)
    instruction_text_label.grid(row=0, column=0, columnspan=3)
    input_text_field = Text(window, height=15, width=100)
    input_text_field.grid(row=1, column=0, columnspan=2)
    input_text_field.bind('<KeyRelease>', lambda fun: danger_counter())
    timer_display = Label(window, text='Danger Counter\n5', width=25, height=1, pady=50, wraplength=500,
                          font=('Arial', 35, 'bold'), background=BACKGROUND_COLOR)
    timer_display.grid(row=1, column=2, columnspan=1)


# ---------------------- UI SETUP --------------------#
window = Tk()
window.title('Disappearing Text')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
word_text = canvas.create_text(400, 263, text="Push yourself to write continuously!", font=('Arial', 30, 'bold'))

canvas.grid(row=0, column=0, columnspan=1)
load_image_but = Button(text='Click here to start writing', command=start_writing)
load_image_but.grid(row=1, column=0)

window.mainloop()

