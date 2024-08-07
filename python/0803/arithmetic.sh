echo ">> first :"
read a
echo ">> second :"
read b
echo ">> a=$a, b=$b"

add=`expr $a + $b`
gob=`expr $a \* $b`
na=`expr $a / $b`
avg=`expr $add / 2`
printf "a+b=%d\na*b=%d\na/b=%d\n(a+b)/2=%d\n" $add $gob $na $avg
exit 0
