
def revenue_per_melon():

    # create dictionary of melon sales, where melon_type is the key and the number
    # of melons sold is the value
    melon_tallies = {}
    f = open("orders_by_type.csv")
    for line in f:
        data = line.split(",")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] = melon_tallies.get(melon_type, 0) + melon_count
    f.close()

    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at $%0.2f each for a total of $%0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
    print "******************************************"

def sales_report_bifurcated():
    f = open("orders_with_sales.csv")
    sales = [0, 0]
    for line in f:
        data = line.split(",")
        if data[1] == "0":
            sales[0] += float(data[3])
        else:
            sales[1] += float(data[3])
    print "Salespeople generated $%0.2f in revenue." % sales[1]
    print "Internet sales generated $%0.2f in revenue." % sales[0]
    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"
    print "******************************************"


if __name__ == "__main__":
    report = raw_input("For a revenue per melon sales report, enter 1.\nFor a report that shows online vs. personal sales, enter 2. >")
    if report == "1":
        revenue_per_melon()
    elif report == "2":
        sales_report_bifurcated()
    else:
        print "That was an invalid entry. Please run the script and try again."



