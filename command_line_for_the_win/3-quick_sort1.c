#include "sort.h"
#include "sort.h"

void swap(int *a, int *b)
{
        int c;

        c = *a;
        *a = *b;
        *b = c;
}


unsigned int lomuto_partition(int *array, int l, int h, size_t size)
{
        int i, j, pivot;

        pivot = array[h];
        i = l - 1;
        j = h;

        while (i < j)
        {
                do
                {
                        i++;
                }
                while (array[i] < pivot);
                do
                {
                        j--;
                }
                while (array[j] > pivot);
                if (i < j)
                {
                        swap(&array[i], &array[j]);
                        print_array(array, size);
                }
        }
        swap(&array[i], &array[h]);
        print_array(array, size);
        return i;
}


void quicksort(int *array, int l, int h, size_t size)
{
        int j;

        if (l < h)
        {
                j = lomuto_partition(array, l, h, size);
		if (j > 0)
                	quicksort(array, l, j - 1, size);
                quicksort(array, j + 1, h, size);
        }
}

void quick_sort(int *array, size_t size)
{
        if(array == NULL || size == 0)
                return;
	quicksort(array, 0, size - 1, size);
}
