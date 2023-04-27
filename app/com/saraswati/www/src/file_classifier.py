import pandas as pd


def get_file_size(file_information) -> int:
    df_file_information = create_data_frame(file_information)
    return df_file_information["file_size"].sum()


def create_data_frame(file_information):
    column_name = ["file_name", "file_size", "classifications"]
    df_file_information = pd.DataFrame(file_information, columns=column_name)
    return df_file_information


def get_top_classifications(file_stats, top_n_classification):
    df_file_information = create_data_frame(file_stats).explode("classifications").groupby("classifications").sum() \
        .reset_index().sort_values("file_size", ascending=False).head(top_n_classification)
    return df_file_information[["classifications", "file_size"]].values.tolist()
