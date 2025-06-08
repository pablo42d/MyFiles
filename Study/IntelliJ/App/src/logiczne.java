public class logiczne {
    public static void main(String[] args) {
//        boolean NOT
        int age = 17;
        boolean hasAccess = age >= 18; // <= mniejsz lub równy, != negacja(not), == równy,
        System.out.println(hasAccess);
        System.out.println("----------------------------");

        if (hasAccess) //!(zaprzeczenie wartości loicznej dla zmiennej)
             {
            System.out.println("Access granted");
        }
        else {
            System.out.println("Access denied");

        }


//        AND
        int cash = 50;
        int price = 40;

        int ageLimit = 18;
        int age1 = 18;
        boolean isOldEnough = age1 >= ageLimit;
        boolean hasEnoughtMoney = price <= cash;

        boolean canBuy = isOldEnough && hasEnoughtMoney;

        System.out.println(canBuy);
        System.out.println("----------------------------");

//        OR
        int cash1 = 50;
        int price2 = 40;

        boolean canPayWithCash = price <= cash;

        int creditCardAmount = 1000;
        boolean canPayWithCard = creditCardAmount >= price2;

//        ||=or
        boolean canBuy1 = canPayWithCard || canPayWithCash;{
            System.out.println(canBuy);
            System.out.println("----------------------------");
        }




    }
}
