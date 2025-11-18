from transformers import pipeline


class SpamDetector:
    def __init__(self, model_name: str = "Goodmotion/spam-mail-classifier"):
        self.pipe = pipeline("text-classification", model=model_name)
        self.label_map = {"LABEL_0": False, "LABEL_1": True}

    def is_spam(self, text: str) -> tuple[bool, int]:
        result = self.pipe(text)[0]
        return self.label_map[result["label"]], result["score"]


# Example usage:
if __name__ == "__main__":
    detector = SpamDetector()
    sample_text = "Congratulations! You've won a free lottery ticket. Click here to claim your prize."
    result = detector.is_spam(sample_text)
    print(f"Text: {sample_text}\nSpam Detection Result: {result}")
