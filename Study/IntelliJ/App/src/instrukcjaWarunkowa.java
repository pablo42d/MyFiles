public class instrukcjaWarunkowa {
    public static void main(String[] args) {
        int x = 10;

        if (x < 2) {

            System.out.println(1);
            System.out.println(2);
            System.out.println(3);
        }
        System.out.println(x);

//------------------------------------------------------------------------------
        int age = 13;

        if (age >= 18) {
            System.out.println("Adult more then " + age);
        } else if (age > 12) {
            System.out.println("Teenager");
        } else {
            System.out.println("To young");
        }
//-----------------------------------------------------------------------------

        int shortTermCost = 50; //day 1-3
        int midTermCost = 40; //day 4-7
        int longTermCost = 30; //8+


        int twoDaysPrice = getRentalPrice(2);
        int fiveDaysPrice = getRentalPrice(5);
        int tenDaysPrice = getRentalPrice(10);



        System.out.println(twoDaysPrice);
        System.out.println(fiveDaysPrice);
        System.out.println(tenDaysPrice);


    }

    public static int getRentalPrice(int days) {
        if (days <3) {
            return days * 50;
//            return; days * shortTermCost;
        }
        if (days < 7) {
            int midTermCost = days - 3;
            return 3 * 50 + midTermCost *40;
        }
        int longTermPriceDays = days -7;
        return 3 * 50 + 4 * 40 + longTermPriceDays *30;

    }
}