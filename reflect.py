import numpy as np
import cv2

def unit_vector(vector):
    unit = vector / np.linalg.norm(vector)
    return unit

ball_vector = unit_vector(np.random.normal(0, 1, 2))
ball_speed = 5
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
    

while True:
    scr = np.full((400,400,3),(255,255,255), dtype=np.uint8)
    cv2.circle(scr, ball_pos.astype(int), 3, (0,0,0))
    crash_detection()
    ball_pos += ball_vector*ball_speed
    cv2.imshow('geometry', scr)
    if cv2.waitKey(16) & 0xFF == 27:
        break
cv2.destroyAllWindows