import numpy as np
import cv2

def unit_vector(vector):
    unit = vector / np.linalg.norm(vector)
    return unit

ball_vector = unit_vector(np.random.normal(0, 1, 2))
ball_speed = 7
ball_pos = np.array([200,200], dtype=np.float64)

def reflect(vector, norm):
    return vector + 2 * norm * np.dot(norm,-vector)

def crash_detection():
    global ball_vector,ball_pos
    y = ball_pos[0]
    x = ball_pos[1]
    if y>400:
        norm = np.array((-1,0))
        ball_vector = reflect(ball_vector,norm)
        ball_vector = unit_vector(ball_vector)
    if y<0:
        norm = np.array((1,0))
        ball_vector = reflect(ball_vector,norm)
        ball_vector = unit_vector(ball_vector)
    if x>400:
        norm = np.array((0,1))
        ball_vector = reflect(ball_vector,norm)
        ball_vector = unit_vector(ball_vector)
    if x<0:
        norm = np.array((0,-1))
        ball_vector = reflect(ball_vector,norm)
        ball_vector = unit_vector(ball_vector)

class chaser:
    def __init__(self) -> None:
        self.pos = np.array((200,200), dtype=np.float64)
        self.vector = np.array((0,0), dtype=np.float64)
        self.speed = 2 + np.random.rand() * 3

    def chase(self):
        self.vector = ball_pos - self.pos
        self.vector = unit_vector(self.vector)
        self.pos += self.vector * self.speed
    

chasers = [chaser()]

def mouse_event(event, x, y, flags, param):
    global chasers
    if event == cv2.EVENT_FLAG_LBUTTON:
        chasers.append(chaser())

    elif event == cv2.EVENT_FLAG_RBUTTON:
        chasers.pop(0)

window = cv2.namedWindow('geometry')
cv2.setMouseCallback('geometry', mouse_event)

while True:
    scr = np.full((400,400,3),(255,255,255), dtype=np.uint8)
    cv2.circle(scr, ball_pos.astype(int), 3, (0,0,0))
    crash_detection()
    ball_pos += ball_vector*ball_speed
    for i in chasers:
        i.chase()
        cv2.circle(scr, i.pos.astype(int), 3, (0,0,255))
    cv2.imshow('geometry', scr)
    if cv2.waitKey(16) & 0xFF == 27:
        break
cv2.destroyAllWindows