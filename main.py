#coding:utf-8

from tkinter import StringVar
from numpy import var
from traitlets import default


try:
    import tkinter as tk
    import webbrowser
    import pycountry
    import sqlite3
    import numpy
    from tkinter import ttk
    from tkcalendar import DateEntry
    from tkinter import messagebox
    from tkinter import filedialog
except ImportError:
    print("Installer tout les modules requis avant de continuer")

nom = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegowina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Congo, the Democratic Republic of the", "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Holy See (Vatican City State)", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Republic of", "Korea, Republic of", "Kuwait", "Kyrgyzstan", "Lao, People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia, The Former Yugoslav Republic of", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia (Slovak Republic)", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan, Province of China", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "United States Minor Outlying Islands", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zambia", "Zimbabwe"]


def voiranime():
    webbrowser.open_new("www.voiranime.stream/anime/one-piece")



def ouvrir():
    global photoprofil
    global buttonphoto
    filename = filedialog.askopenfilename()
    photoprofil = tk.PhotoImage(file=filename).zoom(10).subsample(60)
    buttonphoto.configure(image=photoprofil)

def validerconnexion():
    """ permet de valider les identfiants de connexion de l'utilisateur"""
    var_buttonvalider.set("Connexion en cour...")
    connection = sqlite3.connect("base_de_donnee-tkinter.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tt_users WHERE user_pseudo = ?',(ent_cn1.get(),))
    password = cursor.fetchone()
    connection.close()
    
    #fichier = open("DataUsers.txt","r")
    #lecture = fichier.read()
    #verification = lecture.split()
    #fichier.close()
    if password != None:
        if ent_cn2.get() == password[7]:
            var_buttonvalider.set("Se connecter")
            #tp.destroy()
            chargement(tp)
            Main()
        else:
            var_buttonvalider.set("Se connecter")
            tk.messagebox.askretrycancel("ERREUR","Mot de passe incorrect, veuillez reessayer ")
            var_buttonvalider.set("Se connecter")
    else:
        var_buttonvalider.set("Se connecter")
        tk.messagebox.askretrycancel("ERREUR","Pseudo incorrect, veuillez reessayer ")
        var_buttonvalider.set("Se connecter")

    

def validerinscription():
    """permet de valider l'inscription de l'utilisateur"""

    connexion = sqlite3.connect("base_de_donnee-tkinter.db")
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM tt_users WHERE user_pseudo = ?",(var_entrypseudo.get(),))
    pseudo = cursor.fetchall()
    connexion.close()
    

    if (var_entrypass.get() !="" or var_entrypseudo.get() !="" or var_entryconfirm.get() !=""): 
        if var_entry1.get() != "" :
            if var_entry2.get() != "" :

                if pseudo == []:

                #elif (type(var_entry1.get()) != str or type(var_entry2.get()) != str or type(var_entrypass.get()) != str or type(var_entrypseudo.get()) != str or type(var_entryconfirm.get()) != str):
                #    tk.messagebox.showwarning("Avertissement","Utilisez uniquement des lettres l'aphabet francais")

                    if var_entrypass.get() != var_entryconfirm.get():
                        tk.messagebox.showerror("Erreur","le mot de passe confirmé est incorrect")
                    
                    elif len(var_entrypseudo.get()) < 4:
                        tk.messagebox.showinfo("Avertissement","Votre pseudo doit faire plus de 3 caracteres")
                    
                    elif len(var_entrypass.get()) < 6:
                        tk.messagebox.showinfo("Avertissement","Votre mot de passe doit faire plus de 5 caracteres")

                    else:
                        tp1.destroy()
                        try:
                            connexion = sqlite3.connect("base_de_donnee-tkinter.db", timeout=10)
                            cursor = connexion.cursor()
                            new_users = (cursor.lastrowid,var_entry1.get(),var_entry2.get(),var_checkb.get(),varcal.get(),varpays.get(),var_entrypseudo.get(),var_entrypass.get())
                            cursor.execute("INSERT INTO tt_users VALUES(?,?,?,?,?,?,?,?)", new_users)
                            connexion.commit()
                        except Exception as e:
                            print("Erreur de connexion avec la base de données :", e)
                        finally:
                            connexion.close()

                        #threading.Thread(target=tp1.destroy()).start().join()
                        tk.messagebox.showinfo("ok","Merci de vous etes inscris, maintenant vous pouvez vous connecter")
                else:
                    tk.messagebox.showinfo("Avertissement","Ce pseudo est déjà existant, veuillez en choisir en un autre")
            else:
                tk.messagebox.askretrycancel("ERREUR","Vous devez entrer votre prenom")
        else:
            tk.messagebox.askretrycancel("ERREUR","Vous devez entrer votre nom ")
    else:
        tk.messagebox.askretrycancel("Erreur","Vous devez remplir obligatoirement tout les champs")

    print("({},{},{},{},{},{},{},{})".format(var_entry1.get(),var_entry2.get(),var_checkb.get(),varcal.get(),varpays.get(),var_entrypseudo.get(),var_entrypass.get(),var_entryconfirm.get()))

def connexion():
    root.destroy()
    global tp
    tp = tk.Tk()
    tp.geometry("780x312")
    tp.title("plus qu'une etape avant de KouMan :)")
    tp.configure(bg="#74EC8D")
    tp.iconbitmap("quiz2.ico")
    img1 = tk.PhotoImage(file="sign-in.png").zoom(19).subsample(40)
    global fn5
    fn5 = tk.Frame(tp, bg="#74EC8D")
    global canvas1
    canvas1 = tk.Canvas(fn5, width=250, height=250, bg="#74EC8D", borderwidth=0, highlightthickness=0)
    canvas1.create_image(125, 125, image=img1)
    tp.minsize(width=670, height=235)
    
    global fn4
    fn4 = tk.Frame(fn5, bg="#74EC8D")
    global fn3
    fn3 = tk.Frame(fn4,border=2, bg="#74EC8D", relief="sunken")
    global fn1
    fn1 = tk.Frame(fn3, bg="#74EC8D")
    global fn2
    fn2 = tk.Frame(fn3, bg="#74EC8D")
    global fn6
    fn6 = tk.Frame(fn5, width=100, bg="#74EC8D")
    
    global ent_cn1
    global ent_cn2
    global var # juste pour pouvoir ajouter le pseudo sous la photo de profil
    var = tk.StringVar()
    ent_cn1 = tk.Entry(fn1, width=30, bg="#74EC8D",fg="black", font=("arial bold",10))
    ent_cn2 = tk.Entry(fn2, width=30, show=" ",textvariable=var, bg="#74EC8D",fg="black", font=("arial bold",10))
    
    global label_cn1
    global label_cn2
    label_cn1 = tk.Label(fn1, text="Entrer votre pseudo ", font=("verdana",10), bg="#74EC8D", fg="black")
    label_cn2 = tk.Label(fn2, text="Entrer votre mot de passe", font=("verdana",10), bg="#74EC8D", fg="black")

    global var_buttonvalider
    var_buttonvalider = tk.StringVar()
    var_buttonvalider.set("Se connecter")
    global btn_v
    btn_v = tk.Button(fn4, textvariable=var_buttonvalider, fg="black", bg="#74EC8D", font=("verdana",10),activebackground="black", bd=0.5, command=validerconnexion)

    ent_cn1.pack(side="right",fill="x")
    ent_cn2.pack(side="right", fill="x")
    label_cn1.pack(side="left", fill="x", padx=24,pady=15)
    label_cn2.pack(side="left", fill="x", ipadx=6, pady=15)
    canvas1.pack(side="left")
    fn1.pack()
    fn2.pack()
    fn3.pack(expand="yes")
    fn4.pack(side="right")
    fn5.pack(expand="yes")
    fn6.pack(expand="yes")
    btn_v.pack(fill="x", pady="20", ipady=5)
    tp.mainloop()

def chargement(widget): ####################################################
    for widgets in widget.winfo_children():
        widgets.destroy()

    varlab = tk.StringVar()
    varlab.set("En attente du chargement.")
    label = tk.Label(tp, text=varlab, fg ="red", font=("arial",15)).pack(expand ="yes")
    varlab.set("En attente du chargement..")
    varlab.set("En attente du chargement...")
    tp.destroy()



def func(event):
    """pour raccourssi clavier """
    #event.widget. ensuite on peut appeller n'importe quelle methode des widgets
    event.widget.attributes("-fullscreen", False)
    #print("Fenetre Reduit avec succès !")

def inscription():
    global tp1
    tp1 = tk.Toplevel()
    tp1.configure(background="#4AA3A2")
    tp1.iconbitmap("quiz2.ico")
    tp1.geometry("700x400")
    tp1.bind("<Escape>",func)
    #definir racourssi pour le quitter le mode plein ecran car impossible
    tp1.attributes("-fullscreen", True)

    framecenter = tk.Frame(tp1,background="#4AA3A2")

    frame11 = tk.Frame(framecenter,background="#4AA3A2")

    frame = tk.Frame(frame11,background="#4AA3A2", relief="ridge", bd=2)
    frame1 = tk.Frame(frame,background="#4AA3A2")
    frame2 = tk.Frame(frame,background="#4AA3A2")
    frame3 = tk.Frame(frame,background="#4AA3A2")
    frame4 = tk.Frame(frame,background="#4AA3A2")
    frame44 = tk.Frame(frame4,background="#4AA3A2")
    frame5 = tk.Frame(frame,background="#4AA3A2")
    frameBouton = tk.Frame(frame11)
    labelNom = tk.Label(frame1, text="Nom*", font="Times",background="#4AA3A2",foreground='black')
    label_in2 = tk.Label(frame2, text="Prenom*", font="Times",background="#4AA3A2",foreground='black')
    label_in3 = tk.Label(frame3, text="Date de naissance* ", font="Times",background="#4AA3A2",foreground='black')
    label_in4 = tk.Label(frame4, text="Sexe ", font="times",background="#4AA3A2",foreground='black')
    label_in1 = tk.Label(frame5, text="pays de residence ", font="Times",background="#4AA3A2",foreground='black')

    global var_checkb
    var_checkb = tk.StringVar()
    checkb1 = tk.Radiobutton(frame44,text = "Masculin", value="M", variable=var_checkb, font="Times",activebackground="black",background="#4AA3A2",foreground='black')
    checkb2 = tk.Radiobutton(frame44,text="Feminin", value="F", variable=var_checkb, font="Times",background="#4AA3A2",activebackground="black",foreground='black')
    global var_entry1
    global var_entry2
    var_entry1 = tk.StringVar()
    var_entry2 = tk.StringVar()
    entry1 = tk.Entry(frame1,background="#4AA3A2", relief="ridge", bd=2,foreground='black', textvariable=var_entry1)
    entry2 = tk.Entry(frame2,background="#4AA3A2", relief="ridge", bd=2,foreground='black', textvariable=var_entry2)

    frame6 = tk.Frame(frame,background="#4AA3A2")
    pseudo = tk.Label(frame6, text="Entrer votre pseudo*", font="Times",background="#4AA3A2",foreground='black')
    global var_entrypseudo
    var_entrypseudo = tk.StringVar()
    entrypseudo = tk.Entry(frame6,background="#4AA3A2", relief="ridge", bd=2,foreground='black', textvariable=var_entrypseudo)

    frame7 = tk.Frame(frame,background="#4AA3A2")
    password = tk.Label(frame7, text="Entrer votre mot de passe*", font="Times",background="#4AA3A2",foreground='black')
    global var_entrypass
    var_entrypass = tk.StringVar()
    entrypass = tk.Entry(frame7,background="#4AA3A2", relief="ridge", bd=2,foreground='black',show="*", textvariable=var_entrypass)

    frame8 = tk.Frame(frame,background="#4AA3A2")
    confirmpassword = tk.Label(frame8, text="Confirmer votre mot de passe*", font="Times",background="#4AA3A2",foreground='black')
    global var_entryconfirm
    var_entryconfirm = tk.StringVar()
    entryconfirm = tk.Entry(frame8,background="#4AA3A2", relief="ridge", bd=2,foreground='black',show=" ", textvariable=var_entryconfirm)

    bouton = tk.Button(frameBouton, text="S'inscrire", font="times",foreground='black', background='#4AA3A2', relief="ridge", command=validerinscription)

    # autre methode pour afficher une image dans tkinter sans Canvas
    imageinscription = tk.Label(framecenter,background="#4AA3A2")
    imageinscription.image = tk.PhotoImage(file="inscription.png")
    imageinscription["image"] = imageinscription.image
    
    labelNom.pack(side="left", ipadx=5)
    entry1.pack(ipadx=10,padx=30)
    label_in2.pack(side="left", ipadx=10)
    entry2.pack(side="right", ipadx=10,padx=30)
    label_in3.pack(side="left", ipadx=10)
    label_in3.pack(side="left", ipadx=10)
    label_in4.pack(side="left", ipadx=10)
    label_in1.pack(side="left", ipadx=10)
    checkb1.pack(side="left")
    checkb2.pack(ipadx=10)
    pseudo.pack(side="left")
    entrypseudo.pack(padx=30)
    password.pack(side="left")
    entrypass.pack(padx=30)
    confirmpassword.pack(side="left")
    entryconfirm.pack(padx=30) 
    frame1.pack(pady=20)
    frame2.pack()
    frame3.pack(pady=15)
    frame4.pack()
    frame44.pack(pady=30)
    frame5.pack()
    frame6.pack(pady=30)
    frame7.pack()
    frame8.pack(pady=30)
    frame11.pack(side="left")
    framecenter.pack(expand="yes")
    imageinscription.pack(side="right", padx=15)
    frame.pack(side="top")
    frameBouton.pack(side="bottom", fill="x", pady=15)
    bouton.pack(fill="x")

    global varcal
    varcal = tk.StringVar(value="Choisir")
    global cal
    cal = DateEntry(frame3, width=12,textvariable=varcal, background='#4AA3A2',foreground='black', borderwidth=2, font="times")
    cal.pack()

    global varpays
    varpays = tk.StringVar(value="Choisir")
    listpays = tk.Spinbox(frame5, textvariable= varpays, values=nom,exportselection=False, font="times",foreground='black', background='#4AA3A2', relief="ridge")
    listpays.pack(padx=30)
    
class Admin(tk.Tk):
    #tk.Tk.__init__(self)
    pass






class Main():
    """contient les elements de la page d'acceuil"""
    def ouvrir(self):
        """permet de demander a l'utilisateur de choisir une photo de profil"""
        #global photo
        #global buttonphoto
        self.filename = filedialog.askopenfilename(parent=self.mainwin, title="Choisir une photo en png")
        self.photo = tk.PhotoImage(file=self.filename).zoom(10).subsample(60)
        self.buttonphoto.configure(image=self.photo)


    def __init__(self):
        """pour la fenetre principale"""
        #global mainframe
        self.mainwin = tk.Tk()
        self.mainwin.title("")
        self.x = int(self.mainwin.winfo_screenwidth())
        self.y = int(self.mainwin.winfo_screenheight())
        #self.geo = "{}x{}".format(self.x,self.y)
        self.mainwin.geometry("980x480")
        self.mainwin.attributes("-fullscreen",True)
        self.mainwin.bind("<Escape>",func)
        self.mainwin.config(bg="#342628")
        self.frame_one = tk.Frame(self.mainwin, bg="#342628",bd=1, relief="raised")
        self.frame_two = tk.Frame(self.mainwin,bd=0, relief="sunken", bg="#342628")
        self.frame_three = tk.Frame(self.mainwin,bd=0, relief="sunken",bg="#342628")
        self.var_question = tk.StringVar()
        self.var_question.set("Quelle est la capitale de la cote d'ivoire ? ")
        self.question = tk.Label(self.frame_two, textvariable=self.var_question, font=("TkHeadingFont",20), bg="#342628", fg="white").pack(side="top", pady=40)

        self.varanswer = tk.IntVar()
        self.varanswerone = tk.StringVar()
        self.varanswerone.set("Bouaké")
        self.varanswertwo = tk.StringVar()
        self.varanswertwo.set("Yamoussoukro")
        self.varanswerthree = tk.StringVar()
        self.varanswerthree.set("Casablanca")
        self.varanswerfour = tk.StringVar()
        self.varanswerfour.set("korogho")
        self.answerone = tk.Radiobutton(self.frame_two,textvariable=self.varanswerone,variable=self.varanswer,value=2, selectcolor='navy', font=("TkMenuFont",15), bg="#342628", fg="white").pack(pady=15)
        self.answertwo = tk.Radiobutton(self.frame_two,textvariable=self.varanswertwo, variable=self.varanswer,value=3, selectcolor='navy', font=("TkIconFont",15), bg="#342628", fg="white").pack()
        self.answerthree = tk.Radiobutton(self.frame_two,textvariable=self.varanswerthree, variable=self.varanswer,value=4, selectcolor='navy', font=("TkCaptionFont",15), bg="#342628", fg="white").pack(pady=15)
        self.answerfour = tk.Radiobutton(self.frame_two,textvariable=self.varanswerfour, variable=self.varanswer,value=5, selectcolor='navy', font=("TktextFont",15), bg="#342628", fg="white").pack()

        self.suivantbutton = tk.Button(self.frame_three, text="Suivant",default="disabled", font=("calibri",20), bg="green",fg="black", command=self.setContent)
        #self.pseudo = ent_cn1.get()
        connexion = sqlite3.connect("base_de_donnee-tkinter.db")
        cursor = connexion.cursor()
        reponse = cursor.execute("SELECT user_pseudo FROM tt_users WHERE user_password = ?",(var.get(),))
        result = cursor.fetchone()
        connexion.close()

        self.varlabel = tk.StringVar()
        self.varlabel.set(result)
        self.label = tk.Label(self.frame_one, textvariable=self.varlabel, fg="white", bg="#342628", font=("verdana",30))

        self.photo = tk.PhotoImage(file="user.png").zoom(20).subsample(50)
        self.buttonphoto = tk.Button(self.frame_one, image=self.photo, bg="#342628", relief="flat", command=self.ouvrir, width=250, height=200)
        
        self.varniveaux = tk.IntVar()
        self.varniveaux.set("0")
        self.niveauxlabel = tk.Label(self.frame_one, textvariable=self.varniveaux, bg="#342628", font=("verdana",150), fg="white")

        self.frame_one.pack(side ="left", padx=0, fill="y")
        self.frame_two.pack(side="top",expand="yes", padx=30)
        self.frame_three.pack(side="right", expand="yes")
        self.suivantbutton.pack(side="bottom", fill="x", pady=30)
        self.buttonphoto.pack()
        self.label.pack()
        self.niveauxlabel.pack(side= "bottom", ipady=20)
        
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        self.bonne_reponse = 0
        self.mauvaise_reponse = -1


        self.mainwin.mainloop()
    
    def setContent(self):

        if self.varanswer.get():
            self.suivantbutton.config(default="normal")

        self.id = numpy.random.randint(1,4)

        connexion = sqlite3.connect("base_de_donnee-tkinter.db")
        cursor = connexion.cursor()
        reponse = cursor.execute("SELECT * FROM tt_questions WHERE id = ?",(self.id,))
        global result
        result = reponse.fetchall()
        connexion.close()
        self.var_question.set(result[0][1])
        self.varanswerone.set(result[0][2])
        self.varanswertwo.set(result[0][3])
        self.varanswerthree.set(result[0][4])
        self.varanswerfour.set(result[0][5])


        if int(self.varanswer.get()) == int(result[0][6]):
            self.bonne_reponse += 1
            #return True
        else:
            self.mauvaise_reponse += 1
            #return False
        

        # en gros le good answer id change de valeur dans la base de donée, meme moi je comprend pas 
        print("nombre aleatoire : ",self.id)
        print("Reponse joueur : ",self.varanswer.get())
        print("Good_answer_id : ",result[0][6])
        print("Bonne reponse : ",self.bonne_reponse)
        print("Mauvaise reponse : ",self.mauvaise_reponse)
        print("--------------------")

        if self.mauvaise_reponse == 3:
            self.suivantbutton.config(default="disabled")


            self.score = self.bonne_reponse + self.mauvaise_reponse
            self.frame = tk.Tk()
            self.frame.title("Fin de la partie !")

            self.label = tk.Label(self.frame, text="Score final : " + str(self.bonne_reponse) + "/" + str(self.score)).pack()
            return self.frame
    

        


root = tk.Tk()
screen_X = int(root.winfo_screenwidth()) #recuperer la largeur de mon ecran
screen_Y = int(root.winfo_screenheight()) #hauteur
fenetre_X = 500
fenetre_Y = 400

posX = (screen_X // 2) - (fenetre_X // 2)
posY = (screen_Y // 2) - (fenetre_Y // 2)

geo = "{}x{}+{}+{}".format(fenetre_X,fenetre_Y,posX,posY)

root.geometry(geo)
#root.eval("tk::PlaceWindow . center")

root.title("JOUER et GAGNER des RECOMPENSES")
root.configure(bg="#333533")
root.iconbitmap("logo.ico")
fn = tk.Frame(root,bg="#333533")
#creation image
image = tk.PhotoImage(file="quiz2.png").zoom(4).subsample(10)
canvas = tk.Canvas(fn, width=250, height=250, bg="#333533", borderwidth=0, highlightthickness=0)
canvas.create_image(125, 125, image=image)

canvas.pack()

btn_1 = tk.Button(fn, text="Connexion", font=("courrier",10), width=15, height=3,activebackground="black", background="#74EC8D",fg="black", command=connexion)
btn_2 = tk.Button(fn, text="Inscription", font=("courrier",10), width=15, height=3,activebackground="black", background="#4AA3A2", fg="black", command=inscription)

btn_1.pack(side="left", pady=15) # grace a expand il sera toujours au centre
btn_2.pack(side="right", pady=15)

fn.pack(expand="yes") # on peut aussi utiliser fn.place(relx=0.5, rely=0.5, anchor="center")
#fn.configure(bg="black")

root.mainloop()