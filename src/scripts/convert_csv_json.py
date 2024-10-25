import csv
import json
import os


if __name__ == '__main__':
    hotel_data_csv = os.path.join(os.getcwd(), 'source_data', 'hotel_data_provider.csv')
    data_json = os.path.join(os.getcwd(), 'source_data', 'data.json')

    with open(hotel_data_csv, mode ='r')as file:
        csvFile = csv.reader(file)

        csv_data = []

        for index, lines in enumerate(csvFile):
            if index > 0:
                csv_data.append(dict(
                    model="genie_app.hotelroom",
                    pk=index,
                    fields=dict(
                        id=lines[2],
                        room_id=lines[0],
                        night_of_stay=lines[1],
                        rpg_status=lines[3],
                        timestamp=lines[4],
                        hotel_id=lines[5]
                    )
                ))

        json_object = json.dumps(csv_data, indent=4)

        with open(data_json, "w") as outfile:
            outfile.write(json_object)
