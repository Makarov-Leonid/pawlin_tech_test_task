import csv


class CSVReader:
    @staticmethod
    def read(
            path
    ):
        with open(path) as csvfile:
            content = []
            reader = csv.reader(csvfile, delimiter=";")
            next(reader)
            for row in reader:
                content.append(
                    {
                        "farm": row[0],
                        "house": row[1],
                        "breed_type": row[2],
                        "gender": row[3],
                        "daynum": row[4],
                        "target_weight": row[5],
                    }
                )
        return content

    @staticmethod
    def check_structure_csv_with_chicken_post(path):
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            try:
                header = next(reader)
                if header == ['farm', 'house', 'breed_type', 'gender', 'daynum', 'target_weight']:
                    return True
                else:
                    return False
            except StopIteration:
                return False


if __name__ == "__main__":
    pass
