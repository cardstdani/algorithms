import java.util.*;

public class RecursiveLinearSearch {

  public static int RecursiveLinSearch(List<Integer> l, int target, int index) {
    if (index >= l.size()) {
      return -1;
    }
    if (target == l.get(index)) {
      return index;
    }

    return RecursiveLinSearch(l, target, index + 1);
  }

  public static void main(String args[]) {
    List<Integer> l = new ArrayList<Integer>();

    int r = (int) (Math.random() * (40));
    int target = (int) (Math.random() * (r - 1));
    for (int i = 0; i < r; i++) {
      l.add(i);
    }
    System.out.println(l);
    System.out.println("Target: " + target + " at position: " + RecursiveLinSearch(l, target, 0));
  }
}
