import csv

from db.queries.chicken_post_queries import select_chicken_posts


class CSVWriter:
    @staticmethod
    def create_csv_with_chicken_posts_from_db(path):
        chicken_posts = select_chicken_posts()
        with open(path, "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(
                ["farm", "house", "breed_type", "gender", "daynum", "target_weight"]
            )
            for post in chicken_posts:
                writer.writerow(
                    [
                        post.farm.name,
                        post.house.name,
                        post.breed_type.name,
                        post.gender.name,
                        post.daynum,
                        post.target_weight,
                    ]
                )


if __name__ == "__main__":
    CSVWriter.create_csv_with_chicken_posts("sw_data_new.csv")
