//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
// Sygnatura metody
public class metody {
//    psvm
    public static void main(String[] args) {
//        rectangle 5x8
        int hight = 5;
        int width = 8;
        printRectInfo(hight, width); // wywołanie metody
        printRectInfo(12, 7); //wywołanie z jawnymi wartościami

//        return type
        String johnName = "John";
        String bobName = "Bob";
        String greetJohn = createGreetMessage(johnName);
        String greetBob = createGreetMessage(bobName);
        System.out.println(greetBob);
        System.out.println(greetJohn);
        System.out.println("___________________");

//        display default message
        sayHello();
        System.out.println("___________________");

//        Promień koła
        double radius = 10.0;
        double result = getCircleCircumference(radius);
        System.out.println(result);
        System.out.println("___________________");

    }


//  modifiers: public static
//  return type: void (nic nie zwraca) String, int, itd
//    method name: int
//    input params: int height, int width
//    body{....}
    public static void printRectInfo(int hight, int width) {
        int perimeter = hight * 2 + width *2;

            System.out.println("Restangle " + hight + " x " + width);
            System.out.println("Perimeter is " + perimeter);
            System.out.println("-------------------------------------------");
    }


    public static String createGreetMessage(String name) {
        String greet = "Hi " + name + " all good?";
        return greet;
    }

    public static void sayHello() {
        System.out.println("Hi there");
    }

    public static double getCircleCircumference(double radius) {
        double result = radius * radius*3.14;
        return result;


    }
}