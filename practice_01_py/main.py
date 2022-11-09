import random
import tkinter

hand = "void"
com_list = 'Rock', 'Scissors', 'Paper'

count_com = 0  # 컴의 승리상황을 저장
count_user = 0  # 유저의 승리상황을 저장


def Start():
    Destory_menu()  # 티킨터 기존요소 제거

    label_user = tkinter.Label(tk, text="유저!!", font=("System", 45))  # 유저 라벨
    label_user.place(x=1300, y=100)
    
    button_rock = tkinter.Button(tk, text="바위", font=("System", 25), command=User_Rock)  # 바위 버튼
    button_rock.place(x=1200, y=200)
    button_scissors = tkinter.Button(tk, text="가위", font=("System", 25), command=User_Scissors)  # 가위 버튼
    button_scissors.place(x=1300, y=200)
    button_paper = tkinter.Button(tk, text="보", font=("System", 25), command=User_Paper)  # 보 버튼
    button_paper.place(x=1400, y=200)
    
    button_select = tkinter.Button(tk, text="선택!!", font=("System", 45), command=Select)  # 선택 버튼
    button_select.place(x=1300, y=300)

    label_com = tkinter.Label(tk, text="컴퓨터!!", font=("System", 45))  # 컴 라벨
    label_com.place(x=200, y=100)

    label_count_com = tkinter.Label(tk, text="0번째 승리!!", font=("System", 30))  # 컴의 승리 상황을 띄워주는 라벨 - 값이 매번 바뀜
    label_count_user = tkinter.Label(tk, text="0번째 승리!!", font=("System", 30))  # 유저의 승리 상화을 띄어주는 라벨 - 값이 매번 바뀜
    label_count_com.place(x=30, y=50)
    label_count_user.place(x=1500, y=50)

    button_end = tkinter.Button(tk, text="종료버튼.", font=("System, 30"), command=tk.destroy)
    button_end.place(x=1400, y=1000)

    tk.mainloop()
    

    
def Destory_menu():  # 초기 메뉴티킨터 요소 삭제
    label_menu.destroy()
    button_start.destroy()
    button_opthion.destroy()
    button_exit.destroy()
    cavas_main.destroy()


def User_Rock():  # 바위선택
    Destory_hand()
    cavas_hand.place(x=850, y=0)
    im_rock = tkinter.PhotoImage(file="Rock.png")
    cavas_hand.create_image(150, 150, image=im_rock, tag="im_rock")

    global hand
    hand = "Rock"
    tk.mainloop()
    

def User_Scissors():  # 가위선택
    Destory_hand()
    cavas_hand.place(x=850, y=0)
    im_scissors = tkinter.PhotoImage(file="Scissors.png")
    cavas_hand.create_image(150, 150, image=im_scissors, tag="im_scissors")

    global hand
    hand = "Scissors"
    tk.mainloop()
    

def User_Paper():  # 보 선택
    Destory_hand()
    cavas_hand.place(x=850, y=0)
    im_paper = tkinter.PhotoImage(file="Paper.png")
    cavas_hand.create_image(150, 150, image=im_paper, tag="im_paper")

    global hand
    hand = "Paper"
    tk.mainloop()
   


def Destory_hand():  # 이미지 출력 전에 기존 이미지 초기화
    cavas_hand.delete("im_rock")
    cavas_hand.delete("im_scissors")
    cavas_hand.delete("im_paper")


def Select():  # 유저가 동작을 선택했을때
    global hand
    # print(hand)

    global com_choice

    com_choice = random.choice(com_list)

    print(hand)
    if hand == "void":
        print("아무것도 선택하지 않았습니다.")


    if com_choice == "Rock":
        Com_Rock()
    elif com_choice == "Scissors":
        Com_Scissors()
    elif com_choice == "Paper":
        Com_Paper()
    elif com_choice == "void":
        print("아무것도 선택허지 않았습니다.")

    # print("컴퓨터의 값은 : ", com_choice)


def Com_Rock():
    Destory_com()
    cavas_com.place(x=450, y=0)
    im_rock = tkinter.PhotoImage(file="Rock.png")
    cavas_com.create_image(150, 150, image=im_rock, tag="im_rock")

    if hand == "Rock":  # 컴의 상태가 Rock일때 유저의 상태에 따라 승리여부 결정
        draw()
    elif hand == "Paper":
        User_win()
    else:
        Com_win()
    tk.mainloop()

