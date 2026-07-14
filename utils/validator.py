REQUIRED_COLUMNS = ["name","handle","platform","followers","bio","recent_posts"]

def validate_frames(done):
    missing_columns = []

    for column in REQUIRED_COLUMNS:
        if column not in done.columns:
            missing_columns.append(column)

        if missing_columns:
            return False, missing_columns

    return True, None