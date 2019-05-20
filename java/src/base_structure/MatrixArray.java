package base_structure;

public class MatrixArray<T> implements IArray<T> {

    private int size;
    private int vector;
    private IArray<IArray<T>> array;

    public MatrixArray(int vector) {
        this.vector = vector;
        array = new SingleArray<>();
        size = 0;
    }

    public MatrixArray() {
        this(10);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void add(T item) {
        if (size == array.size() * vector)
            array.add(new VectorArray<>(vector));
        array.get(size / vector).add(item);
        size ++;
    }

    @Override
    public T get(int index) {
        return array.get(index / vector).get(index % vector);
    }

    @Override
    public void add(T item, int index) {
        if (index > size || index<0) {
            throw new IndexOutOfBoundsException();
        }
        if (size == array.size() * vector) {
            array.add(new VectorArray<T>(vector));
        }
        int k = index/vector;
        if(k < array.size() - 1) {
            array.get(size / vector).add(array.get(array.size() - 2).get(vector - 1), 0);
            for (int i = array.size()-2; i > k; i --) {
                array.get(i).remove(vector-1);
                array.get(i).add(array.get(i-1).get(vector-1), 0);
            }
            array.get(k).remove(vector-1);
            array.get(k).add(item, index % vector);
        }
        else{
            array.get(k).add(item, index - k * vector);
        }
        size++;
    }

    @Override
    public T remove(int index) {
        if (index >= size || index<0) {
            throw new IndexOutOfBoundsException();
        }
        T item = (T) array.get(index / vector).get(index % vector);
        int k = index/vector;
        array.get(k).remove(index % vector);
        for (int i = k; i < array.size()-1; i++) {
            array.get(i).add(array.get(i+1).get(0), vector-1);
            array.get(i + 1).remove(0);
        }
        size --;
        if(array.get(array.size()-1).size() == 0) {
            array.remove(array.size()-1);
        }
        return item;
    }

    @Override
    public String toString() {
        var str = new StringBuilder();
        for (int i = 0; i < array.size(); i++) {
            str.append(array.get(i)).append('\n');
        }
        return str.toString();
    }
}
