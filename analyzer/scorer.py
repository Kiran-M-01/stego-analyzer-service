class ConfidenceScorer:

    @staticmethod
    def calculate(report: dict) -> dict:
        """
        Calculate an overall confidence score for the image.
        """

        entropies = []
        variances = []

        for channel in report.values():
            entropies.append(channel["entropy"])
            variances.append(channel["variance"])

        avg_entropy = sum(entropies) / 3
        avg_variance = sum(variances) / 3

        # Temporary heuristic
        confidence = 50.0

        if avg_entropy > 7:
            confidence += 20

        if avg_variance > 0.245:
            confidence += 15

        confidence = max(0, min(100, confidence))

        prediction = (
            "Likely Stego"
            if confidence >= 60
            else "Likely Clean"
        )

        return {
            "prediction": prediction,
            "confidence": round(confidence, 2),
            "average_entropy": round(avg_entropy, 4),
            "average_variance": round(avg_variance, 6),
        }