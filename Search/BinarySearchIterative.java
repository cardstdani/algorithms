import java.util.*;

public class BinarySearch {

  public static int BinSearch(List<Integer> l, int target) {
    int start = 0;
    int mid = 0;
    int end = l.size() - 1;

    while (start <= end) {
      mid = (int) ((end + start) / 2);
      if (target == l.get(mid)) {
        return mid;
      } else if ((end - start) <= 1) {
        return -1;
      } else if (target < l.get(mid)) {
        end = mid;
      } else if (target > l.get(mid)) {
        start = mid;
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
    System.out.println("Target: " + target + " at position: " + BinSearch(l, target));
  }
}
