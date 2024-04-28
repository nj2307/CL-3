import java.rmi.Naming;
import java.util.Scanner;

public class HotelBookingClient {
    public static void main(String[] args) {
        try {
            HotelBooking bookingService = (HotelBooking) Naming.lookup("rmi://localhost/HotelBookingService");
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter 'B' to book a room or 'C' to cancel booking: ");
            String choice = scanner.nextLine().toUpperCase();

            if (choice.equals("B")) {
                System.out.print("Enter guest name: ");
                String guestName = scanner.nextLine();
                System.out.print("Enter room number: ");
                int roomNumber = scanner.nextInt();

                boolean booked = bookingService.bookRoom(guestName, roomNumber);
                System.out.println("Room booked: " + booked);
            } else if (choice.equals("C")) {
                System.out.print("Enter guest name to cancel booking: ");
                String guestName = scanner.nextLine();

                boolean canceled = bookingService.cancelBooking(guestName);
                System.out.println("Booking canceled: " + canceled);
            } else {
                System.out.println("Invalid choice.");
            }

            scanner.close();
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
