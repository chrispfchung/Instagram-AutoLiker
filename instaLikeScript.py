import pyautogui
import time
import sys

#Keep pulling cursor to top left corner for 2.5 seconds to abort script
pyautogui.FAILSAFE = True


##Instructions
#open chrome to full screen
#Run python -i instalikescript.py in terminal

##Notes
#If you need to stop, go terminal press ctrl+c
#Keep the .png files in the same directory, script needs them to run
#keep top left quadrant clear for pyautogui click on to chrome when you run

#Automatically enters username link with username argument
def enter_IG_link(username):
    pyautogui.click(0,430,clicks=2)
    pyautogui.hotkey('command', 'n')
    pyautogui.hotkey('command', 'l')
    str = 'https://www.instagram.com/' + '{}' + '/?hl=en'
    pyautogui.typewrite(str.format(username))
    pyautogui.hotkey('enter')


#Automatically enters hashtag link with hashtag argument
def enter_IG_hash_link(hashtag):
    pyautogui.click(409,389,clicks=2)
    pyautogui.hotkey('command', 'n')
    pyautogui.hotkey('command', 'l')
    str = 'https://www.instagram.com/explore/tags/' + '{}' + '/'
    pyautogui.typewrite(str.format(hashtag))
    pyautogui.hotkey('enter')


#Clicks first photo on username's page (Adjust click coordinates to your own screen)
def click_someones_first_photo():
    time.sleep(6)
    pyautogui.click(525,750, clicks=1 ,interval=0.5)


#Clicks first photo on selected hashtag's page (Adjust click coordinates to your own screen)
def click_first_hashtag_photo():
    time.sleep(7)
    pyautogui.click(395,492, clicks=1, interval=0.5)
    time.sleep(2)


#Likes photos on someones page (Define how many of their posts you'll like with 'end' var)
def like_someones_photos():
    count = 0
    end = 30
    while count < end:
        if count == end:
            break
        locate_heart = pyautogui.locateOnScreen('Heart.png', region=(750,188, 300,600))
        if locate_heart == None:
            pyautogui.press('right')
            time.sleep(2)
            count += 1
            continue
        hearts_center = pyautogui.center(locate_heart)
        click_heart = pyautogui.click(hearts_center, clicks=1, interval=0.5)
        count +=1
        pyautogui.press('right')
        if pyautogui.locateOnScreen('Heart.png'):
            continue


#Likes hashtag photos (define when to stop with 'end' variable)
def like_one_hashtag():
    count = 0
    end = 95
    while count < end:
        if count == end:
            break
        locate_heart = pyautogui.locateOnScreen('Heart.png', region=(670,570, 400,400))
        if locate_heart == None:
            pyautogui.press('right')
            time.sleep(2)
            count += 1
            continue
        hearts_center = pyautogui.center(locate_heart)
        click_heart = pyautogui.click(hearts_center, clicks=1, interval=0.5)
        count +=1
        pyautogui.press('right')
        if pyautogui.locateOnScreen('Heart.png'):
            continue

def like_multiple_hashtags(hashtags):
    hashtags = ['datascience', 'workethic', 'power', 'inspiration']
    count = 0
    end = 20
    finish_count = 0
    finish = end*len(hashtags)
    for i in hashtags:
        enter_IG_hash_link(i)
        click_first_hashtag_photo()
        while finish_count < finish:
            locate_heart = pyautogui.locateOnScreen('Heart.png', region=(670,570, 400,400))
            if locate_heart == None:
                pyautogui.press('right')
                time.sleep(2)
                count += 1
                finish_count += 1
                continue
            hearts_center = pyautogui.center(locate_heart)
            click_heart = pyautogui.click(hearts_center, clicks=1, interval=0.5)
            count +=1
            finish_count += 1
            pyautogui.press('right')
            if pyautogui.locateOnScreen('Heart.png'):
                continue
            if count == end:
                pyautogui.hotkey('command', 'w')
                count = 0
                break
            # if finish_count == end*(len(hashtags)/2):
            #     time.sleep(600)
            #     continue
    print('10X')









###Like an entire person's post after inserting their username
# enter_IG_link('tang.zi')
# click_someones_first_photo()
# like_someones_photos()
#
#
# ###Like an entire page of chosen hashtag
# enter_IG_hash_link('finance') #function with selected hashtag
# click_first_hashtag_photo() #function to click first hashtag
# like_one_hashtag() #function to start liking the photos
# pyautogui.click(19,23, clicks=2)
# enter_IG_hash_link('patagonia') #function with selected hashtag


###Like multiple hashtags (requires initial hashtag and specified hashtags within function)
like_multiple_hashtags('hashtags')
