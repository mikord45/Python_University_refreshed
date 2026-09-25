import csv
import random
import webbrowser
import statistics

csv_path = 'legoSets.csv'

def readDataFromCsV(year_to_search):
    number_of_sets = 0
    numbers_of_elements_per_set = []

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            current_year = int(row['year'])
            if current_year == year_to_search:
                number_of_sets += 1
                numbers_of_elements_per_set.append(int(row['num_parts']))

    return number_of_sets, numbers_of_elements_per_set

def main():
    year_from = 1949
    year_to = 2024

    try:
        year_to_search = int(input("Podaj rocznik od 1949 do 2024: "))
        if(year_to_search < year_from or year_to_search > year_to):
            print("Podano błędną wartość rocznika")
            return
    except:
        print("Podano błędną wartość rocznika")
        return

    number_of_sets, numbers_of_elements_per_set = readDataFromCsV(year_to_search)
    print(f'Rok {year_to_search}: Ilość zestawów = {number_of_sets}')

    if numbers_of_elements_per_set:
        avg_elements_number = statistics.mean(numbers_of_elements_per_set)
        median_elements_number = statistics.median(numbers_of_elements_per_set)
        print(f'\nŚrednia ilość elementów w zestawach: {avg_elements_number}')
        print(f'Mediana ilości elementów w zestawach: {median_elements_number}')

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            random_set = random.choice([row for row in reader if int(row['year']) == year_to_search])

        img_url = random_set['img_url']
        webbrowser.open(img_url)

if __name__ == '__main__':
    main()