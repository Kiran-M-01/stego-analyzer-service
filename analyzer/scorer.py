class ConfidenceScorer:

    @staticmethod
    def calculate(report: dict) -> dict:
        """
        Calculate an overall confidence score for the image.

        BUG FIX: the previous version never read channel["chi_square"] at
        all -- the entire chi-square attack was computed and discarded.
        It also used two binary thresholds (avg_entropy > 7,
        avg_variance > 0.245), which meant there were only ever 4
        possible confidence values (50/65/70/85) for ANY image. That's
        why clean and embedded versions of the same image, or unrelated
        images, kept landing on identical scores.

        This version is a continuous weighted blend of all three
        signals, with chi-square (the most targeted, sensitive signal)
        weighted highest.
        """

        entropies = []
        variances = []
        chi_p_values = []

        for channel in report.values():
            entropies.append(channel["entropy"])
            variances.append(channel["variance"])
            chi_p_values.append(channel["chi_square"]["p_value"])

        avg_entropy = sum(entropies) / len(entropies)
        avg_variance = sum(variances) / len(variances)

        # Use the strongest channel/window result, not the average --
        # embedding usually targets one channel (often blue) and a
        # localized region, so averaging across channels would dilute
        # a real detection back down.
        max_chi_p = max(chi_p_values)

        # Normalize each raw signal into a 0-1 "suspicion score".
        chi_score = max_chi_p  # already 0-1 and IS the primary evidence

        # Full-channel entropy for a real photo typically sits ~6.5-7.5;
        # embedding pushes it higher. Map that range onto 0-1.
        entropy_score = min(max(avg_entropy - 6.5, 0.0) / 1.5, 1.0)

        # LSB-plane variance maxes out at 0.25 (perfectly balanced bits).
        # Natural images often already sit close to that, so this is a
        # weak signal on its own -- kept as a small supporting weight.
        variance_score = min(max(avg_variance - 0.20, 0.0) / 0.05, 1.0)

        confidence = (
            0.70 * chi_score +
            0.20 * entropy_score +
            0.10 * variance_score
        ) * 100

        confidence = max(0.0, min(100.0, confidence))

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
            "max_chi_square_p_value": round(max_chi_p, 4),
        }
