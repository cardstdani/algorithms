public class Main{
	public static void main(String[] args) {
		System.out.println(decToBin(852, ""));
	}
	
	public static String decToBin(int dec, String r){
	    if(dec < 1){
	        return r;
	    }
	    return decToBin(dec/2, (dec%2) + r);
	}
}
