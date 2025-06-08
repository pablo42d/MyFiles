public class ternarOperator {
    public static void main(String[] args) {


        int age = 16;
        String messageTernar = age >= 18 ? "Adult" : "Child";

        System.out.println(messageTernar);


//        ---------------------------------------------

        String message;
        if (age >= 18) {
            message = "Adult";
        }
        else {
            message = "Child";
        }

        System.out.println(message);
    }

}
