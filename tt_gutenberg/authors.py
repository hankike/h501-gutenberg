import pandas as pd


def list_authors(by_languages=False, alias=False):
    authors = pd.read_csv("gutenberg_authors.csv")
    metadata = pd.read_csv("gutenberg_metadata.csv")
    languages = pd.read_csv("gutenberg_languages.csv")

    data = metadata.merge(
        languages[["gutenberg_id", "total_languages"]],
        on="gutenberg_id"
    )

    data = data.merge(
        authors[["gutenberg_author_id", "alias"]],
        on="gutenberg_author_id"
    )

    if by_languages:
        data = (
            data.groupby(
                ["gutenberg_author_id", "alias"]
            )["total_languages"]
            .sum()
            .sort_values(ascending=False)
        )
    else:
        data = (
            data.groupby(
                ["gutenberg_author_id", "alias"]
            )
            .size()
            .sort_values(ascending=False)
        )

    if alias:
        return data.index.get_level_values("alias").tolist()

    return data.index.get_level_values("gutenberg_author_id").tolist()
