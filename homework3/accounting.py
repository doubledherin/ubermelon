
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
    revenue_per_melon()
    sales_report_bifurcated()



"""
We sold 4795 Musk melons at $1.15 each for a total of $5514.25
We sold 34982 Watermelon melons at $1.75 each for a total of $61218.50
We sold 1928 Hybrid melons at $1.30 each for a total of $2506.40
We sold 841 Winter melons at $4.00 each for a total of $3364.00
******************************************
Salespeople generated $206266.50 in revenue.
Internet sales generated $108440.29 in revenue.
Guess there's some value to those salespeople after all.
******************************************
"""
