public class instrukcjaWarunkowa {
    public static void main(String[] args) {

//  if (warunek) {
//   ciało_instrukcji
//}

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

        System.out.println(getDriverLicense(16));
        System.out.println(GetDriverlicense(13));

        System.out.println(calculateTaxes(10001));

        System.out.println(getTipsRating(51));
    }
//------------------------------------------------------------------------
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
//------------------------------------------------------------------------------

    public static String getDriverLicense(int age) {
        if (age < 16) {
            return "You can't get a license";
        }
            return "You can get a license";

    }
// ----------------------- inny ---------------------------------------------------

    public static String GetDriverlicense(int age) {
        if (age >= 16) {
            return "You can get a license";
        } else {
            return "You can't get a license";
        }
    }

    public static double calculateTaxes(double income) {

        if (income <= 1000) {
            return income * 0.02;
        }
        if (income >=1001 && income <= 10000) {
            return income * 0.03;
        }
        return income * 0.05;

    }

    public static String getTipsRating(int amount) {
        if (amount == 0) {
            return "terrible";
        }
        if (amount <= 10) {
            return "poor";
        }
        if (amount > 10 && amount <= 20) {
            return "good";
        }
        if (amount > 20 && amount <= 50) {
            return "great";
        }
        return "excellent";

    }

}