from p5 import *

n=0.0

def setup():
    size(400,225);
    # smooth()
    # frame_rate(30)

    background(0)

    # stroke_weight(0)
    no_stroke()

def draw():
    global n
    # filter(BLUR,2)
    # text_align(CENTER)
    # text_size(30)
    fill(255)
    # text("testing",mouse_x,mouse_y)
    n += 0.05

if __name__ == '__main__':
    run()

# void setup() {
#     size(400,225);
#     smooth();
#     frameRate(30);
#
#     background(0);
#
#     strokeWeight(0);
#     noStroke();
# }
#
# void draw() {
#     filter(BLUR,2);
#     //fill(0,50);
#     //rect(0,0,width,height);
#     textAlign(CENTER);
#     textSize(30);
#     fill(255);
#     text("testing",mouseX,mouseY);
#     n+=0.005;
# }
