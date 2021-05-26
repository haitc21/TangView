from selenium import webdriver
import time

url = 'https://www.youtube.com/watch?v=Nj2U6rhnucI&ab_channel=DuaLipaDuaLipaK%C3%AAnhngh%E1%BB%87s%C4%A9ch%C3%ADnhth%E1%BB%A9c'
buton_play_selector = '#movie_player > div.ytp-cued-thumbnail-overlay > button'
script_open_new_tab = "window.open('" + url + "')"
tab_index = 0
tab_count = 1
total_tabs = 1
NUMBER_OF_TAB = 4
LOOP_TIME = 10 # thời gian chờ chuyển tab (2)
TIME_VIEW = 15 # thời gian xem video

# bật chrome và mở link trong get (tab1) tab_index = 0
brower = webdriver.Chrome()
brower.get(url)
# click nút mở
time.sleep(1) # đợi 1s để trang load xong mơi ấn play
play_button = brower.find_element_by_css_selector(buton_play_selector)
play_button.click()
print("tab_index: "+ str(tab_index))
print("total_tabs: "+ str(total_tabs))
time.sleep(LOOP_TIME)

while True:
    tab_index = (tab_index + 1) % NUMBER_OF_TAB
    if tab_count < NUMBER_OF_TAB: 
        tab_count = tab_count + 1
        brower.execute_script(script_open_new_tab)
    total_tabs = total_tabs + 1
    if tab_count >= NUMBER_OF_TAB: 
        if total_tabs % NUMBER_OF_TAB == 0:
            print("------End tab---------")
            time.sleep(TIME_VIEW)
        handle_window = brower.window_handles[tab_index]
        brower.switch_to.window(handle_window)
        time.sleep(1)
        brower.get(url)

    time.sleep(LOOP_TIME)
    
    

