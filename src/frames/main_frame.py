from tkinter import Tk, Canvas


def create_main_frame():
    root = Tk()
    root.geometry("800x460")
    root.configure(bg="#FFFFFF")

    canvas = Canvas(
        root,
        bg="#FFFFFF",
        height=460,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(0.0, 0.0, 800.0, 460.0, fill="#378AEC", outline="")
    root.resizable(False, False)

    return root
