class ConfidenceScorer:

    @staticmethod
    def calculate(report: dict) -> dict:

        entropies = []
        variances = []
        chi_p_values = []

        for channel in report.values():
            entropies.append(channel["entropy"])
            variances.append(channel["variance"])
            chi_p_values.append(channel["chi_square"]["p_value"])

        avg_entropy = sum(entropies) / len(entropies)
        avg_variance = sum(variances) / len(variances)

        # Strongest chi-square signal
        max_chi_p = max(chi_p_values)

        # ----------------------------
        # Normalize scores (0-1)
        # ----------------------------

        chi_score = max_chi_p

        # LSB entropy normalization
        entropy_score = min(
            max((avg_entropy - 0.15) / 0.65, 0.0),
            1.0
        )

        # LSB variance normalization
        variance_score = min(
            max((avg_variance - 0.02) / 0.18, 0.0),
            1.0
        )

        # ----------------------------
        # Weighted confidence
        # ----------------------------

        confidence = (
            0.50 * chi_score +
            0.30 * entropy_score +
            0.20 * variance_score
        ) * 100

        confidence = round(
            max(0.0, min(confidence, 100.0)),
            2
        )

        # ----------------------------
        # Prediction
        # ----------------------------

        if confidence >= 75:
            prediction = "Likely Stego"

        elif confidence >= 45:
            prediction = "Suspicious"

        else:
            prediction = "Likely Clean"

        # ----------------------------
        # Return result
        # ----------------------------

        return {
            "prediction": prediction,
            "confidence": confidence,
            "average_entropy": round(avg_entropy, 4),
            "average_variance": round(avg_variance, 6),
            "max_chi_square_p_value": round(max_chi_p, 4)
        }