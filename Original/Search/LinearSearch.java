import java.util.*;

public class LinearSearch {
  
  public static int LinSearch(List<Integer> l, int target) {
    for (int i = 0; i < l.size(); i++) {
      if (target == l.get(i)) {
        return i;
      }
    }
    return -1;
  }

  public static void main(String args[]) {
    List<Integer> l = new ArrayList<Integer>();

    int r = (int) (Math.random() * (40));
    int target = (int) (Math.random() * (r - 1));
    for (int i = 0; i < r; i++) {
      l.add(i);
    }
    System.out.println(l);
    System.out.println("Target: " + target + " at position: " + LinSearch(l, target));
  }
}
