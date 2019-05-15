class Buttons():

    Label: str = None
    Action: str = None
    Prob: float = None

    def __init__(self, label: str, action: str, prob: float):
        self.Label = label
        self.Action = action   
        self.Prob = prob