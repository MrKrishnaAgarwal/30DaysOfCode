<h3> List </h3>

<p> A list is a collection which is ordered and changeable. In Python lists are written with square brackets. </p>

<h4> Create a List </h4>

<p> You can create a list by placing all the items (elements) inside square brackets [], separated by commas. </p>

<p> It can have any number of items and they may be of different types (integer, float, string etc.). </p>

<p> The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. </p>

<p> The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator. </p>

<p> For example − </p>

<pre class="python"><code class="python">list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]
</code></pre>

<h4> Accessing Values in Lists </h4>

<p> To access values in lists, use the square brackets for slicing along with the index or indices to obtain value available at that index. </p>

<p> For example − </p>

<pre class="python"><code class="python">list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
</code></pre>

<p> When the above code is executed, it produces the following result − </p>

<pre class="python"><code class="python">list1[0]:  physics
list2[1:5]:  [2, 3, 4, 5]
</code></pre>