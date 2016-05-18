reset
#set terminal png
#set output "simple_train.png"
set style data lines
set key right

# Training loss vs. training iterations
set title "Training loss vs. training iterations"
set xlabel "Training iterations"
set ylabel "Training loss"
plot "simple.log.train" using 1:3 title "2fc"

pause -1

#set output "simple_test.png"
#set style data lines
#set key right

# Test accuracy vs. training time
set ylabel "Test accuracy"
set xlabel "Training time"
plot "simple.log.test" using 2:3 title "2fc"

pause -1
