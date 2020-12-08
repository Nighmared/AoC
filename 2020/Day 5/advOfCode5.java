import java.util.Scanner;
import java.io.File;

public class advOfCode5 {
	public static void main(String[] args) {
		Scanner input;
		try {
			input = new Scanner(new File("advOfCode5.txt"));
		} catch (Exception e) {
			System.out.println("nope");
			return;
		}
		char[] currLine;
		int lowerRow, upperRow, midRow, lowerSeat, upperSeat, midSeat, seatID;
		int maxSeatID = 0;
		int minSeatID = 127*8 + 8;
		boolean[] seats = new boolean[1024];

		while (input.hasNextLine()) {
			lowerRow = 0;
			upperRow = 127;
			lowerSeat = 0;
			upperSeat = 7;
			currLine = input.nextLine().toCharArray();
			for(int i = 0; i<7; i++){
				midRow = (lowerRow+upperRow)/2;
				if(currLine[i] == 'F'){
					upperRow = midRow;
					//System.out.println("front half: "+lowerRow+" - "+upperRow);
				}
				else{
					lowerRow = midRow+1;
					//System.out.println("back half: "+lowerRow+" - "+upperRow);
				}
			}
			for(int i = 7; i<10; i++){
				midSeat = (lowerSeat + upperSeat)/2;
				if(currLine[i] == 'L'){
					upperSeat = midSeat;
				}
				else{
					lowerSeat = midSeat+1;
				}
			}
			if(lowerRow != upperRow || lowerSeat != upperSeat){
				System.out.println(lowerRow+" "+upperRow+" | "+lowerSeat+" "+upperSeat);
				throw new IllegalStateException("whut");
			}
			seatID = lowerRow*8 + lowerSeat;
			seats[seatID] = true;
			maxSeatID = Math.max(maxSeatID,seatID);
			minSeatID = Math.min(minSeatID,seatID);
		}

		System.out.println("Highest seat ID: "+ maxSeatID);
		for(int i = minSeatID+1; i< maxSeatID; i++){
			if(seats[i]) continue;
			if(seats[i-1] && seats[i+1]){
				System.out.println("Found my Seat! It's ID is "+ i);
				break;
			}
		}


	}
}