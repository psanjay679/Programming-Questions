import java.lang.reflect.Array;
import java.util.*;

class Sample {

    int binSearch(ArrayList<Integer> ar, int val) {
        int low = 0;
        int high = ar.size();
        int mid;

        while (low <= high) {
            mid = (low + high) / 2;
            if (ar.get(mid) < val) {
                low = mid + 1;
            } else if (ar.get(mid) > val) {
                high = mid - 1;
            }
            return mid;
        }

        return -1;
    }

    public static void main(String[] args) {
        int n = 3;

        ArrayList<ArrayList<Integer>> ar = new ArrayList<ArrayList<Integer>>(n);

        for (int i = 0; i < 100; i++) {
            ArrayList<Integer> a1 = new ArrayList<Integer>();
            for (int j = 0; j < 10; j++) {
                a1.add(10 * i + j);
            }
            ar.add(a1);
        }

        Iterator<ArrayList<Integer>> aIterator = ar.iterator();

        while (aIterator.hasNext()) {
            ArrayList<Integer> a = aIterator.next();
            Iterator<Integer> nIterator = a.iterator();
            while (nIterator.hasNext()) {
                System.out.print(nIterator.next());
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}