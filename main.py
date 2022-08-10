from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
root = Tk()

# OPEN WORDS FILE ##############################

words = []
fName = open("mywords.txt")
for line in fName:
    line = line.strip('\n')
    words.append(line)
fName.close()

print(words)
index = random.randint(0, len(words) - 1)
print(len(words) - 1)
print(index, " ", words[index])

string_to_guess = words[index]
string_tmp = ""
string_to_guess_blank = ""
for l in string_to_guess:
    string_to_guess_blank = string_to_guess_blank + "_ "
    string_tmp = string_tmp + "_"
print(string_to_guess_blank)


##########################################################

# Get hangman image ######################################

image1 = Image.open('images/4.jpg')
image2 = Image.open('images/5.jpg')
image3 = Image.open('images/6.jpg')
image4 = Image.open('images/7.jpg')
image5 = Image.open('images/8.jpg')
image6 = Image.open('images/9.jpg')
image7 = Image.open('images/10.jpg')
#image8 = Image.open('images/11.jpg')

img = [image1, image2, image3, image4, image5, image6, image7]


# Resize the image in the given (width, height)
# #img = image.resize((450, 450))

# Convert the image in TkImage
pos = 0
my_img1 = ImageTk.PhotoImage(img[0])
##########################################################

frame = LabelFrame(root, text="Hangman", padx=20, pady=20)
frame.grid(row=0, column=0, padx=10, pady=10)

frame2 = LabelFrame(root, text="Buttons", padx=20, pady=20)
frame2.grid(row=1, column=0, padx=10, pady=10)

myLabel = Label(frame, image=my_img1)
myLabel.grid(row=0, column=0)
wordLabel = Label(frame, text=string_to_guess_blank, font=("monospace", 18))
wordLabel.grid(row=0, column=1, padx=30)


def containsLetter(mystring, aletter):
    return aletter in mystring


def mytext(btext):
    global string_to_guess
    global string_to_guess_blank
    global string_tmp
    global wordLabel
    global pos
    global myLabel
    global my_img1
    btext['state'] = DISABLED
    letter = btext['text']
    letter = letter.lower()
    print(btext['text'])
    print(letter)
    btext['bg'] = "red"

    #mylist = list(string_to_guess_blank)
    #print(mylist)
    string_list = list(string_to_guess_blank)
    #print(string_list)
    count = 0
    failed = 1
    for l in string_to_guess:

        if l == letter:
            btext['bg'] = "green"
            string_list[count*2] = l
            failed = 0
        count = count + 1
    string_to_guess_blank = ""
    string_to_guess_blank = string_to_guess_blank.join(string_list)
    wordLabel.destroy()
    wordLabel = Label(frame, text=string_to_guess_blank, font=("monospace", 18))
    wordLabel.grid(row=0, column=1, padx=30)
    if containsLetter(string_to_guess_blank, "_") == FALSE:
        messagebox.showwarning('YOU WON', 'Winning')
        quit()

    if failed == 1:
        myLabel.destroy()
        pos = pos + 1
        my_img1 = ImageTk.PhotoImage(img[pos])
        myLabel = Label(frame, image=my_img1)
        myLabel.grid(row=0, column=0)
        if pos == 6:
            messagebox.showwarning('DEATH', 'You died!')
            quit()


button_a = Button(frame2, text="A", command=lambda: mytext(button_a))
button_b = Button(frame2, text="B", command=lambda: mytext(button_b))
button_c = Button(frame2, text="C", command=lambda: mytext(button_c))
button_d = Button(frame2, text="D", command=lambda: mytext(button_d))
button_e = Button(frame2, text="E", command=lambda: mytext(button_e))
button_f = Button(frame2, text="F", command=lambda: mytext(button_f))
button_g = Button(frame2, text="G", command=lambda: mytext(button_g))
button_h = Button(frame2, text="H", command=lambda: mytext(button_h))
button_i = Button(frame2, text="I", command=lambda: mytext(button_i))
button_j = Button(frame2, text="J", command=lambda: mytext(button_j))
button_k = Button(frame2, text="K", command=lambda: mytext(button_k))
button_l = Button(frame2, text="L", command=lambda: mytext(button_l))
button_m = Button(frame2, text="M", command=lambda: mytext(button_m))
button_n = Button(frame2, text="N", command=lambda: mytext(button_n))
button_o = Button(frame2, text="O", command=lambda: mytext(button_o))
button_p = Button(frame2, text="P", command=lambda: mytext(button_p))
button_q = Button(frame2, text="Q", command=lambda: mytext(button_q))
button_r = Button(frame2, text="R", command=lambda: mytext(button_r))
button_s = Button(frame2, text="S", command=lambda: mytext(button_s))
button_t = Button(frame2, text="T", command=lambda: mytext(button_t))
button_u = Button(frame2, text="U", command=lambda: mytext(button_u))
button_v = Button(frame2, text="V", command=lambda: mytext(button_v))
button_w = Button(frame2, text="W", command=lambda: mytext(button_w))
button_x = Button(frame2, text="X", command=lambda: mytext(button_x))
button_y = Button(frame2, text="Y", command=lambda: mytext(button_y))
button_z = Button(frame2, text="Z", command=lambda: mytext(button_z))


button_a.grid(row=1, column=0)
button_b.grid(row=1, column=1)
button_c.grid(row=1, column=2)
button_d.grid(row=1, column=3)
button_e.grid(row=1, column=4)
button_f.grid(row=1, column=5)
button_g.grid(row=1, column=6)
button_h.grid(row=1, column=7)
button_i.grid(row=1, column=8)
button_j.grid(row=1, column=9)
button_k.grid(row=1, column=10)
button_l.grid(row=1, column=11)
button_m.grid(row=1, column=12)
button_n.grid(row=2, column=0)
button_o.grid(row=2, column=1)
button_p.grid(row=2, column=2)
button_q.grid(row=2, column=3)
button_r.grid(row=2, column=4)
button_s.grid(row=2, column=5)
button_t.grid(row=2, column=6)
button_u.grid(row=2, column=7)
button_v.grid(row=2, column=8)
button_w.grid(row=2, column=9)
button_x.grid(row=2, column=10)
button_y.grid(row=2, column=11)
button_z.grid(row=2, column=12)






root.mainloop()