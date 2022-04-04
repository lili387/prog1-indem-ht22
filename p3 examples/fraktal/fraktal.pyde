size_x = 2000
size_y = 2000

def setup():
    global size_x, size_y
    size(size_x,size_y)
    background(0,0,0);
    stroke(255, 255, 255)
    fill(255, 255, 255)

def draw():
    
    kvadrater = [ {"bredd" : 1.0/3, "pos_x" : 1.0/2, "pos_y" :1.0/2 }];
    
    antal_nivaer = 5
    for n in range(antal_nivaer):
        for k in kvadrater:
            rita_kvadrat(k['bredd'], k['pos_x'], k['pos_y'])
            
        nya_kvadrater = []
        for kvadrat in kvadrater:
            for ny_kvadrat in hitta_nasta_kvadrat(kvadrat['bredd'], kvadrat['pos_x'], kvadrat['pos_y']):
                nya_kvadrater.append(ny_kvadrat)    
        kvadrater = nya_kvadrater
        

def rita_kvadrat(bredd, pos_x, pos_y):
    global size_x, size_y

    pixel_x_start = size_x*(pos_x-bredd/2)
    pixel_y_start = size_y*(pos_y-bredd/2)
    pixel_bredd = bredd*size_x
    pixel_hojd = pixel_bredd
    rect(pixel_x_start, pixel_y_start, pixel_bredd, pixel_hojd); # pixel värde
    return
    

def hitta_nasta_kvadrat(bredd, pos_x, pos_y):
    hojd = bredd
    x_centers = [pos_x-bredd, pos_x, pos_x+bredd]
    y_centers = [pos_y-hojd, pos_y, pos_y+hojd]

    ny_bredd = bredd*1.0/3
    nya_kvadrater = []
    
    for x_center in x_centers:
        for y_center in y_centers:
            if x_center == pos_x and y_center == pos_y:
                continue
            
            nya_kvadrater.append({"bredd" : ny_bredd, "pos_x" : x_center, "pos_y" :y_center })
    
    return nya_kvadrater
