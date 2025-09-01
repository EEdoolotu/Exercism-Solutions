def translate(text):
    def translate_word(word: str) -> str:
        vowels = "aeiou"
        w = word

        # Rule 1: starts with vowel OR "xr"/"yt"
        if w[0].lower() in vowels or w.startswith(("xr", "yt")):
            return w + "ay"

        # Rule 3 (special case): leading "qu"
        if w[:2].lower() == "qu":
            return w[2:] + "quay"

        # Rules 2 & 3: move consonant cluster (bundle any trailing 'qu')
        for i, ch in enumerate(w):
            if ch.lower() in vowels:
                # If this vowel is 'u' and immediately preceded by 'q', treat 'qu' as consonant cluster
                if i > 0 and w[i-1:i+1].lower() == "qu":
                    i += 1  # include the 'u'
                return w[i:] + w[:i] + "ay"

        # Rule 4: treat 'y' as a vowel if we saw no a/e/i/o/u
        if "y" in w:
            j = w.lower().index("y")
            return w[j:] + w[:j] + "ay"

        # Fallback (rare: no vowels at all and no 'y')
        return w + "ay"

    return " ".join(translate_word(w) for w in text.split())