def Com_Scissors():
    Destory_com()
    cavas_com.place(x=450, y=0)
    im_rock = tkinter.PhotoImage(file="Scissors.png")
    cavas_com.create_image(150, 150, image=im_rock, tag="im_scissors")

    if hand == "Scissors":
        draw()
    elif hand == "Rock":
        User_win()
    else:
        Com_win()
    tk.mainloop()

def Com_Paper():
    Destory_com()
    cavas_com.place(x=450, y=0)
    im_rock = tkinter.PhotoImage(file="Paper.png")
    cavas_com.create_image(150, 150, image=im_rock, tag="im_Paper")

    if hand == "Paper":
        draw()
    elif hand == "Scissors":
        User_win()
    else:
        Com_win()
    tk.mainloop()


def Destory_com():
    cavas_com.delete("im_rock")
    cavas_com.delete("im_scissors")
    cavas_com.delete("im_Paper")
    



def draw():
    label_Com_result["text"] = "draw..."  # 컴 결과의 text 요소를 변경
    label_User_result["text"] = "draw..."  # 유저 결과의 text 요소를 변경

    label_Com_result.place(x=500, y=500)
    label_User_result.place(x=900, y=500)
    tk.mainloop()

def User_win():
    global count_user
    count_user += 1

    label_count_user["text"] = (str(count_user) + "번째 승리!!")

    label_Com_result["text"] = "Lose..."  # 컴 결과의 text 요소를 변경
    label_User_result["text"] = "Win!!"  # 유저 결과의 text 요소를 변경

    label_Com_result.place(x=500, y=500)
    label_User_result.place(x=900, y=500)
    tk.mainloop()


def Com_win():
    global count_com
    count_com += 1

    label_count_com["text"] = (str(count_com) + "번째 ㅅ")

    label_Com_result["text"] = "Win!!"  # 컴 결과의 text 요소를 변경
    label_User_result["text"] = "Lose..."  # 유저 결과의 text 요소를 변경

    label_Com_result.place(x=500, y=500)
    label_User_result.place(x=900, y=500)
    tk.mainloop()






tk = tkinter.Tk()
tk.geometry("1800x1600")
tk.title("가위바위보")

cavas_main = tkinter.Canvas(width=500, height=500, bg="red")
cavas_main.pack()
im = tkinter.PhotoImage(file="Rock-Paper-Scissors.png")
cavas_main.create_image(250, 300, image=im, tag="im_main")

cavas_hand = tkinter.Canvas(width=300, height=300, bg="green")  # 가위, 바위, 보 의 모양이 출력되는 캔버스를 미리선언  - 유저
cavas_com = tkinter.Canvas(width=300, height=300, bg="blue")  # 가위, 바위, 보 의 모양이 출력되는 캔버슬르 미리선언  - 컴


label_Com_result = tkinter.Label(tk, text="void", font=("System", 100))  # 게임의 출력 결과를 보여주는 라벨을 미리선언 - 컴
label_User_result = tkinter.Label(tk, text="void", font=("System", 100))  # 게임의 출력 결과를 보여주는 라벨을 미리선언 - 유저


label_menu = tkinter.Label(tk, text="가위바위보~ 게임~", font=("System", 45))  # 메뉴 라벨
label_menu.pack()
button_start = tkinter.Button(tk, text="시작", font=("System", 25), command=Start)  # 시작 버튼
button_start.pack()
button_opthion = tkinter.Button(tk, text="옵션", font=("System", 25))  # 옵션 버튼
button_opthion.pack()
button_exit = tkinter.Button(tk, text="종료", font=("System", 25), command = tk.destroy)  # 종료 버튼
button_exit.pack()


label_count_com = tkinter.Label(tk, text="0번째 승리!!", font=("System", 30))  # 컴의 승리 상황을 띄워주는 라벨 - 값이 매번 바뀜
label_count_user = tkinter.Label(tk, text="0번째 승리!!", font=("System", 30))  # 유저의 승리 상화을 띄어주는 라벨 - 값이 매번 바뀜

tk.mainloop()  # 무한반복