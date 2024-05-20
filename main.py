import time

import pyautogui
from numpy import where
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
i = 1

while i<300:
    print("\033[1;34m"f"进入第{i}次操作")
    tt1 = pyautogui.locateOnScreen('1/tt1.png', confidence=0.8)
    if tt1 is not None:
        x, y = pyautogui.center(tt1)
        pyautogui.leftClick(x+400, y)
        print("\033[1;32m""点击")
        time.sleep(1)

    p0 = pyautogui.locateOnScreen('1/p0.png', confidence=0.8)
    if p0 is not None:
        x, y = pyautogui.center(p0)
        pyautogui.leftClick(x, y)
        time.sleep(1)

    p1 = pyautogui.locateOnScreen('1/p1.png', confidence=0.8)
    p2 = pyautogui.locateOnScreen('1/p2.png', confidence=0.8)
    p3 = pyautogui.locateOnScreen('1/p3.png', confidence=0.8)
    if p1 is not None:
        b = 1
    if p2 is not None:
        b = 2
    if p3 is not None:
        b = 3


    t22 = pyautogui.locateOnScreen('1/t22.png', confidence=0.8)
    if t22 is not None:
        x, y = pyautogui.center(t22)
        pyautogui.leftClick(x, y)
        print("\033[1;32m""点击")
        time.sleep(3)


    r4 = pyautogui.locateOnScreen('1/4.png', confidence=0.8)
    r44 = pyautogui.locateOnScreen('1/44.png', confidence=0.8)
    pp1 = pyautogui.locateOnScreen('1/pp1.png', confidence=0.8)
    pp2 = pyautogui.locateOnScreen('1/pp2.png', confidence=0.8)
    if r4 is not None:
        x, y = pyautogui.center(r4)
        pyautogui.leftClick(x, y)
        print("\033[1;32m""轻触继续")
        time.sleep(1)
    elif r44 is not None:
        if b == 1:
            print("\033[1;32m""使用轻装")
        if b == 2:
            pyautogui.leftClick(pp1)
            print("\033[1;32m""切换重装")
        if b == 3:
            pyautogui.leftClick(pp2)
            print("\033[1;32m""切换神秘")
        time.sleep(2)
        x, y = pyautogui.center(r44)
        pyautogui.leftClick(x, y)
        print("\033[1;32m""进入战斗，等待60秒")
        time.sleep(60)
        k = 0
        while k<1:
            r444 = pyautogui.locateOnScreen('1/444.png', confidence=0.8)
            r4444 = pyautogui.locateOnScreen('1/4444.png', confidence=0.8)
            #c = 0
            if r444 is not None:
                x, y = pyautogui.center(r444)
                pyautogui.leftClick(x, y)
                print("\033[1;32m""战斗结束")
                #c += 1
                k += 1
                time.sleep(3)
            elif r4444 is not None:
                x, y = pyautogui.center(r4444)
                pyautogui.leftClick(x, y)
                print("\033[1;32m""战斗失败")
                time.sleep(3)
                pyautogui.leftClick(x, y)
                #c += 1
                k += 1
                time.sleep(3)
            else:
                print("未检测到画面")
            #k = c
    else:
        print("\033[1;31m"'未发现4&44，结算和战斗')

    t3 = pyautogui.locateOnScreen('1/t3.png', confidence=0.8)
    if t3 is not None:
        x, y = pyautogui.center(t3)
        pyautogui.leftClick(x, y)
        print("\033[1;32m""进入下一节")
        time.sleep(2)
        pyautogui.leftClick(x, y)
        time.sleep(1)
        pyautogui.leftClick(x, y)
        time.sleep(3)
        pyautogui.leftClick(x+100, y)
        time.sleep(10)
    else:
        print("\033[1;31m"'未发现5')
    i += 1

