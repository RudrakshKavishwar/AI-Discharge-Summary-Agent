from difflib import SequenceMatcher

def edit_score(draft, edited):

    similarity = SequenceMatcher(
        None,
        draft,
        edited
    ).ratio()

    return round(similarity * 100, 2)