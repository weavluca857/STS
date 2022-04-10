
class paddleAI:
    pos = 0
    traj = 0
    def __init__(self):
        self.pos = 0
        self.ball_pos = (0, 0)
        self.traj = 0

    def update(self, new_pos, ball_data):
        self.ball_pos = ball_data
        self.pos = new_pos

    def calc_new_pos(self):
        if self.ball_pos[0] > self.pos:
            self.traj = 1
        elif self.ball_pos[0] < self.pos:
            self.traj = -1
        else:
            self.traj = 0