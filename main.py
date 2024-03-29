import pygame
import random
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH,HEIGHT=1000,500
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))

BLUE=(0,255,255)
YELLOW=(255,255,0)
RED=(255,0,0)
ORANGE=(255,153,51)
WHITE=(255,255,255)
BLACK=(0,0,0)
PURPLE=(138,43,226)

FPS=60
VEL=5
AIM_SIZE=30
TARGET_SIZE=70
TABLE=HEIGHT-HEIGHT//4
FONT_SIZE=32
INITIAL_TARGETS=5
INITIAL_RANDOM_MIN=-1
INITIAL_RANDOM_MAX=1
ENTER_NAME_X=WIDTH//2-WIDTH//10
ENTER_NAME_Y=HEIGHT//4-HEIGHT//20
ENTER_NAME_WIDTH=len('Enter name ')*FONT_SIZE//2 +6
GAME_OVER_WIDTH=len('Game over!')*FONT_SIZE//2+6
NAME_X=WIDTH//100
NAME_Y=TABLE + HEIGHT//50
LEVEL_GOAL_X=WIDTH//2-WIDTH//15
LEVEL_GOAL_Y=NAME_Y
SCORE_X=WIDTH-WIDTH//5
SCORE_Y=NAME_Y
HEALTH_X=NAME_X
HEALTH_Y=LEVEL_GOAL_Y+HEIGHT//10
TIME_X=LEVEL_GOAL_X
TIME_Y=HEALTH_Y
TEXT_X=WIDTH//2 - GAME_OVER_WIDTH//2
TEXT_Y=HEIGHT//2 - FONT_SIZE//2
HEART_SIZE=32
LEADERBORD_X=ENTER_NAME_X -10
LEADERBORD_Y=ENTER_NAME_Y+HEIGHT//2 -10
QUIT_X=LEADERBORD_X
QUIT_Y=LEADERBORD_Y+30


global  ENTER_NAME_FONT

OK_SPECIAL=[]
SPECIAL_TARGET=[]
SPECIAL_VEL_X=[]
SPECIAL_VEL_Y=[]

