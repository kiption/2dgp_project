# 오브젝트 스크롤

def get_scroll(map_length, player):
    scroll = player.scroll

    if 0 <= player.x < 300:
        scroll = 0
    elif player.x < player.scroll:
        pass
    elif player.scroll + 600 >= map_length:
        scroll = map_length - 600
    else:
        scroll = player.x - 300

    return scroll

