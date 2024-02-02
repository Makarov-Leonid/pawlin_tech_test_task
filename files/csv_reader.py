import csv


class CSVReader:
    @staticmethod
    def read(
        path,
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


if __name__ == "__main__":
    pass
