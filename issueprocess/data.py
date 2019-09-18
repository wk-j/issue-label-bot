def loaddata(foldername):
    import logging
    logging.getLogger().setLevel(logging.INFO)
    DataTitle = []
    DataDescription = []
    DataLabel = []
    import csv
    import os
    for filename in os.listdir(foldername):
        if filename.endswith(".csv"):
            with open(os.path.join(foldername+"/", filename), mode='r') as csv_file:
                logging.info(filename)
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    DataTitle.append(row["Title"])
                    DataDescription.append(row["Description"])
                    DataLabel.append(row["Label"])
                    line_count += 1
                logging.info(f'Processed {line_count} lines.')
    return DataTitle,DataDescription,DataLabel
    