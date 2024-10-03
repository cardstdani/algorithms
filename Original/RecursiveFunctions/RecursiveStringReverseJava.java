public class Main {
	public static void main(String[] args) {
		System.out.println(reverse("Hello World"));
	}
	
	public static String reverse(String s){
	    if(s.length() <= 1){
	        return s;
	    }
	    return reverse(s.substring(1)) + s.charAt(0);
	}
}
