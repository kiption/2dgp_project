def collide_check(o1, o2):
    # bounding box
    o1_left, o1_bottom, o1_right, o1_top = o1.get_bb()

    o2_left, o2_bottom, o2_right, o2_top = o2.get_bb()
    o2_mid_x, o2_mid_y = o2.x, o2.y

    # if o1_bottom > o2_top or o1_top < o2_bottom or o1_right < o2_left or o1_left > o2_right:
    #     return

    # player 위
    if o2_bottom <= o1_top <= o2_mid_y:
        if o2_left <= o1_left <= o2_right:
            return "top"
        if o2_left <= o1_right <= o2_right:
            return "top"
        if o2_left >= o1_left and o2_right <= o1_right:
            return "top"

    # player 아래
    if o2_mid_y <= o1_bottom <= o2_top:
        if o2_left <= o1_left <= o2_right:
            return "bottom"
        if o2_left <= o1_right <= o2_right:
            return "bottom"
        if o2_left >= o1_left and o2_right <= o1_right:
            return "bottom"

    # player 왼쪽
    if o2_mid_x <= o1_left <= o2_right:
        if o2_bottom <= o1_top <= o2_top:
            return "left"
        if o2_bottom <= o1_bottom <= o2_top:
            return "left"
        if o1_bottom <= o2_top <= o1_top:
            return "left"
        if o1_bottom <= o2_bottom <= o1_top:
            return "left"

    # player 오른쪽
    if o2_left <= o1_right <= o2_mid_x:       # player충돌rect 오른쪽이 obj 안에 있을 때
        if o2_bottom <= o1_top <= o2_top:     # player충돌rect 윗변이 obj 안에 있음
            return "right"
        if o2_bottom <= o1_bottom <= o2_top:  # player충돌rect 아랫변이 obj 안에 있음
            return "right"
        if o1_bottom <= o2_top <= o1_top:    # obj충돌rect 윗변이 player 안에 있음
            return "right"
        if o1_bottom <= o2_bottom <= o1_top: # obj충돌rect 아랫변이 player 안에 있음
            return "right"

    return
