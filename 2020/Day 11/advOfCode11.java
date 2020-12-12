import java.util.LinkedList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class advOfCode11 {
	public static void main(String[] args) throws FileNotFoundException{
		Scanner input = new Scanner(new File("advOfCode11.txt"));
		LinkedList<char[]> tmpInput = new LinkedList<>();
		while(input.hasNextLine()){
			tmpInput.add(input.nextLine().toCharArray());
		}
		input.close();
		char[][] layout = new char[tmpInput.size()][tmpInput.get(0).length];
		int i = 0;
		for(char[] cA : tmpInput){
			layout[i++] = cA;
		}
		Solver solver = new Solver(layout);
		System.out.println("Sol for part 1: "+solver.solve(false));
		solver.reset();
		System.out.println("Sol for part 2: "+solver.solve(true));


	}
	
}


class Solver{
	final private char[][] resetLayout;
	private char[][] RoomA;
	private char[][] RoomB;
	private char[][][] rooms;
	private int roomIndx = 0;
	final private int w;
	final private int h;
	private boolean part2;
	private int limit;
	Solver(char[][] layout){
		resetLayout = cloneLayout(layout);
		RoomA = cloneLayout(layout);
		RoomB = new char[layout.length][layout[0].length];
		rooms = new char[][][]{RoomA,RoomB};
		w = layout[0].length;
		h = layout.length;
	}
	public void reset(){
		RoomA = cloneLayout(resetLayout);
		RoomB = new char[h][w];
		rooms[0] = RoomA;
		rooms[1] = RoomB;
		roomIndx = 0;
	}
	private char[][] cloneLayout(char[][] layout){
		char[][] res = new char[layout.length][layout[0].length];
		for(int i = 0; i<layout.length;i++){
			for(int j = 0; j<layout[0].length; j++){
				res[i][j] = layout[i][j];
			}
		}
		return res;
	}

	public int solve(boolean part2){
		limit = part2? 5 : 4;
		this.part2 = part2;
		boolean anyChangeLastIter = true;
		char[][] currLayout = RoomA;
		char[][] nextLayout = RoomB;
		while(anyChangeLastIter){
			anyChangeLastIter = false;
			currLayout = rooms[roomIndx];
			roomIndx = (roomIndx+1)%2;
			nextLayout = rooms[roomIndx];
			for(int i = 0; i<h;i++){
				for(int j = 0; j<w;j++){
					anyChangeLastIter = applySeatRules(currLayout, nextLayout, i, j)? true : anyChangeLastIter;
				}
			}

		}
		

		return countOccupSeats(currLayout);
		
	}

	private void printLayout(char[][] layout){
		for(char[] cA :layout){
			for(char c : cA){
				System.out.print(c);
			}
			System.out.println();
		}
	}


	private int countOccupSeats(char[][] layout){
		int out = 0;
		for(int i = 0; i<h; i++){
			for(int j = 0; j<w; j++){
				if(layout[i][j] == '#') out++;
			}
		}
		return out;
	}

	private boolean applySeatRules(char[][] state, char[][] res, int i, int j){ // return true if anything changes
		char currPos = state[i][j];
		if(currPos=='.'){
			res[i][j] = currPos;
			return false; //do nothing on floor
		}
		int numOfOccupSeats = 0;
		int[][] directions = new int[][]{
			{0,1},{0,-1},{1,0},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}
		};
		for(int[] dirs : directions){
			numOfOccupSeats += visibOccup(i, j, dirs[0], dirs[1], state);
		}
		if(currPos == 'L'){
			if(numOfOccupSeats == 0){
				res[i][j] = '#';
				return true;
			}
			else{
				res[i][j] = 'L';
				return false;
			}
		}


		else if(currPos == '#'){
			if(numOfOccupSeats>=limit){
				res[i][j] = 'L';
				return true;
			}
			else{
				res[i][j] = '#';
				return false;
			}
		}
		else{
			System.out.println("WTF GOING ON HERE UNEXPECTED CHAR: "+currPos);
		}
		return false;
	}

	private int visibOccup(int i, int j, int di, int dj,char[][] layout){
		if(!part2){
			boolean indexCond = (i+di<h) && (i+di>=0) && (j+dj<w) && (j+dj>=0);
			return (indexCond && layout[i+di][j+dj]=='#') ? 1 :0;
		}
		else{
			while((i+di<h) && (i+di>=0) && (j+dj<w) && (j+dj>=0)){
				i+=di;
				j+=dj;
				if(layout[i][j] == '#'){
					return 1;
				}
				else if(layout[i][j]=='L'){
					return 0;
				}
			}
			return 0;
		}
	}
}