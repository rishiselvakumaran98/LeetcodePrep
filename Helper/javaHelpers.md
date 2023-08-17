### To convert a List array to int[] array

```java
List<Integer> = new ArrayList<>();
return result.stream().mapToInt(a -> a).toArray(); // conversion
```

### Swap function

```java
public void swap(int l, int r, int[] arr){
    int temp = arr[l];
    arr[l] = arr[r];
    arr[r] = arr[l];
}
```

### create a copy of array within Range

```java
int [] array = {6,9,8,7,3,1,2,1};
return array.copyOfRange(array,0,3); // {6,9,8,7}
```

### Generating a frequency Map

```java
Map<Integer, Integer> frequencyMap = new HashMap<>();
for (int num: arr){
    frequencyMap.put(num, frequencyMap.getOrDefault(num, 0)+1);
}
```

