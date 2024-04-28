import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class HotelBookingServer extends UnicastRemoteObject implements HotelBooking {
    private Map<Integer, String> bookings;

    public HotelBookingServer() throws RemoteException {
        bookings = new HashMap<>();
    }

    @Override
    public synchronized boolean bookRoom(String guestName, int roomNumber) throws RemoteException {
        if (bookings.containsKey(roomNumber)) {
            return false; // Room already booked
        }
        bookings.put(roomNumber, guestName);
        return true; // Room booked successfully
    }

    @Override
    public synchronized boolean cancelBooking(String guestName) throws RemoteException {
        for (Map.Entry<Integer, String> entry : bookings.entrySet()) {
            if (entry.getValue().equals(guestName)) {
                bookings.remove(entry.getKey());
                return true; // Booking canceled
            }
        }
        return false; // Guest not found in bookings
    }

    public static void main(String[] args) {
        try {
            HotelBooking server = new HotelBookingServer();
            java.rmi.registry.LocateRegistry.createRegistry(1099);
            java.rmi.Naming.rebind("rmi://localhost/HotelBookingService", server);
            System.out.println("Server running...");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
