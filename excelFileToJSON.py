import csv, json

csvFilePath = "worksheet.csv"
jsonFilePath = "wrksht1.json"
#reading data, from csv file
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        Roll = csvRow['Roll']
        data[Roll]=csvRow
# writing JSON
with open('jsonFilePath','w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))











