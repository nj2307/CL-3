import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HotelBooking extends Remote {
    boolean bookRoom(String guestName, int roomNumber) throws RemoteException;
    boolean cancelBooking(String guestName) throws RemoteException;
}


// Commands to run this all codes:
// 1. javac HotelBooking.java HotelBookingServer.java HotelBookingClient.java
// 2. i) start rmiregistry
//    ii) java HotelBookingServer
// 3. java HotelBookingClient

