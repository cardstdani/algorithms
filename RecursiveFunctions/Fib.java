import java.util.*;

public class Fib {

  public static Integer fibMem(int n, HashMap<Integer, Integer> mem) {
    if (n <= 1) {
      return 1;
    }

    if (mem.containsKey(n)) {
      return mem.get(n);
    }

    mem.put(n, fibMem(n - 1, mem) + fibMem(n - 2, mem));
    return mem.get(n);
  }

  public static int fib(int n) {
    if (n <= 1) {
      return 1;
    }
    return fib(n - 1) + fib(n - 2);
  }

  public static void main(String args[]) {
    System.out.println(fib(8));
    System.out.println(fibMem(40, new HashMap<Integer, Integer>()));
  }
}
