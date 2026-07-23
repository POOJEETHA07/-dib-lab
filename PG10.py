def text_analysis(paragraph):
    total_chars = len(paragraph)
    words = paragraph.split()
    total_words = len(words)
    sentences = [s for s in paragraph.split('.') if s.strip()]
    total_sentences = len(sentences)
    if total_words > 0:
        avg_word_length = total_chars / total_words
    else:
        avg_word_length = 0
    and_count = paragraph.lower().count("is")
    print("Text Analysis Report")
    print("==============")
    print(f"Total characters (including spaces and punctuation): {total_chars}")
    print(f"Total words: {total_words}")
    print(f"Total sentences: {total_sentences}")
    print(f"Average word length: {avg_word_length:.2f}")
    print(f"Occurrences of 'is': {and_count}")
if __name__ == "__main__":
    paragraph = """
    Education is the cornerstone of personal growth and societal progress.
    It empowers individuals with knowledge and skills essential for navigating
    the complexities of life. Beyond academics, education fosters critical thinking,
    creativity, and empathy, shaping individuals into informed and responsible global citizens.
    Accessible and quality education is pivotal in bridging socio-economic gaps and building a brighter, more inclusive future for generations to come.
    """
    text_analysis(paragraph)