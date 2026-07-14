def inside_viewport(x,y,width,height):
    return (
        0 <= x <= width

        and

        0 <= y <= height
    )