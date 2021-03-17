# Read-only
def read_only():
    '''a method that only read the file'''
    try:
        file1 = open('data.txt','r') # read-only (by default(if you don't put anything) it is read-only)
        text = file1.read()
        print(text)
        file1.close()
    except FileNotFoundError:
        text = None
        print(text)

def write_only():
    '''a method that writes to a file'''
    file2 = open('more_data.txt','w') # write to the file, if file exist it would be overwritten, if it doesn't exist, it will be created
    file2.write('tomatoes')
    file2.close()

#another way of writing above function - in this one python will know to close it
with open('data.txt') as f:
    txt = f.read()
    print(txt)


def read_food_sales():
    all_dates=[]
    with open('sampledatafoodsales.csv') as f:
        # data = f.read()
        data = f.readlines()
        # print(data)

        for food_sale in data:
            split_food_sale = food_sale.split(',')
            order_date = split_food_sale[0]
            # print(order_date)
            all_dates.append(order_date)
    with open('data.txt', 'w') as f:
        for date in all_dates:
            f.write(date)
            f.write('\n')

def append_text():
    '''Apend data to an existing file'''
    with open('data.txt', 'a') as f:
        f.write('3/17/2021')
        print('done')

# 1
def foodsale_date_save():
    all_dates=[]
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
    with open('sampledatafoodsales.csv') as f:
        for food_sale in data:
            split_food_sale = food_sale.split(',')
            order_date = split_food_sale[0]
            all_dates.append(order_date)
        with open('dates.txt', 'w') as f:
            for date in all_dates:
                f.write(date)
                f.write('\n')
def foodsale_region_save():
    all_regions=[]
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
    with open('sampledatafoodsales.csv') as f:
        for food_sale in data:
            split_food_sale = food_sale.split(',')
            order_region = split_food_sale[1]
            all_regions.append(order_region)
        with open('regions.txt', 'w') as f:
            for region in all_regions:
                f.write(region)
                f.write('\n')

def foodsale_city_save():
    all_cities=[]
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
    with open('sampledatafoodsales.csv') as f:
        for food_sale in data:
            split_food_sale = food_sale.split(',')
            order_city = split_food_sale[2]
            all_cities.append(order_city)
        with open('cities.txt', 'w') as f:
            for city in all_cities:
                f.write(city)
                f.write('\n')

if __name__ == '__main__':
    # read_only()
    # write_only()
    # read_food_sales()
    # append_text()
    # foodsale_date_save()
    # foodsale_region_save()
    foodsale_city_save()