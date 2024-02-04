import os
from argparse import ArgumentParser

from db.queries.chicken_post_queries import (
    insert_chicken_post_from_csv,
)
from files.csv_reader import CSVReader
from files.csv_writer import CSVWriter


def is_valid_file(parser, arg):
    if arg.split(".")[-1] != "csv":
        parser.error(f"The file {arg} is not csv!")
    if not CSVReader.check_structure_csv_with_chicken_post(arg):
        parser.error(f"The csv file on the {arg} path has an unsupported structure!")
    return arg


def upload_csv_to_db(path):
    data = CSVReader.read(path)
    insert_chicken_post_from_csv(data)


def create_csv_from_db_data(path):
    CSVWriter.create_csv_with_chicken_posts_from_db(path)


def cli():
    parser = ArgumentParser(description="Upload files to database")
    parser.add_argument(
        "--download", action="store_true", help="Download csv with all in db data."
    )
    parser.add_argument(
        "-f",
        dest="filename",
        required=True,
        type=lambda x: is_valid_file(parser, x),
    )

    args = parser.parse_args()

    if args.download:
        action = create_csv_from_db_data
    else:
        action = upload_csv_to_db

    action(args.filename)


if __name__ == "__main__":
    cli()
