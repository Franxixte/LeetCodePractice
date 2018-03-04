// 选择排序算法
// Selection Sort Algorithm

function selectionSort(arr) {
    var len = arr.length;

    for ( var i = 0; i < len; i++ ) {
        var tar = i;
        for ( var j = i + 1; j < len; j++) {
            if ( arr[tar] > arr[j] ) {
                tar = j;
            }
        }
        var temp = arr[tar];
        arr[tar] = arr[i];
        arr[i] = temp;
    }
    return arr;
}

var lst = [43, 31, 43, 89, 76, 5, 65, 4, 23, 75, 90]

sorted_lst = selectionSort(lst);
console.log(sorted_lst);