

class coord_handler:
    def __init__(self, start_pick_position: list  , number_pick_positions :int , start_set_position :list , number_set_position : int):
       
       
        self.pick_start_position = start_pick_position
        self.set_start_position = start_set_position
        self.pick_positions = self._get_pick_positions()
        self.set_positions = self._get_set_positions()

    def _get_pick_positions(self):
        ## do the pick position code here
        ## this should be an array of number_pick_positions (each element is a 6 element list) with all those on the LEFT as even indexes
        pick_positions = []
        pos1 = []
        pick_positions.append(self.pick_start_position)

        for i in range(6):
            # determine vial pick slots based on start pick position


            # append pick positions
            pick_positions.append(pos1)
        return pick_positions
    
    def _get_set_positions(self):
        ## do the set position code here
        ## this should be an array of number_set_positions (each element is a 6 element list) with the set positions
        set_positions = []
        pos2 = []
        set_positions.append(self.set_start_position)

        for i in range(3):
            # determine vial set slots based on start set position

            # append set positions
            set_positions.append(pos2)
        return set_positions
