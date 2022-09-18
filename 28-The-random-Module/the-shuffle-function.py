import random

dental_health_kit = ["toothbrush", "floss", "mouthwash"]
print(dental_health_kit)

clone = dental_health_kit[:]
#clone = dental_health_kit.copy()
random.shuffle(clone)
print(clone)