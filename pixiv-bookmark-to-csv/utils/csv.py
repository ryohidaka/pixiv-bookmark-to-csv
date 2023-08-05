import csv
import os


# Define the CSV headers
headers = ["id", "title", "custom_tags", "type", "user_id", "user_name"]


def output(self, csv_file, data):
    """
    Write a list to a CSV file.

    Parameters
    ----------
    csv_file: str
        The name of the CSV file.
    data: list
        The list of data to write.
    """

    with open_csv_file_with_write_mode(self, csv_file) as file:
        write_to_csv(self, file, data)


def open_csv_file_with_write_mode(self, csv_file):
    """
    Open a CSV file in write mode.

    Parameters
    ----------
    csv_file: str
        The name of the CSV file.
    """

    self.logger.info("[Start] Opening CSV file in write mode")

    # Check if the file exists.
    if not os.path.exists(csv_file):
        # Create a new file if it does not exist.
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)  # Write the header row.

    # Open the file in write mode.
    file = open(csv_file, "a", newline="")

    # Check if the file is empty.
    if file.tell() == 0:
        # Write the header row if the file is empty.
        writer = csv.writer(file)
        writer.writerow(headers)  # Write the header row.

    self.logger.info("[End] Opening CSV file in write mode")

    return file


def write_to_csv(self, file, data):
    """
    Write a list to a CSV file.

    Parameters
    ----------
    file: file
        The file to write to.
    data: list
        The list of data to write.
    """

    self.logger.info("[Start] Writing to CSV file")

    # Check if the mode is "all".
    if self.mode == "all":
        self.logger.info(f"Reset: {file.name}")
        # Overwrite the file.
        file.truncate(0)
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

    # Create a CSV writer.
    writer = csv.DictWriter(file, fieldnames=headers)

    # Write the data to the file in reverse order.
    for row in reversed(data):
        writer.writerow(row)

    self.logger.info("[End] Writing to CSV file")


def get_last_id(self, csv_file) -> int:
    """
    Get the last ID from a CSV file.

    Parameters
    ----------
    csv_file: str
        The name of the CSV file.
    """

    try:
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) > 1:
                last_row = rows[-1]
                last_id = int(last_row[0])

                file.close()
            else:
                last_id = None

    except FileNotFoundError:
        last_id = None

    self.logger.info(f"Last ID: {last_id}")

    return last_id
