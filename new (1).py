# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:43:56 2020

@author: Krishna Madhuri
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:36:34 2020

@author: Krishna Madhuri
"""

import nltk.classify.util
nltk.download('movie_reviews')
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
def extract_features(word_list):
    return dict([(word, True) for word in word_list])
if __name__=='__main__':                                                             #taking movie review dataset as input
                                                                            #to train the nltk against.
    positive_fileids = movie_reviews.fileids('pos')
    negative_fileids = movie_reviews.fileids('neg')

features_positive = [(extract_features(movie_reviews.words(fileids=[f])),
           'Positive') for f in positive_fileids]
features_negative = [(extract_features(movie_reviews.words(fileids=[f])),
           'Negative') for f in negative_fileids]
threshold_factor = 0.8
threshold_positive = int(threshold_factor * len(features_positive))
threshold_negative = int(threshold_factor * len(features_negative))
features_train = features_positive[:threshold_positive] + features_negative[:threshold_negative]
features_test = features_positive[threshold_positive:] + features_negative[threshold_negative:]

classifier = NaiveBayesClassifier.train(features_train)       #initializing bayes theorem to train against.then comparing
#The final function to be incorporated as required


from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import pickle


#*************************GLOBAL VARIABLES*****************************************************************


global user_list
user_list=[]
global user_count
user_count=0
global total_posts
total_posts=[]
global post_count
post_count=0
global post_content
post_content=""
global name_per
name_per=""
global current_user
current_user=0
global var1
var1=0
global var2
var2=0
global var3
var3=0
global var4
var4=0
global var5
var5=0
global var6
var6=0
global var7
var7=0
global var8
var8=0
global var9
var9=0
global var10
var10=0
global sorted_array
sorted_array=[]
global newuserlist
newuserlist=[]


#User class contains the login and sign up part
class User:
    def __init__(self):
        self.username=""
        self.id=0
        self.password=""
        self.confpass=""

user_list=[User() for i in range(15)]


#Post class contains all the parameters of the post as well as the content that will go into it.
#It has options to actually login/sign up.
#It will be used to create as well as calculate the overall score of the post
class Post():

    def __init__(self):
        self.name=""
        self.content=""
        self.score=0.0
        self.likes=[0]*5
        self.id=0
        self.categ_score=0


    def likes_dislikes(self):
        count=0
        print(self.likes)
        for i in self.likes:
            if self.likes[i]!=0:
                count=count+1
        like_val= (count/len(self.likes))*10
        return like_val

    def pos_neg(self, input_string):
        input_review=list(input_string.split(' '))
        for review in input_string:
            probdist = classifier.prob_classify(extract_features(review))
            pred_sentiment = probdist.max()
        probab = round(probdist.prob(pred_sentiment), 2)
        print(probab, "aaaaaaaaaaaaaaaaaaaaaaaaa")
        return probab


    def category(self):

        global sum
        global var1,var2,var3,var4,var5,var6,var7,var8,var9,var10


        sum=IntVar()
        sum.set(var1.get()+var2.get()+var3.get()+var4.get()+var5.get()+var6.get()+var7.get()+var8.get()+var9.get()+var10.get())
    #    sum=var1.get()+var2.get()+var3.get()+var4.get()+var5.get()+var6.get()+var7.get()+var8.get()+var9.get()+var10.get()
        print(sum.get())
        category_val=(sum.get()/55)*10
        print(category_val)
        self.categ_score=category_val
        return category_val

    def category_score(self):

        return self.categ_score

    def compute_score(self):
            #k = int(predictors(self.content)
            self.score= 0.45 * self.category_score() + 0.15 * self.likes_dislikes() + 0.40 * self.pos_neg(self.content)
            return self.score


total_posts=[Post() for i in range(5)]
'''total_posts[0].name= "Meghana"
total_posts[0].content="The mess food is unhygenic"
total_posts[0].likes=[0,0,1,0,0]
total_posts[0].id=100
total_posts[1].name= "Krishna"
total_posts[1].content="Too much academic stress"
total_posts[1].likes=[0,0,1,1,1]
total_posts[1].id=101'''

#***********************************MAIN WINDOW************************************************************

root=Tk()
root.configure(bg="#FFFFFF")
root.geometry("1920x1080")
root.title("Main Page")

#backgroung_image=ImageTk.PhotoImage(Image.open("lognbg.png"))
#bg_lg=Label(root,image=backgroung_image)
#bg_lg.place(x="0",y="0",relwidth="1", relheight="1")


#*******************************LIKED A POST***************************************************88

def liked_post(postid):

    global sorted_array
    for p in range(len(sorted_array)):
        if sorted_array[p].id == postid:
            q=p
    if sorted_array[q].likes[current_user] == 0:
        sorted_array[q].likes[current_user]=1
        print(sorted_array[q].name, sorted_array[q].likes)


#****************************FUNCTION TO GENERATE FINAL FEED********************************

def generate_feed():

    feed=Toplevel()
    feed.configure(bg="#a6ed8e")
    feed.geometry("1920x1080")
    feed.title("Feed")

    global a
    a=0

    def display_post(postname,postcontent,postid):

        global a
        a=0
        feed_frame=LabelFrame(feed,height="70", width="500")
        #feed_frame.resizable(width="False", height="False")
        feed_frame.pack(padx="10",pady="10")

        display_name=Label(feed_frame,text=postname,font="Oxygen 14")
        display_name.grid(row=a,column="0",columnspan="2")
        a=a+1
        display_content=Label(feed_frame,text=postcontent,font="Oxygen 14")
        display_content.grid(row=a,column="0",columnspan="2")
        a=a+1
        like_btn=Button(feed_frame,text="Like",command=lambda: liked_post(postid), bg="#0057E7", width="5", height="1",fg="#FFFFFF")
        like_btn.grid(row=a,column="0",pady=(3,3),padx=(0,5))
        dislike_btn=Button(feed_frame,text="Dislike", bg="#0057E7",width="5", height="1",fg="#FFFFFF")
        dislike_btn.grid(row=a,column="1",pady=(3,3))
        a=a+1
        feed_frame.pack_propagate(0)

#    for m in range(post_count):
#        print(total_posts[m].compute_score())



    for i in range(len(sorted_array)-1):
        for j in range(len(sorted_array)-i-1):
            if(sorted_array[j].compute_score()<sorted_array[j+1].compute_score()):
                t=sorted_array[j+1]
                sorted_array[j+1]=sorted_array[j]
                sorted_array[j]=t

#    for n in range(post_count):
#        print(sorted_array[n].compute_score())


    for k in range(len(sorted_array)):
        #print(sorted_array[k].name)
        display_post(sorted_array[k].name,sorted_array[k].content,sorted_array[k].id)

    refresh_btn=Button(feed,text="Refresh", command= generate_feed,bg="#008744",padx="50",pady="5")
    refresh_btn.pack()


#*****************************FUNCTION COMBINE\MERGE OF FUNCTIONS WHILE CREATING POST**************************************************
def makearray():
    global sorted_array
    global post_count
    sorted_array=[]
    f2=open("PostFile.txt","rb")

    while 1:
        try:
            o = pickle.load(f2)
        except EOFError:
            break
        sorted_array.append(o)

    post_count= post_count+1
    #print(post_count)
    generate_feed()

def combinefunc():

    global post_content
    global name_per
    global post_count

    total_posts[post_count].category()
    total_posts[post_count].name=name_per.get("1.0", END)
    total_posts[post_count].id=total_posts[post_count].name[0:4]
    total_posts[post_count].content= post_content.get("1.0", END)
    print(total_posts[post_count].name)
    print(total_posts[post_count].content)

    f1=open("PostFile.txt","ab")
    pickle.dump(total_posts[post_count],f1)
    f1.close()

    makearray()

#*********************************CREATE POST FUNCTION***************************************************


def create_post():

    post_window=Toplevel()
    post_window.configure(bg="#a6ed8e")
    post_window.geometry("1920x1080")
    post_window.title("Create A Post!")

    label_name=Label(post_window, text="Name:",bg="#a6ed8e",font="Oxygen 20" )
    label_name.grid(row="0",column="0", padx=(400,10), pady=(100,20))
    global name_per
    name_per=Text(post_window, height="1", width="30",font = "Calibri 18")
    name_per.grid(row="0", column="1", pady=(100,20))
    global post_content
    label_content=Label(post_window, text="Content:",bg="#a6ed8e",font="Oxygen 20" )
    label_content.grid(row="1",column="0", padx=(400,10), pady=(0,20))
    post_content=Text(post_window, height="5", width="30",font = "Calibri 18")
    post_content.grid(row="1", column="1",pady=(0,10))

    global var1
    var1=IntVar()
    c1= ttk.Checkbutton(post_window,text="Security", variable=var1, onvalue=10, offvalue=0)
    c1.grid(row="3",column="0",columnspan="2",pady=(5,5), sticky="nw",padx=(600,0) )
    global var2
    var2=IntVar()
    c2=ttk.Checkbutton(post_window,text="Administration", variable=var2, onvalue=9, offvalue=0)
    c2.grid(row="4",column="0",columnspan="2",pady=(0,5),sticky="nw",padx=(600,0))
    global var3
    var3=IntVar()
    c3=ttk.Checkbutton(post_window,text="Medical", variable=var3, onvalue=8, offvalue=0)
    c3.grid(row="5",column="0",columnspan="2",pady=(0,5), sticky="nw",padx=(600,0) )
    global var4
    var4=IntVar()
    c4=ttk.Checkbutton(post_window,text="Academics", variable=var4, onvalue=7, offvalue=0)
    c4.grid(row="6",column="0",columnspan="2",pady=(0,5), sticky="nw",padx=(600,0) )
    global var5
    var5=IntVar()
    c5=ttk.Checkbutton(post_window,text="Hostel and Mess", variable=var5, onvalue=6, offvalue=0)
    c5.grid(row="7",column="0",columnspan="2",pady=(0,5), sticky="nw",padx=(600,0) )
    global var6
    var6=IntVar()
    c6=ttk.Checkbutton(post_window,text="Technical", variable=var6, onvalue=5, offvalue=0)
    c6.grid(row="8",column="0",columnspan="2",pady=(0,5), sticky="nw",padx=(600,0) )
    global var7
    var7=IntVar()
    c7=ttk.Checkbutton(post_window,text="Transport", variable=var7, onvalue=4, offvalue=0)
    c7.grid(row="9",column="0",columnspan="2",pady=(0,5), sticky="nw",padx=(600,0) )
    global var8
    var8=IntVar()
    c8=ttk.Checkbutton(post_window,text="Competition", variable=var8, onvalue=3, offvalue=0)
    c8.grid(row="10",column="0",columnspan="2",pady=(0,5), sticky="nw",padx=(600,0) )
    global var9
    var9=IntVar()
    c9=ttk.Checkbutton(post_window,text="Event", variable=var9, onvalue=2, offvalue=0)
    c9.grid(row="11",column="0",columnspan="2",pady=(0,5), sticky="nw",padx=(600,0) )
    global var10
    var10=IntVar()
    c10=ttk.Checkbutton(post_window,text="College Life", variable=var10, onvalue=1, offvalue=0)
    c10.grid(row="12",column="0",columnspan="2",pady=(0,5), sticky="nw",padx=(600,0) )




    post_btn=Button(post_window, text="Post!", command=combinefunc,bg="#008744",padx="50",pady="5")
    post_btn.grid(row="13",column="0",columnspan="2",padx=(400,0) )



#*****************LOGIN WINDOW**************************************************************


def open_login():


    def confirm():

        newuserlist=[]
        g2=open("UserFile.txt","rb")

        while 1:
            try:
                o = pickle.load(g2)
            except EOFError:
                break
            newuserlist.append(o)

        print(user_count)
        for j in range(len(newuserlist)):
            if(newuserlist[j].username == e1.get()):
                print(j)
                if(newuserlist[j].password == e2.get()):
                    print(j)
                    login_cnf=Label(login, text="You have successfully logged in!")
                    current_user=j
                    login_cnf.grid(row="4", column="0",columnspan="2")
                    menu=Toplevel()
                    menu.configure(bg="#a6ed8e")
                    menu.geometry("1920x1080")
                    menu.title("Menu")
                    generate_label=Label(menu, text="Choose An Option!",font='Helvetica 40 bold',bg="#a6ed8e")
                    generate_label.grid(row="0",column="0",columnspan="2",padx="390",pady=(100,50))
                    generate_icon=ImageTk.PhotoImage(Image.open("ge.png"))
                    generate_btn=Button(menu,image=generate_icon,command=makearray,bg="#a6ed8e")
                    generate_btn.image=generate_icon
                    generate_btn.grid(row="1",column="0", padx=(120,50))
                    create_icon=ImageTk.PhotoImage(Image.open("cr.png"))
                    create_btn=Button(menu,image=create_icon, command=create_post,bg="#a6ed8e")
                    create_btn.image=create_icon
                    create_btn.grid(row="1",column="1",padx=(0,120))
                    break
                else:
                    unconf_login=Label(login, text="Incorrect details! Please try again.")
                    unconf_login.grid(row="4",column="0", columnspan="2")
                    e1.delete(0,END)
                    e2.delete(0,END)
                    open_login()
                    break
            else:
                continue


    login=Toplevel()
    login.configure(bg="#a6ed8e")
    login.geometry("1920x1080")
    login.title("Login Page")

    label_title=Label(login, text="Login!",bg="#a6ed8e",font='Helvetica 40 bold')
    label_title.grid(row="0", column="0",padx="530", pady=(180,0),columnspan="2")

    e1=Entry(login, width="40", borderwidth="5")
    label1=Label(login, text="Username:",bg="#a6ed8e",font="Oxygen 18" )
    label1.grid(row="1", column="0", padx=(250,5), pady=(50,10))
    e1.grid(row="1", column="1", pady=(50,10), padx=(0,150))

    e2=Entry(login, width="40", borderwidth="5")
    label2=Label(login, text="Password:",bg="#a6ed8e",font="Oxygen 18" )
    label2.grid(row="2", column="0", padx=(250,5))
    e2.grid(row="2", column="1", padx=(0,150))

    login_btn=Button(login, text="Login", bg="#008744", padx="50", pady="5",font="Montserrat 13", command=confirm)
    login_btn.grid(row="3",column="0",columnspan="2", pady=(40,10))




#**********************SIGNUP WINDOW**************************************************************************

def open_signup():


    def confirmation():

        if e4.get()==e5.get():
            g1=open("UserFile.txt","ab")
            pickle.dump(total_posts[post_count],g1)
            g1.close()
            global user_count
            user_list[user_count].username=e3.get()
            user_list[user_count].password=e4.get()
            user_list[user_count].id=user_count+100
            user_count=user_count+1
            conf_signup=Label(signup, text="You have successfully signed up!")
            conf_signup.grid(row="5",column="0", columnspan="2")
            #print(user_count)
        else:
            unconf_signup=Label(signup, text="Incorrect details! Please try again.")
            unconf_signup.grid(row="5",column="0", columnspan="2")
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            open_signup()


    signup=Toplevel()
    signup.configure(bg="#a6ed8e")
    signup.geometry("1920x1080")
    signup.title("Sign Up Page")


    label_title2=Label(signup, text="Sign Up!",bg="#a6ed8e",font='Helvetica 40 bold')
    label_title2.grid(row="0", column="0",padx="500", pady=(180,0),columnspan="2")

    e3=Entry(signup, width="40", borderwidth="5")
    label3=Label(signup, text="Username:",bg="#a6ed8e",font="Oxygen 18" )
    label3.grid(row="1", column="0", padx=(250,5), pady=(50,10))
    e3.grid(row="1", column="1", pady=(50,10), padx=(0,150))

    e4=Entry(signup, width="40", borderwidth="5")
    label4=Label(signup, text="Password:",bg="#a6ed8e",font="Oxygen 18" )
    label4.grid(row="2", column="0", padx=(250,5), pady=(0,10))
    e4.grid(row="2", column="1", padx=(0,150), pady=(0,10))

    e5=Entry(signup, width="40", borderwidth="5")
    label5=Label(signup, text="Confirm Password:",bg="#a6ed8e",font="Oxygen 18" )
    label5.grid(row="3", column="0", padx=(250,5))
    e5.grid(row="3", column="1", padx=(0,150))

    login_btn=Button(signup, text="Sign Up", bg="#008744", padx="50", pady="5",font="Montserrat 13", command=confirmation)
    login_btn.grid(row="4",column="0",columnspan="2", pady=(40,10))




#****************MAIN WINDOW BUTTONS***************************************

logo_img=ImageTk.PhotoImage(Image.open("logo.png"))
logo_label=Label(root,image=logo_img,bg="#FFFFFF")
logo_label.pack(fill=X, pady=(100,0))
login_bt=Button(root, text="Login", bg="#008744", width="50", height="2",font="Montserrat 13 italic", command=open_login)
signup_bt=Button(root, text="Sign Up", bg="#008744", width="50", height="2", font="Montserrat 13 italic", command=open_signup)
login_bt.pack( pady=(30,10), padx="150")
signup_bt.pack( pady="10", padx="150")
root.mainloop()
