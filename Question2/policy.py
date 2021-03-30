
import random as ran
OUT_OF_BOUNDS = -1
EMPTY = 0
START = 1
CURRENT = 2
END = 3
#MIN = 0
#MAX = 10


def valid(i, j, map_array):
    """
    Static class function, designed to determine if a new position is valid
    Args:
        i(int): x-coordinate
        j(int): y-coordinate
        map_array(numpy array 2D): Map of current field

    Return:
        True if valid position to move to
    """
    rows = map_array.shape[0]
    cols = map_array.shape[1]
    if i < 0 or i >= rows:
        return False
    if j < 0 or j >= cols:
        return False
    if map_array[i, j] == START or map_array[i, j] == OUT_OF_BOUNDS or map_array[i, j] == CURRENT:
        return False
    return True


def update_pr(up1, outcome: bool):
    """
        Static class function, designed to update Adjusters on probabilities for actions
        Args:
            up1(int): Current adjuster to be updated
            outcome(bool): Decision of good outcome a bad outcome from the last action

        Return:
            up1(int): updatedadjuster
        """
    if outcome:
        up1 = up1 + 1
    else:
        up1 = up1 - 1
    return up1


class Policy:
    """
    Policy class A current state is entered into the class with the map,
     then an action is made and updated map is returned. Probabilities of actions can vary over time.
    """
    def __init__(self):
        self.p1 = 1
        self.p2 = 90
        self.p2r = 5
        self.p3 = 101
        self.p3r = 5
        self.p4 = 190
        self.p4r = 5
        self.p5 = 201
        self.p5r = 5
        self.p6 = 290
        self.p6r = 5
        self.p7 = 301
        self.p7r = 5
        self.p8 = 390
        self.p8r = 5
        self.p9 = 590
        self.p9r = 5
        self.num = 0

    def new_policy(self, i, j, map_array):
        """
        This function is meant to determine a new action to be taken
        :param i: X-coordinate
        :param j: Y-coordinate
        :param map_array: Current map of the field
        :return: Returns new x-coordinate, y-coordinate, and updated map
        """
        v = True
        end = self.p9 + self.p9r + 1
        while v:
            new_i, new_j = i, j
            rand = ran.randrange(1, end, 1)
            if self.p1 < rand <= self.p2 + self.p2r:
                self.num = 1
                new_i = new_i + 1
            elif self.p2 - self.p2r < rand <= self.p3 + self.p3r:
                self.num = 2
                new_i = new_i - 1
            if self.p3 - self.p3r < rand <= self.p4 + self.p4r:
                self.num = 3
                new_j = new_j + 1
            elif self.p4 - self.p4r < rand <= self.p5 + self.p5r:
                self.num = 4
                new_j = new_j - 1
            if self.p5 - self.p5r < rand <= self.p6 + self.p6r:
                self.num = 5
                new_i = new_i + 1
                new_j = new_j + 1
            elif self.p6 - self.p6r < rand <= self.p7 + self.p7r:
                self.num = 6
                new_i = new_i + 1
                new_j = new_j - 1
            if self.p7 - self.p7r < rand <= self.p8 + self.p8r:
                self.num = 7
                new_i = new_i - 1
                new_j = new_j + 1
            elif self.p8 - self.p8r < rand <= self.p9 + self.p9r:
                self.num = 8
                new_i = new_i - 1
                new_j = new_j - 1
            if valid(new_i, new_j, map_array):
                v = False
                map_array[new_i, new_j] = CURRENT
                map_array[i, j] = EMPTY
                # print("rand", rand)
                # print("i, j, old", i, j, map_array[i, j])
                # print("i, j, new", new_i, new_j, map_array[new_i, new_j])
        return new_i, new_j, map_array

    def update_policy(self, outcome: bool):
        """
        This function determines what probability adjuster needs to be updated.
        :param outcome: Was the last action provided good or bad i.e. true or false
        """
        if self.num == 1:# and MIN <= self.p2r <= MAX:
            self.p2r = update_pr(up1=self.p2r, outcome=outcome)
           # print(self.p2r)
        elif self.num == 2:# and MIN <= self.p3r <= MAX:
            self.p3r = update_pr(up1=self.p3r, outcome=outcome)
            #print(self.p3r)
        if self.num == 3:# and MIN <= self.p4r <= MAX:
            self.p4r = update_pr(up1=self.p4r, outcome=outcome)
            #print(self.p4r)
        elif self.num == 4:# and MIN <= self.p5r <= MAX:
            self.p5r = update_pr(up1=self.p5r, outcome=outcome)
            #print(self.p5r)
        if self.num == 5:# and MIN <= self.p6r <= MAX:
            self.p6r = update_pr(up1=self.p6r, outcome=outcome)
            #print(self.p6r)
        elif self.num == 6:# and MIN <= self.p7r <= MAX:
            self.p7r = update_pr(up1=self.p7r, outcome=outcome)
            #print(self.p7r)
        if self.num == 7:# and MIN <= self.p8r <= MAX:
            self.p8r = update_pr(up1=self.p8r, outcome=outcome)
            #print(self.p8r)
        elif self.num == 8:# and MIN <= self.p9r <= MAX:
            self.p9r = update_pr(up1=self.p9r, outcome=outcome)
            #print(self.p9r)
        self.num = 0

            


