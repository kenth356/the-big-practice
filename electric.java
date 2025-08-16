import java.util.*;
import java.io.*;

class customersDC {
    String customerNAME, classiFICT;
    double totalKWU, ratePKU, groAMT, misceCHAR, totalAMT, prevREADING, currREADING;
    int meterID;
}

public class electric {
    static Scanner input = new Scanner(System.in);
    static List<customersDC> customersD = new ArrayList<>();
    public static void main(String[] args) {
        while (true) {
            int choice;
            System.out.println("\n[ELECTRIC COMPANY]");
            System.out.print("\n1. Calculate Bill");
            System.out.print("\n2. Visit Database");
            System.out.println("\n3. Exit");
            System.out.print("\nEnter: ");
            try {
                choice = Integer.parseInt(input.nextLine());
            } catch (NumberFormatException e) {
                choice = -1;
            }
            switch (choice) {
                case 1:
                elecCAL();
                break;
                case 2:
                dataBASE();
                break;
                case 3:
                exit();
                return;
                default:
                for (int i = 0; i < 3; i++) {
                    System.out.println("\n[PLEASE ENTER A VALID INPUT]");
                }
            }
        }
    }

    public static void elecCAL() {
        customersDC customers = new customersDC();
        System.out.println("\n[CALCULATE ELECTRIC BILL]");
        System.out.print("\nEnter Customer Name: ");
        customers.customerNAME = input.nextLine();
        System.out.print("\nEnter Meter ID: ");
        customers.meterID = input.nextInt();
        input.nextLine();
        System.out.print("\nEnter Classification: ");
        customers.classiFICT = input.nextLine();
        System.out.print("\nEnter Previous Reading: ");
        customers.prevREADING = input.nextDouble();
        System.out.print("\nEnter Current Reading: ");
        customers.currREADING = input.nextDouble();
        input.nextLine();
        //BRUH
        customers.totalKWU = customers.currREADING - customers.prevREADING;
        if (customers.classiFICT.equalsIgnoreCase("residential")) {
            if (customers.totalKWU > 300) {
                customers.misceCHAR = 0.8;
                customers.ratePKU = 0.55;
                customers.groAMT = customers.totalKWU * customers.ratePKU;
                customers.totalAMT = customers.groAMT + customers.misceCHAR;
                customersD.add(customers);
                SAVEDFILES();
                disPLAY();
            } else if (customers.totalKWU >= 100 && customers.totalKWU <= 299) {
                customers.misceCHAR = 0.5;
                customers.ratePKU = 0.55;
                customers.groAMT = customers.totalKWU * customers.ratePKU;
                customers.totalAMT = customers.groAMT + customers.misceCHAR;
                customersD.add(customers);
                SAVEDFILES();
                disPLAY();
            } else if (customers.totalKWU < 100) {
                customers.misceCHAR = 0;
                customers.ratePKU = 0.55;
                customers.groAMT = customers.totalKWU * customers.ratePKU;
                customers.totalAMT = customers.groAMT + customers.misceCHAR;
                customersD.add(customers);
                SAVEDFILES();
                disPLAY();
            }
        } else if (customers.classiFICT.equalsIgnoreCase("commercial")) {
            if (customers.totalKWU > 300) {
                customers.misceCHAR = 0.8;
                customers.ratePKU = 0.75;
                customers.groAMT = customers.totalKWU * customers.ratePKU;
                customers.totalAMT = customers.groAMT + customers.misceCHAR;
                customersD.add(customers);
                SAVEDFILES();
                disPLAY();
            } else if (customers.totalKWU >= 100 && customers.totalKWU <= 299) {
                customers.misceCHAR = 0.5;
                customers.ratePKU = 0.75;
                customers.groAMT = customers.totalKWU * customers.ratePKU;
                customers.totalAMT = customers.groAMT + customers.misceCHAR;
                customersD.add(customers);
                SAVEDFILES();
                disPLAY();
            } else if (customers.totalKWU < 100) {
                customers.misceCHAR = 0;
                customers.ratePKU = 0.75;
                customers.groAMT = customers.totalKWU * customers.ratePKU;
                customers.totalAMT = customers.groAMT + customers.misceCHAR;
                customersD.add(customers);
                SAVEDFILES();
                disPLAY();
            }
        }
    }

    public static void dataBASE() {
        try (BufferedReader reader = new BufferedReader(new FileReader("customers.txt"))) {
            String line;
            System.out.println("\n[CUSTOMERS' DATABASE]");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            for (int i = 0; i < 3; i++) {
                System.out.println("\nERROR");
            }
        }
    }

    public static void disPLAY() {
        for (customersDC customers : customersD) {
            System.out.println("Customer Name: " + customers.customerNAME);
            System.out.printf("Total Kilowatt Usage: %.2f kWh%n", customers.totalKWU);
            System.out.printf("Rate Per Kilowatt: %.2f kWh%n", customers.ratePKU);
            System.out.printf("Gross Amount: %.2f PHP%n", customers.groAMT);
            System.out.printf("Miscellaneous Charges: %.1f PHP%n", customers.misceCHAR);
            System.out.printf("Total Amount Due: %.2f PHP%n", customers.totalAMT);
        }
    }

    public static void exit() {
        System.out.println("\n[THANK YOU FOR USING!]");
    }

    public static void SAVEDFILES() {
        try (PrintWriter writer = new PrintWriter("customers.txt")) {
            for (customersDC customers : customersD) {
                writer.println("CUSTOMER NAME: " + customers.customerNAME);
                writer.println("METER ID: " + customers.meterID);
                writer.printf("PREVIOUS READING: %.2f kWh%n", customers.prevREADING);
                writer.printf("CURRENT READING: %.2f kWh%n", customers.currREADING);
                writer.printf("TOTAL KILOWATT USAGE: %.2f kWh%n", customers.totalKWU);
                writer.printf("RATE PER KILOWATT: %.2f kWh%n", customers.ratePKU);
                writer.printf("GROSS AMOUNT: %.2f PHP%n", customers.groAMT);
                writer.printf("MISCELLANEOUS CHARGES: %.1f PHP%n", customers.misceCHAR);
                writer.printf("TOTAL AMOUNT DUE: %.2f PHP%n", customers.totalAMT);
            }
        } catch (IOException e) {
            for (int i = 0; i < 3; i++) {
                System.out.println("[ERROR]");
            }
        }
    }
}