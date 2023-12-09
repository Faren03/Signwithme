import pygame
import sys
import math

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

WHITE = (255, 255, 255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Customizable Animated Avatar")

# Character state
x_position = 200
y_position = 150
initial_hand_angle = 0  # Start the arm at the side
hand_angle = initial_hand_angle
vertical_oscillation = 20  # Increase the vertical movement for a more noticeable effect
vertical_motion_direction = 1  # 1 for upward motion, -1 for downward motion
vertical_motion_speed = 2  # Adjust the speed of the vertical motion


def draw_character(head_color, body_color, hand_color):
  
    screen.fill(WHITE)

    
    pygame.draw.circle(screen, head_color, (x_position, y_position), 30)


    pygame.draw.rect(screen, body_color, (x_position - 15, y_position + 30, 30, 50))

    
    vertical_motion = vertical_oscillation * math.sin(math.radians(hand_angle))

  
    arm_length = 30
    arm_end = rotate_point(x_position, y_position + 30, hand_angle, arm_length)
    arm_end = (arm_end[0], arm_end[1] + vertical_motion)  # Adjust the vertical position of the arm end
    pygame.draw.line(screen, body_color, (x_position, y_position + 30), arm_end, 10)

    
    pygame.draw.circle(screen, hand_color, arm_end, 8)

   
    pygame.display.flip()


def rotate_point(x, y, angle, distance):
    radian_angle = math.radians(angle)
    new_x = x + distance * math.cos(radian_angle)
    new_y = y + distance * math.sin(radian_angle)
    return int(new_x), int(new_y)


def get_user_customization():
    head_color = tuple(map(int, input("Enter head color (R G B): ").split()))
    body_color = tuple(map(int, input("Enter body color (R G B): ").split()))
    hand_color = tuple(map(int, input("Enter hand color (R G B): ").split()))

    return head_color, body_color, hand_color


try:
    head_color, body_color, hand_color = get_user_customization()
except ValueError:
    print("Invalid input. Please enter three integers separated by spaces for each color.")
    sys.exit()

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

  
    hand_angle += 2  # Adjust the speed of the wave

  
    if hand_angle >= initial_hand_angle + 45 or hand_angle <= initial_hand_angle - 45:
        vertical_motion_direction *= -1

    
    vertical_oscillation += vertical_motion_direction * vertical_motion_speed

    draw_character(head_color, body_color, hand_color)

    pygame.time.delay(50)
