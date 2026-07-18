class PairGenerator:
    """
    Generates the 128 Pair-of-Values (PoV)
    used in the Chi-Square steganalysis attack.
    """

    @staticmethod
    def generate():
        """
        Returns:
            list[tuple]: [(0,1), (2,3), ..., (254,255)]
        """

        return [
            (i, i + 1)
            for i in range(0, 256, 2)
        ]