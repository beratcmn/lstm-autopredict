# load data.txt and remove the duplicate lines
# save the cleaned data to data_cleaned.txt


def clean_data():
    with open("data.txt", "r") as f:
        lines = f.readlines()
    lines = list(set(lines))
    with open("data_cleaned.txt", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    clean_data()
    print("Data cleaned successfully!")
    print("data_cleaned.txt saved successfully!")
