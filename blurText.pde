n=0.0;

void setup() {
    background(0);
    size(400,225);
    smooth();
    frameRate(30);

    strokeWeight(0);
    noStroke();
}

void draw() {
    filter(BLUR,2);
    //fill(0,50);
    //rect(0,0,width,height);
    textAlign(CENTER);
    textSize(30);
    fill(255);
    text("testing",mouseX,mouseY);
    n+=0.005;
}
