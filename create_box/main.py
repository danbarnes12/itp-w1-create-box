"""This is the entry point of the program."""


def create_box(height, width, character):
    if height < 1 or width < 1:
        'Please enter height and width of at least 1'
    height_counter = 1
    width_counter = 1
    box = character
    while width_counter < width:
        box += character
        width_counter += 1
    box += '\n' 
    while height_counter < height:
        for i in range(width_counter):
            box += character
        box += '\n'
        height_counter += 1
    return box

def create_box_border(border_height,border_width,border_character):
    if border_height < 1 or border_width < 1:
        'Please enter border height and width of at least 1'
    border_height_counter = 1
    border_width_counter = 1
    box_border = border_character
    while border_width_counter < border_width:
        box_border += border_character
        border_width_counter += 1
    box_border += '\n'
    while border_height_counter < (border_height - 1):
        box_border += border_character
        for i in range(border_width_counter - 2):
            box_border += ' '
        box_border += border_character
        box_border += '\n'
        border_height_counter += 1
    for i in range(border_width_counter):
        box_border += border_character    
    box_border += '\n'
    return box_border
    
if __name__ == '__main__':
    create_box(3, 4, '*')
