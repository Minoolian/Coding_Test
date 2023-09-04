package preonboarding;

public class HashTable<K, V> {
    class Entry<K, V> {
        K key;
        V value;
        private boolean isDeleted;

        public Entry(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    private Entry<K, V>[] table;
    private int size;

    public HashTable() {
        this.table = new Entry[1024];
    }

    public int hash(String key) {
        return key.hashCode() % table.length;
    }

    public void put(K key, V value) {
        int indexOfTable = hash((String) key);

        boolean flag = false;
        for (int i = 0; i < table.length; i++) {
            indexOfTable = (indexOfTable + i) % table.length;
            if (table[indexOfTable] == null || table[indexOfTable].isDeleted) {
                flag = true;
                break;
            }

            if(table[indexOfTable].key.equals(key)) throw new RuntimeException("Already has key!");
        }

        if(!flag) throw new RuntimeException("Hash Table is Full!");

        table[indexOfTable] = new Entry<>(key, value);
        size++;
    }

    // A A' A'' -> A X A'' -> A B A''
    // A'이 삭제되고 그 해시값에 맞는 B가 삽입된다면 검색은? 결국 전체 검색하는 최악의 경우도 있지 않을까?
    public Entry<K, V> remove(K key) {
        if (isEmpty()) throw new RuntimeException("Hash Table is Empty!");

        int indexOfTable = hash((String) key);

        boolean flag = false;
        for (int i = 0; i < table.length; i++) {
            indexOfTable = (indexOfTable + i) % table.length;
            if (table[indexOfTable] == null) return null;
            if (table[indexOfTable].key == key) {
                flag = true;
                break;
            }
        }

        if (!flag) return null;

        table[indexOfTable].isDeleted = true;
        size--;
        return table[indexOfTable];
    }

    public V get(K key) {
        int indexOfTable = hash((String) key);

        boolean flag = false;
        for (int i = 0; i < table.length; i++) {
            indexOfTable = (indexOfTable + i) % table.length;
            if (table[indexOfTable] == null) return null;
            if (table[indexOfTable].key == key) {
                flag = true;
                break;
            }
        }

        if (!flag) return null;

        return table[indexOfTable].value;
    }

    public boolean isEmpty() {
        return this.size == 0;
    }
}