BACKGROUND=pygame.transform.scale(pygame.image.load('background.jpg'),(WIDTH,HEIGHT//4))
AIM_IMAGE=pygame.transform.scale(pygame.image.load('aim.png'),(AIM_SIZE,AIM_SIZE))
MENU_IMAGE=pygame.transform.scale(pygame.image.load('gunimage.jpg'),(WIDTH,HEIGHT))
CURSOR_IMAGE=pygame.transform.scale(pygame.image.load('cursor.png'),(AIM_SIZE,AIM_SIZE))
WHITE_IMAGE=pygame.transform.scale(pygame.image.load('white.png'),(ENTER_NAME_WIDTH,FONT_SIZE))
HEART_IMAGE=pygame.transform.scale(pygame.image.load('heart.png'),(HEART_SIZE,HEART_SIZE))
SPECIAL_TARGET_IMAGE=pygame.transform.scale(pygame.image.load('target.png'),(TARGET_SIZE,TARGET_SIZE))

SPECIAL_TARGET.append(pygame.Rect(random.randint(0,WIDTH-TARGET_SIZE),random.randint(0,TABLE-TARGET_SIZE),TARGET_SIZE,TARGET_SIZE))
OK_SPECIAL.append(0)
SPECIAL_VEL_X.append(random.randint(INITIAL_RANDOM_MIN,INITIAL_RANDOM_MAX)) 
SPECIAL_VEL_Y.append(random.randint(INITIAL_RANDOM_MIN,INITIAL_RANDOM_MAX))

OK=[]
TARGET_IMAGE=[]
TARGET=[]
VEL_TARGET_X=[]
VEL_TARGET_Y=[]
for i in range(INITIAL_TARGETS):
  TARGET_IMAGE.append(pygame.transform.scale(pygame.image.load('bullseye.png'),(TARGET_SIZE,TARGET_SIZE)))
  TARGET.append(pygame.Rect(random.randint(0,WIDTH-TARGET_SIZE),random.randint(0,TABLE-TARGET_SIZE),TARGET_SIZE,TARGET_SIZE))
  VEL_TARGET_X.append(random.randint(INITIAL_RANDOM_MIN,INITIAL_RANDOM_MAX)) 
  VEL_TARGET_Y.append(random.randint(INITIAL_RANDOM_MIN,INITIAL_RANDOM_MAX))
  OK.append(0)

pygame.display.set_caption("Rapid Fire")
ICON=pygame.image.load('pistol.png')
pygame.display.set_icon(ICON)

font=pygame.font.Font('freesansbold.ttf',FONT_SIZE)
CLOCK=pygame.time.Clock()
pygame.mouse.set_visible(False)
AIM=pygame.Rect(0,0,AIM_SIZE,AIM_SIZE)
CURSOR=pygame.Rect(0,0,AIM_SIZE,AIM_SIZE)

TEXT_QUIT=font.render("QUIT",True,BLACK)
TEXT_LEADERBOARD=font.render("LEADERBOARD",True,BLACK)
INPUT_RECTANGLE=pygame.Rect(ENTER_NAME_X,ENTER_NAME_Y,ENTER_NAME_WIDTH,32)
LEADERBOARD_RECTANGLE=pygame.Rect(LEADERBORD_X,LEADERBORD_Y,TEXT_LEADERBOARD.get_width(),32)
QUIT_RECTANGLE=pygame.Rect(QUIT_X,QUIT_Y,TEXT_QUIT.get_width(),32)

COLOR_ACTIVE=pygame.Color('aliceblue')
COLOR_PASIVE=WHITE
COLOR_NAME=(153,153,0)

TIMER_TEXT=font.render("01:00",True,WHITE)
TIMER=pygame.USEREVENT + 1
pygame.time.set_timer(TIMER,1000)

TARGET_SOUND=pygame.mixer.Sound(r'D:\ATM\Anul 1\Rapid Fire\gun.wav')
GAME_OVER_SOUND=pygame.mixer.Sound(r'D:\ATM\Anul 1\Rapid Fire\game_over.wav')
LOOSE_HEART_SOUND=pygame.mixer.Sound(r'D:\ATM\Anul 1\Rapid Fire\ouchmp3-14591.wav')
INTRO_SOUND=pygame.mixer.Sound(r'D:\ATM\Anul 1\Rapid Fire\intro.wav')
EXCELENT_SOUND=pygame.mixer.Sound(r'D:\ATM\Anul 1\Rapid Fire\excelent.wav')

def draw_target(SPECIAL_TARGET_SCORE,NUM_TARGETS,RANDOM_MIN,RANDOM_MAX):
            if    SPECIAL_VEL_X[0]!=0 and SPECIAL_VEL_Y[0]!=0 and   SPECIAL_VEL_Y[0]+SPECIAL_TARGET[0].y<TABLE - TARGET_SIZE:
                        SPECIAL_TARGET[0].x+=SPECIAL_VEL_X[0]
                        SPECIAL_TARGET[0].y+=SPECIAL_VEL_Y[0]
            else:
                 
                                                      SPECIAL_VEL_X[0]=random.randint(RANDOM_MIN,RANDOM_MAX)
                                                      SPECIAL_VEL_Y[0]=random.randint(RANDOM_MIN,RANDOM_MAX)            
            for i in range(NUM_TARGETS):
                 if   VEL_TARGET_X[i]!=0 and VEL_TARGET_Y[i]!=0  and VEL_TARGET_Y[i]+TARGET[i].y<TABLE - TARGET_SIZE: 
                        TARGET[i].x+=VEL_TARGET_X[i]
                        TARGET[i].y+=VEL_TARGET_Y[i]
                 else:
                      
                                                      VEL_TARGET_X[i]=random.randint(RANDOM_MIN,RANDOM_MAX)
                                                      VEL_TARGET_Y[i]=random.randint(RANDOM_MIN,RANDOM_MAX)

                 if OK[i]==0:          
                         SCREEN.blit(TARGET_IMAGE[i],(TARGET[i].x,TARGET[i].y))
            if OK_SPECIAL[0]==0:
                   TEXT=font.render(str(SPECIAL_TARGET_SCORE),True,WHITE)
                   SCREEN.blit(SPECIAL_TARGET_IMAGE,(SPECIAL_TARGET[0].x,SPECIAL_TARGET[0].y)) 
                   SCREEN.blit(TEXT,(SPECIAL_TARGET[0].x+25,SPECIAL_TARGET[0].y+ 20))

def draw_aim():
      global mouse
      mouse=pygame.mouse.get_pos()
      AIM.x=mouse[0]
      AIM.y=mouse[1]
      SCREEN.blit(AIM_IMAGE,(AIM.x,AIM.y))

def draw_window(SPECIAL_TARGET_SCORE,SCORE,POINTS_REMAIN,NUM_TARGETS,RANDOM_MIN,RANDOM_MAX,HEALTH,NAME):
      SCREEN.fill(BLUE)
      SCREEN.blit(BACKGROUND,(0,TABLE))
      draw_target(SPECIAL_TARGET_SCORE,NUM_TARGETS,RANDOM_MIN,RANDOM_MAX)
      draw_aim()
      draw_score(SCORE)
      draw_level_goal(POINTS_REMAIN)
      draw_name(NAME)
      draw_health(HEALTH)  
   
def draw_name(NAME):
      NAME_FONT=font.render("Player:" + NAME,True,WHITE)
      SCREEN.blit(NAME_FONT,(NAME_X,NAME_Y))

def draw_score(SCORE):
      SCORE_FONT=font.render("Score: " + str(SCORE),True,WHITE)
      SCREEN.blit(SCORE_FONT,(SCORE_X,SCORE_Y))

def draw_level_goal(POINTS_REMAIN):
      LEVEL_GOAL_FONT=font.render("Level Goal: " + str(POINTS_REMAIN),True,WHITE)
      SCREEN.blit(LEVEL_GOAL_FONT,(LEVEL_GOAL_X, LEVEL_GOAL_Y))

def draw_health(HEALTH):
      HEALTH_FONT=font.render("Health:",True,WHITE)
      SCREEN.blit(HEALTH_FONT,(HEALTH_X,HEALTH_Y))
      HEART_X=HEALTH_X +HEALTH_FONT.get_width()
      HEART_Y=HEALTH_Y
      for i in range(HEALTH):
            HEART_X+=HEART_SIZE + 5
            SCREEN.blit(HEART_IMAGE,(HEART_X, HEART_Y))

def draw_cursor():
    global ARROW
    ARROW=pygame.mouse.get_pos()
    CURSOR.x=ARROW[0]
    CURSOR.y=ARROW[1]
    SCREEN.blit(CURSOR_IMAGE,(CURSOR.x,CURSOR.y))
    pygame.display.update()  

def draw_introduction(NAME,COLOR): 
      SCREEN.blit(MENU_IMAGE,(0,0)) 
      pygame.draw.rect(SCREEN,COLOR,INPUT_RECTANGLE)
      if COLOR==COLOR_PASIVE:
            TEXT_SURFACE=font.render("Enter Name",True,BLACK)
            SCREEN.blit(TEXT_SURFACE,(INPUT_RECTANGLE.x, INPUT_RECTANGLE.y))
      else:      
            TEXT_SURFACE=font.render(NAME,True,BLACK)
            SCREEN.blit(TEXT_SURFACE,(INPUT_RECTANGLE.x, INPUT_RECTANGLE.y))            
            INPUT_RECTANGLE.w=max(100,TEXT_SURFACE.get_width()+10)
      draw_cursor()
      pygame.display.update()

def draw_menu(NAME):
     SCREEN.blit(MENU_IMAGE,(0,0))
     pygame.draw.rect(SCREEN,WHITE,INPUT_RECTANGLE)
     TEXT_SURFACE=font.render("Play Game",True,BLACK)
     SCREEN.blit(TEXT_SURFACE,(INPUT_RECTANGLE.x, INPUT_RECTANGLE.y))
     draw_name_menu(NAME)
     draw_leaderboard()
     draw_quit()
     draw_cursor()
     pygame.display.update()     

def draw_name_menu(NAME):
      TEXT_SURFACE=font.render("Welcome, "+(NAME),True,COLOR_NAME)
      SCREEN.blit(TEXT_SURFACE,(10,10))

def draw_leaderboard():
       pygame.draw.rect(SCREEN,WHITE,LEADERBOARD_RECTANGLE)
       SCREEN.blit(TEXT_LEADERBOARD,(LEADERBORD_X,LEADERBORD_Y))

def draw_quit():
  pygame.draw.rect(SCREEN,WHITE,QUIT_RECTANGLE)
  SCREEN.blit(TEXT_QUIT,(QUIT_X,QUIT_Y))       

def draw_text():
      TEXT="GAME OVER!"
      TEXT_FONT=font.render(TEXT,True,BLACK)
      SCREEN.blit(TEXT_FONT,(WIDTH//2-TEXT_FONT.get_width()//2 ,HEIGHT//2-TEXT_FONT.get_height()))
      pygame.display.update()
      pygame.time.wait(5000)

def draw_time(TIMER_SEC):
      TIMER_TEXT=font.render("00:%02d"%TIMER_SEC,True,WHITE)
      SCREEN.blit(TIMER_TEXT,(TIME_X,TIME_Y))
      pygame.display.update()

def main():
    RUN=True
    CHECK=0
    CHECK_LEADERBOARD=0
    CHECK_QUIT=0
    SCORE=0
    LEVEL_GOAL=5
    POINTS_REMAIN=LEVEL_GOAL
    HEALTH=5
    NUM_TARGETS=INITIAL_TARGETS
    RANDOM_MIN=INITIAL_RANDOM_MIN
    RANDOM_MAX=INITIAL_RANDOM_MAX
    ACTIVE= False
    NAME= ''
    COLOR=COLOR_PASIVE
    TIMER_SEC=59
    TARGET_APPARITION=1
    SPECIAL_TARGET_APPARITION=1
    PERMISSION_TARGET=0
    KEEP_NAMES=[]
    KEEP_SCORES=[]
    LINE_X=0
    LINE_Y=0
    CHECK_LINES=0
    SPACES_FOR_SCORE=30
    ENDTIME_SPECIAL=0
    STARTTIME_SPECIAL=time.time()
    STARTTIME=time.time()
    ENDTIME=0
    while RUN:
      KEY_PRESSED=pygame.key.get_pressed()
      CLOCK.tick(FPS)
      for event in pygame.event.get():
             CHECK_HEALTH=0
             PERMISSION_TARGET=0
             OK_SCORE=0

             if event.type==pygame.QUIT:
               RUN=False

             if CHECK==0:
                  if event.type==pygame.MOUSEBUTTONDOWN:
                        if INPUT_RECTANGLE.collidepoint(event.pos):
                              ACTIVE=True
                        else: 
                              ACTIVE=False
                  if event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_BACKSPACE:
                             NAME= NAME[:-1]
                        else:
                              NAME+=event.unicode
                  if ACTIVE:
                        COLOR=COLOR_ACTIVE
                  else:
                        COLOR=COLOR_PASIVE
                  draw_introduction(NAME,COLOR)
                  if KEY_PRESSED[pygame.K_RETURN]:
                                CHECK=1
                                NAME=NAME[:-1]
             
             if CHECK==1 and CHECK_LEADERBOARD==0:
                  pygame.mixer.Sound.play(INTRO_SOUND)
                  draw_menu(NAME)
                  if event.type==pygame.MOUSEBUTTONDOWN:
                        if INPUT_RECTANGLE.collidepoint(event.pos):
                              CHECK=2
                        if LEADERBOARD_RECTANGLE.collidepoint(event.pos):
                              CHECK_LEADERBOARD=1
                        if QUIT_RECTANGLE.collidepoint(event.pos):
                             CHECK_QUIT=1 

             if CHECK_LEADERBOARD==1:
                             SCREEN.fill(WHITE)
                             
                             FILE=open('Leaderboard.txt','r')
                             LINE_Y=0
                             for EACH in FILE:
                                           EACH=EACH[:-1]
                                           LINE_FONT=font.render(EACH,True,BLACK)
                                           SCREEN.blit(LINE_FONT,(LINE_X,LINE_Y))
                                           LINE_Y+=LINE_FONT.get_height()
                             draw_cursor()
                             KEEP_NAMES.clear()
                             KEEP_SCORES.clear()
                             if CHECK_LINES==1:  
                                  pygame.time.delay(1000000000)
                             CHECK_LINES=1            
                             pygame.display.update()                    

             if CHECK_QUIT==1:
                             RUN=False

             if CHECK==2:
                 ENDTIME=time.time()
                 pygame.mixer.Sound.stop(INTRO_SOUND)
                 draw_window(SPECIAL_TARGET_APPARITION,SCORE,POINTS_REMAIN,NUM_TARGETS,RANDOM_MIN,RANDOM_MAX,HEALTH,NAME)          
                 if ENDTIME-STARTTIME>1:
                          if TIMER_SEC>0:
                                TIMER_SEC-=1
                                STARTTIME=time.time()                            
                 draw_time(TIMER_SEC)

                 for i in range(NUM_TARGETS):
                                    OK[i]=0

                 if OK_SPECIAL[0]==1: 
                              if ENDTIME_SPECIAL-STARTTIME_SPECIAL>=SPECIAL_TARGET_APPARITION:
                                    OK_SPECIAL[0]=0
                                    STARTTIME_SPECIAL=time.time()

                 if SPECIAL_TARGET[0].x<0 - TARGET_SIZE or SPECIAL_TARGET[0].x>WIDTH or SPECIAL_TARGET[0].y<0-TARGET_SIZE or SPECIAL_TARGET[0].y>TABLE:
                           ENDTIME_SPECIAL=time.time()
                           OK_SPECIAL[0]=1
                           SPECIAL_TARGET[0]=pygame.Rect(random.randint(0,WIDTH-TARGET_SIZE),random.randint(0,TABLE-TARGET_SIZE),TARGET_SIZE,TARGET_SIZE)
                           SPECIAL_VEL_X[0]=random.randint(RANDOM_MIN,RANDOM_MAX)
                           SPECIAL_VEL_Y[0]=random.randint(RANDOM_MIN,RANDOM_MAX)
                           CHECK_HEALTH=1
                           PERMISSION_TARGET=1

                 for i in range(NUM_TARGETS):
                      if TARGET[i].x<0-TARGET_SIZE or TARGET[i].x>WIDTH or TARGET[i].y<0-TARGET_SIZE or TARGET[i].y>TABLE:
                           OK[i]=1
                           TARGET[i]=pygame.Rect(random.randint(0,WIDTH-TARGET_SIZE),random.randint(0,TABLE-TARGET_SIZE),TARGET_SIZE,TARGET_SIZE)
                           VEL_TARGET_X[i]=random.randint(RANDOM_MIN,RANDOM_MAX)
                           VEL_TARGET_Y[i]=random.randint(RANDOM_MIN,RANDOM_MAX)
                           CHECK_HEALTH=1

             if CHECK==2 and event.type==pygame.MOUSEBUTTONUP: 
                  if SPECIAL_TARGET[0].collidepoint(event.pos) and OK_SPECIAL[0]==0:
                           pygame.mixer.Sound.play(TARGET_SOUND)
                           ENDTIME_SPECIAL=time.time()
                           OK_SCORE=1
                           OK_SPECIAL[0]=1
                           SPECIAL_TARGET[0]=pygame.Rect(random.randint(0,WIDTH-TARGET_SIZE),random.randint(0,TABLE-TARGET_SIZE),TARGET_SIZE,TARGET_SIZE)
                           SPECIAL_VEL_X[0]=random.randint(RANDOM_MIN,RANDOM_MAX)
                           SPECIAL_VEL_Y[0]=random.randint(RANDOM_MIN,RANDOM_MAX)
                           CHECK_HEALTH=1
                           PERMISSION_TARGET=1
                           
                  if OK_SCORE==1:
                           SCORE+=SPECIAL_TARGET_APPARITION
                           POINTS_REMAIN-=SPECIAL_TARGET_APPARITION   
                  for i in range(NUM_TARGETS) :   
                       if  TARGET[i].collidepoint(event.pos) and PERMISSION_TARGET==0 and OK[i]==0:
                              pygame.mixer.Sound.play(TARGET_SOUND)
                              OK[i]=1
                              TARGET[i]=pygame.Rect(random.randint(0,WIDTH-TARGET_SIZE),random.randint(0,TABLE-TARGET_SIZE),TARGET_SIZE,TARGET_SIZE)
                              VEL_TARGET_X[i]=random.randint(RANDOM_MIN,RANDOM_MAX)
                              VEL_TARGET_Y[i]=random.randint(RANDOM_MIN,RANDOM_MAX)
                              CHECK_HEALTH=1
                              
                       if OK[i]==1:
                              SCORE+=1
                              POINTS_REMAIN-=1
                              break
                  if CHECK_HEALTH==0 and TIMER_SEC<58:
                             pygame.mixer.Sound.play(LOOSE_HEART_SOUND)
                             HEALTH-=1
             
             if (HEALTH==0 or TIMER_SEC==0) and CHECK==2:
                    pygame.mixer.Sound.play(GAME_OVER_SOUND)
                    PARITY=0
                    VERIFY=0
                    with open('Leaderboard.txt','r') as file:
                                  for line in file:
                                         for word in line.split():
                                                      if PARITY%2==0 and PARITY>1:
                                                             KEEP_NAMES.append(word)
                                                      if PARITY%2==1 and PARITY>1:
                                                            KEEP_SCORES.append(word)
                                                      PARITY+=1

                    for i in range(len(KEEP_NAMES)):
                         if(KEEP_NAMES[i]==NAME):
                                    if SCORE>int(KEEP_SCORES[i]):
                                                KEEP_SCORES[i]=str(SCORE)           
                                    VERIFY=1
                                    break  

                    if VERIFY==0:    
                              KEEP_NAMES.append(NAME)
                              CONVERTER=str(SCORE)
                              KEEP_SCORES.append(CONVERTER)

                    for i in range(len(KEEP_SCORES)):
                                  MAX_IDX=i
                                  for j in range(i+1,len(KEEP_SCORES)):
                                        if int(KEEP_SCORES[MAX_IDX])<int(KEEP_SCORES[j]):
                                               MAX_IDX=j
                                  KEEP_SCORES[i],KEEP_SCORES[MAX_IDX]=KEEP_SCORES[MAX_IDX], KEEP_SCORES[i]            
                                  KEEP_NAMES[i],KEEP_NAMES[MAX_IDX]=KEEP_NAMES[MAX_IDX], KEEP_NAMES[i]

                    FILE1=open('Leaderboard.txt','w')
                    FILE1.write("NAME")
                    for i in range(SPACES_FOR_SCORE):
                              FILE1.write(" ")
                    FILE1.write("SCORE\n")          
                    for i in range(len(KEEP_NAMES)):
                                          FILE1.write(KEEP_NAMES[i])
                                          for j in range(SPACES_FOR_SCORE - len(KEEP_NAMES[i])+5):
                                                  FILE1.write(" ")
                                          FILE1.write(KEEP_SCORES[i])
                                          FILE1.write("\n")
                    KEEP_NAMES.clear()
                    KEEP_SCORES.clear()
                    draw_window(SPECIAL_TARGET_APPARITION,SCORE,POINTS_REMAIN,NUM_TARGETS,RANDOM_MIN,RANDOM_MAX,HEALTH,NAME)
                    draw_text()
                    RUN=False

             if POINTS_REMAIN<0 and CHECK==2:
                  POINTS_REMAIN=0

             if POINTS_REMAIN==0 and CHECK==2:
                pygame.mixer.Sound.play(EXCELENT_SOUND) 
                SPECIAL_TARGET_APPARITION+=1
                TARGET_APPARITION+=5
                LEVEL_GOAL+=5
                RANDOM_MAX+=3
                RANDOM_MIN -=3
                POINTS_REMAIN=LEVEL_GOAL
                TIMER_SEC=59

    pygame.quit()             

if __name__=="__main__":
    main()
