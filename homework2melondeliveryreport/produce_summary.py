def main():


    def print_report(day):

        # Day 1
        print "Day %d" % day
        if day == 1:
            my_file = open("um-deliveries-20140519.csv")
        elif day == 2:
            my_file = open("um-deliveries-20140520.csv")
        elif day == 3:
            my_file = open("um-deliveries-20140521.csv")

        for line in my_file:
            line = line.rstrip()
            words = line.split(',')
            
            melon = words[0]
            count = words[1]
            amount = words[2]
            
            print "Delivered %s %ss for a total of: $%s" % (count, melon, amount)
        my_file.close()
        print "\n",

    day = int(raw_input('What day would you like to print: 1, 2, or 3? > '))

    print_report(day)



if __name__ == "__main__":
    main()