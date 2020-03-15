import java.util.*;

class Trie {

    private ArrayList<Trie> children;

    public void Trie() {

        for (int i = 0; i < 2; i++) {
            children.add(null);
        }
    }

    ArrayList<Trie> getChildren() {
        return this.children;
    }

    void setChildren(int index, Trie trie) {
        this.children.set(index, trie);
    }
}

class Solution {

    void addElement(Trie root, Integer val) {
        Trie curr = root;

        for (int i = 31; i >= 0; i--) {
            int num = val & (1 << i);

            if (curr.getChildren().get(num) == null) {
                curr.setChildren(num, new Trie());
            }
            curr = curr.getChildren().get(num);
        }
    }

    Integer getElement(Trie root, Integer val) {
        Integer result = 0;
        Trie curr = root;
        for (int i = 31; i >= 0; i--) {
            int num = val & (1 << i);
            if (curr.getChildren().get(num) == null) {
                result = result | (1 << i);
                curr = curr.getChildren().get(1 - num);
            } else {
                curr = curr.getChildren().get(num);
            }
        }
        return result;
    }

    Trie buildTrie(ArrayList<Integer> array) {

        Trie root = new Trie();

        Iterator<Integer> it = array.iterator();
        while (it.hasNext()) {
            addElement(root, it.next());
        }

        return root;
    }

    public static void main(String[] args) {

        Solution s = new Solution();
        ArrayList<Integer> array = new ArrayList(10);

        for (int i = 0; i < 10; i++) {
            array.add(i * 10 % 5 + i * 6);
        }

        Trie trie = s.buildTrie(array);
        Integer max_el = Integer.MIN_VALUE;

        for (int i = 0; i < array.size(); i++) {
            max_el = Math.min(max_el, s.getElement(trie, array.get(i)));
        }

        System.out.println(max_el);
    }
}